import json
from threading import Timer
import redis
import login.webdriver
import getscore as gets


#定时器，#每半个小时执行一次，从redis中取出，一一登录拿cookie即可
def updateCookie():
    print(1)
    t = Timer(3600,updateCookie)
    r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
    all  = r.hgetall("account")
    list = all.keys()#获得键，
    for i in list:
        print(i)
        id=i
        password=json.loads(all[i])['password']
        cookie=login.webdriver.getcookie(id,password)
        if cookie!='':
            cookie = cookie['value']
            r.set("jw"+id,cookie)#redis pip install -U redis==2.10.6
    print(list)
    t.start()

def getscore():
    t = Timer(300, getscore)
    r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
    key = r.hkeys("account")
    for i in key:
        if r.get("jw"+i)!=None:
            gets.score(str(r.get("jw"+i)))

    t.start()
    print(5)

#updateCookie()
#r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
#print(r.get("jw"))
