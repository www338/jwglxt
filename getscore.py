import json

import redis
import requests
import mail

def score(cookie):
    print(2)
    xh=""
    r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
    header = {
        'Host': 'jwglxt.qust.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '0',
        'Origin': 'http://jwglxt.qust.edu.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://jwglxt.qust.edu.cn/jwglxt/xtgl/index_initMenu.html',
        'Cookie': 'JSESSIONID='+cookie,
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url="http://jwglxt.qust.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005"
    data={
        "xnm":"2019",
        "xqm":"",
        "_search":"false",
        "nd":"1578632832606",
        "queryModel.showCount":"100",
        "queryModel.currentPage":"1",
        "queryModel.sortName":"",
        "queryModel.sortOrder":"asc",
        "time":"0"
    }
    res = requests.post(url=url,headers=header,data=data)
    #有一个cookie过期判断
    print(res.status_code)#成功状态码是200，不成功是901
    if res.status_code==200:
         res = json.loads(res.text)['items']
         print(len(res))
         xh = res[0]['xh']
         #print(xh)
         all=[]
         print(r.llen("score"+xh))
         #获得所有元素
         for i in range(r.llen("score"+xh)):
             all.append(r.lindex("score"+xh,i))
         print(all)
         for i in res:
             if str(i['kcmc']) not in all:
                 r.lpush("score"+xh,i['kcmc'])
                 #sendmail
                 print(5)
                 s = str(i['xh'])+",您的 "+str(i['kcmc'])+' 的分数是 '+str(i['cj'])+",绩点是 "+str(i['jd'])
                 smail=json.loads(r.hget("account",xh))['mail']
                 mail.sendmail(smail,s)

# score("4659AE9637795069CAEA596FB3A19BCB")