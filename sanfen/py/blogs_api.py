import json
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import pymysql
from mysql import Mysql

mysql = Mysql()

app = FastAPI()

origins = [
    "http://www.sanfensum.cn",
    "http://sanfensum.cn"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/allmyfiles")
def AllMyFile():
    myFiles = mysql.select_all_data()

    if myFiles is False:
        return "select error"

    data = []
    for file in myFiles:
        _data = {
            "name": file[0],
            "time": str(file[1]).replace("T", " "),
            "url": file[2]
        }
        data.append(_data)
    return data

@app.get("/insert")
def Insert(name:str):
    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    _url = "../md/" + name + ".md"

    ok = mysql.insert(name, _time, _url)
    return ok

if __name__ == "__main__":
    uvicorn.run("blogs_api:app", host="0.0.0.0", port=8010, log_level="info")