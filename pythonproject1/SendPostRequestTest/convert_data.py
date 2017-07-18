'''
Created on 2017年7月3日

@author: Administrator
'''

class data(object):
    def __init__(self,User,UserPhone,Title,StockId,StockName,ModelId,UserGrade,IsFree,SelfStr):
        self.User=User
        self.UserPhone=UserPhone
        self.Title=Title
        self.StockId=StockId
        self.StockName=StockName
        self.ModelId=ModelId
        self.UserGrade=UserGrade
        self.IsFree=IsFree
        self.SelfStr=SelfStr
 
#对象类型转换成字典类型       
def convert_data(obj):
        dict={}
        dict.update(obj.__dict__)
        return dict