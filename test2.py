import requests
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
    'Cookie': 'JSESSIONID=856E60C2961F381F2E4D27AAF05A005F',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
url = "http://jwglxt.qust.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su=1708010117"
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
    'sfkgbcx': '0',
    'kkbk': '0',
    'kkbkdj': '0',
    'xkxnm': '2019',
    'xkxqm': '12',
    'rlkz': '0',
    'kspage': 1,
    'jspage': 10,
    'jxbzb': '',
    'kklxdm': '10',
    'tykczgxdcs': 10,
    'sfrxtgkcxd': 1
}
res = requests.post(url=url, headers=header, data=datas)
print(res.text)