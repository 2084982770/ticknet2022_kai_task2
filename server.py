import os

from fastapi import FastAPI, UploadFile, Body, File
from uvicorn import run
from shutil import rmtree
from datetime import datetime
from sys import argv
from yaml import Loader, load
from os.path import exists
from zipfile import ZipFile
from io import BytesIO

if '--nocolor' in argv:
    RED = ''
    BLUE = ''
    GREEN = ''
    RESET = ''
else:
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


def config():
    if not exists('server.yml'):
        print(f'{RED}"server.yml" do not exists{RESET}')
        exit(1)
    with open('server.yml', mode='r', encoding='utf8') as f:
        cfg = load(f, Loader=Loader)
    return cfg


app = FastAPI()


@app.post('/submit')
async def _submit(lesson: int = Body(), key: str = Body(), file: UploadFile = File()):
    cfg = config()
    if lesson >= len(cfg['lessons']):
        return {'msg': f'Lesson {lesson} not exists', 'code': 4}
    else:
        lesson = cfg['lessons'][lesson]

    if not exists(cfg['dir_path']):
        os.mkdir(cfg['dir_path'])
    lesson_dir = f"{cfg['dir_path']}/{lesson['lesson_dir']}"
    if not exists(lesson_dir):
        os.mkdir(lesson_dir)

    day = datetime.now().strftime("%Y-%m-%d")
    start_time = datetime.strptime(lesson['start_time'], "%Y-%m-%d")
    end_time = datetime.strptime(lesson['end_time'], "%Y-%m-%d")

    if start_time > datetime.now():
        return {'msg': '未到开始提交世界', 'code': 1}
    if datetime.now() >= end_time:
        return {'msg': '提交时间已经结束结束', 'code': 2}

    for each in cfg['people']:
        if key == each['key']:
            file_dir = f'{lesson_dir}/{each["name"]}-{day}'
            break
    else:
        return {'msg': f'Secret key wrong', 'code': 3}
    if exists(file_dir):
        rmtree(file_dir)

    temp = await file.read()
    with ZipFile(BytesIO(temp)) as zf:
        zf.extractall(file_dir)

    return {'msg': 'Successful', 'code': 0}
