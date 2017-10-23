'''
Created on 2017年8月10日

@author: Administrator
'''

import requests


def sendmessage():
    url='http://feedback.hao.360.cn/index/submit'
    data={
        "sectionid":1,
        "referer":"http://feedback.hao.360.cn/",    
        "contact":"qqqqqqqqqqqqrrrrr",  
        "deviceinfo":{
        "screen":"1920*1080",
        "browser":{
            "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "platform":"Win32",
            "product":"Gecko",
            "language":"zh-CN",
            "vendor":"Google Inc.",
            "cookieEnabled":true,
            "onLine":true}
                      },    
        "message":"qqqqqqqqq",    
        }
    Msend=requests.post(url=url,data=data)

if __name__ == '__main__':
    sendmessage()