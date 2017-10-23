'''
Created on 2017年7月19日

@author: Administrator

'''

import unittest  
import json  
import requests  
#加载HTMLTestRunner，用于生成HTMLreuslt
import HTMLTestRunner 
import time

from test_case.test_login import *



#构造测试集  
suite = unittest.TestSuite() #实例化  （实例化测试套件）
#suite.addTest(test_loginClass("test_login"))


for i in range(len(userAccount)):
    print("现在的循环次数为：",i)
    suite.addTest(test_loginClass("test_do"))
print("打印完成")




if __name__ == '__main__':
    
    test_dir = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_case"  
    test_report = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_report" 

    #按照一定的格式获取当前的时间   
    now = time.strftime("%Y-%m-%d %H_%M_%S")  
                 
    #定义报告存放路径     
    filename = test_report + "\\" + now + 'result.html'   
    fp = open(filename,"wb")   
                 
    #定义测试报告  
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = "登陆接口测试报告",description = '测试用例执行情况')   
      
    #运行测试   
    runner.run(suite)  
    fp.close()#关闭文件对象把数据写进磁盘        
    
    
    
    