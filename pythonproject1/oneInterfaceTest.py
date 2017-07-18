'''
Created on 2017年6月28日

@author: Administrator
'''

import requests  
import json  
  
def test_qualification_add():  
    url = "http://www.geneedu.cn"    #测试的接口url  
    headers = {"Content-Type":"application/json"}     
    data = {                                        #接口传送的参数  
        "token": "abcdefg",  
        "id": 1,  
        "param": {  
            "QuId":1    
        }  
    }  
    r = requests.post(url = url,json = data,headers = headers)    #发送请求  
    #return r.json  
    print (r.text)                                                #获取响应报文  
    print (r.status_code)  
      
if __name__=="__main__":  
    test_qualification_add()