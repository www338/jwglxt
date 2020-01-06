import requests
import json
import rsa
import binascii
import base64
import execjs
session = requests.session()

url="http://jwglxt.qust.edu.cn/jwglxt/xtgl/login_slogin.html?time=1578239704797"

publicKeyUrl="http://jwglxt.qust.edu.cn/jwglxt/xtgl/login_getPublicKey.html?time=1578239704797"

modulus=""

exponent=""

csrftoken=""

yhm=""

mm=""

header={
    'Host': 'jwglxt.qust.edu.cn',
    'User - Agent': 'Mozilla / 5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length': '467',
    'Origin': 'http://jwglxt.qust.edu.cn',
    'Connection': 'keep-alive'
}
def getCsrftoken():
    #获得csrftoken
    global url
    global header
    global session
    global csrftoken
    res=requests.get(url,header)
    res = res.text.split("csrftoken")[2].split("value=\"")[1].split("\"")[0]
    csrftoken = res
    print(res)
def getPublickKey():
    global publicKeyUrl
    global modulus
    global exponent
    global header
    res = requests.get(publicKeyUrl,header)
    modulus = json.loads(res.text)['modulus']
    exponent = json.loads(res.text)['exponent']
    print(modulus,exponent)

def Rsa(password):
    global modulus
    global exponent
    global mm
    mm = str(mm).encode()
    publickey = rsa.PublicKey(b64othex(modulus),b64othex(exponent))
    mm = (rsa.encrypt(password.encode(),publickey))
    print(mm)

def b64othex(s):
    f = open('base64.js', 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    jsf = htmlstr
    js = execjs.compile(jsf)
    return js.call("b64tohex",s)  # 执行js，并传入参数

def hex2b64(s):
    f = open('base64.js', 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    jsf = htmlstr
    js = execjs.compile(jsf)
    return js.call("hex2b64", s)  # 执行js，并传入参数




getCsrftoken()
getPublickKey()
Rsa("15689926302")
