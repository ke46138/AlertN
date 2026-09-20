import threading
import queue
import time

from google.protobuf.empty_pb2 import Empty
import grpc

from generated import max_bridge_pb2_grpc

from modules import broadcaster
from modules import mysql_adapter as sql
from modules.logger import logger

import config

stop_event = threading.Event()

def grpc_worker():
    while not stop_event.is_set():
        channel = None

        try:
            channel = grpc.insecure_channel(
                f"{config.GRPC_HOST}:{config.GRPC_PORT}"
            )
            stub = max_bridge_pb2_grpc.MaxBridgeStub(channel)

            for event in stub.Subscribe(Empty()):
                if stop_event.is_set():
                    return
                try:
                    sql.write_message(event.text)
                    broadcaster.broadcast(event.text)
                except queue.Full:
                    pass
        except grpc.RpcError:
            logger.exception(f"Ошибка gRPC")
            time.sleep(5)
        finally:
            if channel is not None:
                channel.close()
