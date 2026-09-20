# AlertN
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ke46138/AlertN?style=flat-square&color=2a5c03)

Reticulum LXMF бот для рассылки уведомлений о тревогах

## Требования
1. Python 3
2. MySQL
3. [BPLA_api](https://github.com/ke46138/BPLA_api)

## Запуск
0. Настройте и запустите [BPLA_api](https://github.com/ke46138/BPLA_api)
1. Склонируйте репозиторий:
    - Через HTTP `git clone https://github.com/ke46138/AlertN`
    - Через RNS `rns://7cf12e0bb855cb6167df9c5f20d9cfd3/public/AlertN`
2. Перейдите в склонированный репозиторий
    - `cd AlertN`
3. Установите зависимости
    - `pip install -r requirements.txt`
4. Скопируйте конфиг и отредактируйте его по своему вкусу
    - `cp config.example.py config.py`
    - `nano config.py`
5. Подготовьте базу данных
    - `python3 prepare_database.py`
6. Запустите
    - `python3 main.py`
