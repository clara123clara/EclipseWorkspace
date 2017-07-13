'''
Created on 2017年7月3日

@author: Administrator
'''

import urllib.request
import json

def checkapi_post(url,data):
    #把参数进行编码
    data=urllib.request.urlencode(data)
    
    #.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    url2=urllib.Request(url,data)
    
    #.urlopen打开上一步返回的结果，得到请求后的响应内容
    response=urllib.urlopen(url2)
    
    #将响应内容用read()读取出来
    apicontent=response.read()

    #将str对象转换成json对象
    context=json.loads(apicontent)
    
    #读取json对象中的RetCode的值
    retcode=context['RetCode']
    
    print context
    #跟进返回的状态进行判断
    if retcode!='0':
        print(retcode+' '+u"提交失败")
    else:
        print(retcode+' '+u"提交成功")