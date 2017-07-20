'''
Created on 2017年7月19日

@author: Administrator
'''
import requests  
import json  
import login_OneInterfaceTest
import re  


def test_qualification_add():  
    url = "http://www.geneedu.cn/vote/vote_save.do"    #测试的接口url  
    header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"} 

    cookies={"edustar_login_token":login_OneInterfaceTest.cookie1,
            "sso_key":login_OneInterfaceTest.cookie2, 
            "sso_token":login_OneInterfaceTest.cookie3,
            "JSESSIONID":login_OneInterfaceTest.cookie4                                          
             }
    data = {           
            "vote.title":"投票主题",
            "vote.description":"描述",
            "voteEndTime":"2017-10-17 10:29",    
            "vote.type":"true",
            "vote.visible":"true",
            "content":"投票主题",
            "content":"投票主题投票主题投票主题",
            "vote.voteId":0,
            "vote.userId":"",   
            "vote.counts":0,
            "vote.createTime":"",    
            "vote.status":"false",
            "containerType":"user",
            "containerName":"",  
            "containerId":"",   
            "appCode":"",
            "appId":"",
            "appName":"",
            "sign":"91fd45de94e2d053a5c835d3b3af3b21",
            "returnUrl":"",
    }  
    r = requests.post(url = url,data = data,cookies=cookies)    #发送请求  
    #return r.json  
    print ("r.text打印：",r.text)                                                #获取响应报文  
    print ("“状态骂打印:",r.status_code)  


if __name__=="__main__":  
    login_OneInterfaceTest.test_login()
    test_qualification_add()  
    
    
    
    