'''
Created on 2017年10月20日

@author: Administrator
'''

import unittest

if __name__ == '__main__':
    
    
    test_dir="./test_case/"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    #执行测试用例，实例化TextTestRunner类
    runner=unittest.TextTestRunner()
    #通过该类下面的discover()方法可自动更具测试目录test_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover
    runner.run(discover) 
