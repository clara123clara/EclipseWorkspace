#coding=utf-8
'''
Created on 2017年7月3日

@author: Administrator
'''

import checkapi_post
import ComQuestion_data


#请求地址
url="http://xxxx.xxxx.xx/xxx/xxxxxx/CommitQuestion"

data1=ComQuestion_data.data('30010384200','139****1094','python自动化脚本001','000001','平安银行',2,1,2,'python自动化测试数据001')
data2=ComQuestion_data.data('300034228661','180****1650','自动化脚本002','000001','平安银行',2,1,2,'python自动化测试数据001')
data1=ComQuestion_data.convert_data(data1)
data2=ComQuestion_data.convert_data(data2)

checkapi_post.checkapi_post(url, data1)
checkapi_post.checkapi_post(url, data2)