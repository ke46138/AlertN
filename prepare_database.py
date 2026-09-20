#!/usr/bin/env python3

import pymysql

from modules.logger import logger
import config

logger.info("Подключение к MySQL")

connection = pymysql.connect(
    host=config.MYSQL_HOST,
    port=config.MYSQL_PORT,
    user=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD,
    database=config.MYSQL_DATABASE,
    charset="utf8mb4",
    autocommit=False,
)

queries = (
    """
CREATE TABLE IF NOT EXISTS messages_history (
    id INT(11) NOT NULL AUTO_INCREMENT,
    time BIGINT(20) NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    text TEXT NOT NULL,
    PRIMARY KEY (id)
)""",
    """
CREATE TABLE IF NOT EXISTS sub_users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    identity_hash VARCHAR(32) NOT NULL,
    subscribed TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE KEY user_unique_idx (identity_hash),
    KEY subscribed_idx (subscribed)
)""",
)

logger.info("Создание таблиц")

with connection.cursor() as cursor:
    for query in queries:
        cursor.execute(query)

connection.commit()

logger.info("Готово")