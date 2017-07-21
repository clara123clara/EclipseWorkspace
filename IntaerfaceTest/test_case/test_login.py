'''
Created on 2017年7月19日

@author: Administrator
'''
import requests
import json
import unittest
import re
from subprocess import call


class test_loginTest(unittest.TestCase):     #封装测试环境的初始化和还原的类  
    '''接口名称：用户登陆 '''
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！  
        print("start test")  
        pass  
    def tearDown(self):             #与setUp()相对  
        print("end test")  
        pass  
        
    def test_login_Name_right(self):
        ''' 测试用例：用户名和密码都正确'''
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        
        self.data={
            "returnUrl":"",
            "userVo.loginName":"chenjiajia",
            "userVo.password":"ac1e1f9138e18dcca01311bd10abecf5"
            }
        self.r=requests.post(url=self.url, data=self.data)
        
        print(self.r.text)
        print(self.r.status_code)
        
        #正确反馈的json数据
        s=json.loads(self.r.text)
        responseData=s['data']['returnUrl']
        #断言数据是否正确
        self.assertIn("/honeybee/personcenter/index.do",self.r.text)
        
    def test_login_Name_error(self):
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        self.data={
            "returnUrl":"",
            "userVo.loginName":"chenjiajia1",
            "userVo.password":"error"
            }
        self.r=requests.post(url=self.url, data=self.data)
        #print(self.r.text)
        #print(self.r.status_code)
        self.assertIn("/honeybee/personcenter/index.do",self.r.text)
        
if __name__ == '__main__':
    # unittest.main()
    #test_loginTest("setUp")
    a = test_loginTest()
    a.test_login_Name_right();    
        