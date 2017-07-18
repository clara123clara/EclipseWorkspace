'''
Created on 2017年6月27日

@author: Administrator
'''

import urllib.request


urldata = "http://www.baidu.com/"

s_save=urllib.request.urlopen(urldata).read()
print(s_save)

if urldata=="http://www.baidu.com/":
    print("输入的百度页面")
else:
    print("输入浏览器地址错误！！！")

    




'''
try:
    s_save = urllib.urlopen(urldata).read()
5   print(urldata)
except urllib.HTTPError, e:
    print(e.code)
except urllib.URLError, e:
    print(str(e))
'''