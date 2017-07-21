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


import data_Test.loadJsonData

#构造测试集  
suite = unittest.TestSuite() #实例化  （实例化测试套件）

#TestSuite类的addTest()方法把不同测试类中的测试方法组装到测试套件中。  
#增加测试用例==》接口文件名.接口类(方法也就是这个接口的其他用例),要把每一个测试用例都增加进来！！！ 

#将测试用例加载到测试套件中，执行顺序是安装加载顺序
suite.addTest(test_PackageClass.test_loginTest("test_login_Name_right"))
suite.addTest(test_PackageClass.test_loginTest("test_login_Name_error"))
#执行测试用例，实例化TextTestRunner类
#runner=unittest.TextTestRunner()
#使用run()方法运行测试套件（即运行测试套件中的所有用例）
#runner.run(suite)


'''
#以上方法同时可以构造测试集
#test_dir = './'
test_dir = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#执行测试用例，实例化TextTestRunner类
runner=unittest.TextTestRunner()
#通过该类下面的discover()方法可自动更具测试目录test_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover
runner.run(discover)  

'''

if __name__ == '__main__':

    #按照一定的格式获取当前的时间   
    now = time.strftime("%Y-%m-%d %H_%M_%S")  
                 
    #定义报告存放路径     
    filename = './' + now + 'test_result.html'  
    fp = open(filename,"wb")   
                 
    #定义测试报告  
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,verbosity=1,title = "登陆接口测试报告",description = '测试用例执行情况')   
      
    #运行测试   
    runner.run(suite)  
    fp.close()#关闭文件对象把数据写进磁盘        
    
    
    
    