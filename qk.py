import time

import requests
import json
kcxx={}
session = requests.session()
sessionid=""
xh=""
header={
    'Host': 'jwglxt.qust.edu.cn',
    'User - Agent': 'Mozilla / 5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length': '467',
    'Origin': 'http://jwglxt.qust.edu.cn',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID =856E60C2961F381F2E4D27AAF05A005F',
    'Pragma': 'no - cache',
    'Cache - Control': 'no - cache',
    'Referer':'http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1708010117'

}

def getsessionid():
    global sessionid
    global xh
    sessionid="8388E7E89B5116D6CB2C8CCDB00B1C43"
    xh="1708080121"

def getall():
    global session
    global sessionid
    for i in range (2,10):
        header={
            'Host': 'jwglxt.qust.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '0',
            'Origin': 'http://jwglxt.qust.edu.cn',
            'Connection': 'keep-alive',
            'Referer': 'http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1708010117',
            'Cookie': 'JSESSIONID='+sessionid,
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        global xh
        url="http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su="+xh
        datas={
            'yl_list[0]':'0',
            'yl_list[1]':'1',
            'rwlx':'2',
            'xkly':'0',
            'bklx_id':'0',
            'xqh_id':'2',
            'jg_id':'08',
            'zyh_id':'0801',
            'zyfx_id':'wfx',
            'njdm_id':'2017',
            'bh_id':'17080101',
            'xbm':'1',
            'xslbdm':'421',
            'ccdm':'3',
            'xsbj':'1',
            'sfkknj':'0',
            'sfkkzy':'0',
            'sfznkx':'0',
            'zdkxms':'0',
            'sfkxq':'1',
            'sfkcfx':'0',
            'kkbk':'0',
            'kkbkdj':'0',
            'xkxnm':'2019',
            'xkxqm':'12',
            'rlkz':'0',
            'kspage':i*10-9,
            'jspage':i*10,
            'jxbzb':'',
            'kklxdm':'10'
        }
        res = requests.post(url=url,headers=header,data=datas)
        #print(res.text)

def getB200():
    global sessionid
    global xh
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
        'Referer': 'http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1708010117',
        'Cookie': 'JSESSIONID='+sessionid,
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url="http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su="+xh
    datas = {
        'yl_list[0]': '1',
        'filter_list[0]': 'B200',
        'rwlx': '2',
        'xkly': '0',
        'bklx_id': '0',
        'xqh_id': '2',
        'jg_id': '08',
        'zyh_id': '0801',
        'zyfx_id': 'wfx',
        'njdm_id': '2017',
        'bh_id': '17080101',
        'xbm': '1',
        'xslbdm': '421',
        'ccdm': '3',
        'xsbj': '1',
        'sfkknj': '0',
        'sfkkzy': '0',
        'sfznkx': '0',
        'zdkxms': '0',
        'sfkxq': '1',
        'sfkcfx': '0',
        'sfkgbcx':'0',
        'kkbk': '0',
        'kkbkdj': '0',
        'xkxnm': '2019',
        'xkxqm': '12',
        'rlkz': '0',
        'kspage':1,
        'jspage': 10,
        'jxbzb': '',
        'kklxdm': '10',
        'tykczgxdcs':10,
        'sfrxtgkcxd':1
    }
    res = requests.post(url=url,headers=header,data=datas)
    print(res.text)
    res=json.loads(res.text)
    global kcxx
    for i in res['tmpList']:
        if "走近工程图学" not in i['kcmc']and"橡胶与人类" not in i['kcmc'] and "化学与健康" not in i['kcmc']:
            print("正在抢课"+i['kcmc'])
            kcxx['kch_id']=i['kch_id']
            print(i['kch_id'])
            kcxx['kcmc']='('+i['kch_id']+')'+i['kcmc']+'+-+'+i['xf']+'+学分'
            getxkkzid()
            getkc()
            select()
    #print(kcxx)


def getxkkzid():
    global sessionid
    global xh
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
        'Cookie': 'JSESSIONID=E53B4BBA627C3634244619BEA14A559F',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url="http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su="+xh
    # res = requests.get(url=url,headers=header)
    # res=res.text.split("firstXkkzId")[2].split("value=\"")[1].split("\"")[0]
    # global  kcxx
    # kcxx['jxb_id']=res
    # print(res)

#获得课程详细信息
def getkc():
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
    'Referer': 'http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1708010117',
    'Cookie': 'JSESSIONID='+sessionid,
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
    global kcxx
    print(kcxx['kch_id'])
    url="http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxJxbWithKchZzxkYzb.html?gnmkdm=N253512&su="+xh
    datas={
         'rwlx': '2',
    'xkly': '0',
    'bklx_id': '0',
    'xqh_id': '2',
    'jg_id': '08',
    'zyh_id': '0801',
    'zyfx_id': 'wfx',
    'njdm_id': '2017',
    'bh_id': '17080101',
    'xbm': '1',
    'xslbdm': '421',
    'ccdm': '3',
    'xsbj': '1',
    'sfkknj': '0',
    'sfkkzy': '0',
    'sfznkx': '0',
    'zdkxms': '0',
    'sfkxq': '1',
    'sfkcfx': '0',
    'sfkgbcx': '0',
    'kkbk': '0',
    'kkbkdj': '0',
    'xkxnm': '2019',
    'xkxqm': '12',
    'rlkz': '0',
    'kspage': 1,
    'jspage': 10,
    'jxbzb': '',
    'kklxdm': 10,
    'tykczgxdcs': 10,
    'sfrxtgkcxd': 1,
    'kch_id':kcxx['kch_id'],
    'xkkz_id':'9AE3C2EC10A86D6DE055000000000001',
    'cxbj':0,
    'fxbj':0
    }

    res = requests.post(url=url, headers=header, data=datas)
    print(res.text)

    res = json.loads(res.text)[0]
    print(res)
    kcxx['jxb_ids']=res['do_jxb_id']

def select():
    global sessionid
    global xh
    global kcxx
    print(kcxx)
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
        'Referer': 'http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1708010117',
        'Cookie': 'JSESSIONID='+sessionid,
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url = "http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_xkBcZyZzxkYzb.html?gnmkdm=N253512&su="+xh
    datas = {
        'jxb_ids':kcxx['jxb_ids'],
        #'jxb_ids':'50fe5f32b31483e78eaefdee33fc6fd3818efc5f3dfc4d88a5f9aab9aeef55a06d7357485e8dd52f341dbe6cb9bfff386c4bca36f9da3688b475f1b15ea511016684cd1dc0e97a800e24a9915f25b4f407a7f696a0a24e9d3bb3bf1dfa4816400ea5596b8ff69f1ff95f7de321c11241081c7dc6a86dc1f479c0ad229b6bf93d',
         'kch_id':kcxx['kch_id'],
        'kcmc':kcxx['kcmc'],
        'rwlx':'2',
        'rlkz':'0',
        'rlzlkz	':'1',
        'sxbj':'1',
        'xxkbj':0,
        'qz':0,
        'cxbj':0,
        'xkkz_id':'9AE3C2EC10A86D6DE055000000000001',
        'njdm_id':'2017',
        'zyh_id':'0801',
        'kklxdm':'10',
        'xklc':'2',
        'xkxnm':'2019',
        'xkxqm':'12'
    }
    res = requests.post(url=url, headers=header, data=datas)
    print(res.text)



getsessionid()
#getall()
i=1
while(1):
    try:
        getB200()
        i+=1
        print(i)
        time.sleep(0.15)
    except Exception:
        print(Exception.__text_signature__)
        pass
    continue

