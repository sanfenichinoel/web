import time
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import uvicorn

from mysql import Mysql
from mywater import Mysql_water
from mypwd import IsMe

mysql = Mysql()
mywater = Mysql_water()

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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

#  markdown 文件 ####################################################
@app.get("/sqlapi/files/allmyfiles")
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

@app.get("/sqlapi/files/insert")
@limiter.limit("1/3second")
def Insert(name:str, request: Request):
    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    _url = "../md/" + name + ".md"

    ok = mysql.insert(name, _time, _url)
    return ok


##  水    #########################################
@app.get("/sqlapi/water/allmywater")
def AllMyFile():
    myWaters = mywater.select_all_data()

    if myWaters is False:
        return "select error"

    waters = []
    for water in myWaters:
        _water = {
            "water": water[0],
            "time": water[1]
        }
        waters.append(_water)
    return waters

@app.get("/sqlapi/water/insert")
@limiter.limit("1/3second")
def Insert(water:str, request: Request):
    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    ok = mywater.insert(water, _time)
    return ok


@app.get("/sqlapi/water/delete")
def Delete(_time:str):
    ok = mywater.delete(_time)
    return ok


# login  ########################################
@app.get("/login")
@limiter.limit("1/3second")
def Login(pwd:str, request: Request):
    return IsMe(pwd)


if __name__ == "__main__":
    uvicorn.run("apis:app", host="0.0.0.0", port=8010, log_level="info")
