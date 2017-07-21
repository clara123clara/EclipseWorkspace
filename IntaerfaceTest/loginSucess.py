'''
Created on 2017年7月19日
主要完成登陆功能
@author: Administrator
'''

import requests
import json
import re

cookie1={}
cookie2={}
cookie3={}
cookie4={}


def test_login():
    url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
   # header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data={
        "returnUrl":"",
        "userVo.loginName":"chenjiajia",
        "userVo.password":"ac1e1f9138e18dcca01311bd10abecf5"
        }
    requestsend=requests.post(url=url,data=data)  #发送请求
    
    #print(requestsend.url)
    print(requestsend.text)
    print(requestsend.status_code)
    
    
    #获取返回的json数据
    s=json.loads(requestsend.text)
    print(s.keys())
    print(s['data'])
    print(s['data']['returnUrl'])
    
    
    '''
            获取cookies,并通过正则表达式分别获取想要的值
    '''
    global myHeader,myCookies,cookie1,cookie2,cookie3,cookie4
    myHeader=requestsend.headers
   
    #print("-------------------------")
    #print(a)
    myCookies=myHeader.get("Set-Cookie")
    print("我的Cookies:",myCookies)
    
    p = '(?<=edustar_login_token=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie1 = matcher1.group(0)
    print(cookie1)
    
     
    p = '(?<=sso_key=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie2 = matcher1.group(0)
    print(cookie2)
    
     
    p = '(?<=sso_token=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie3 = matcher1.group(0)
    print(cookie3)
 
    p = '(?<=JSESSIONID=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie4 = matcher1.group(0)
    print(cookie4)   
    
    
if __name__ == '__main__':
    test_login()
    