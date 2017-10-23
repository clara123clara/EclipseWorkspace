
import copy
from builtins import str
from _ast import Str
list=[]
newlist=[]
def Fibonacci(list,n):
    newlist.append(0)
    if n ==1:
        return [1]
    for i in range(n):
        if i==0 or i==n-1:
            newlist[i]=1
        else:
            newlist[i]=list[i-1]+list[i]
    return newlist
blanknum=68
for i in range(17):
    blanknum = blanknum - 4
    list=copy.deepcopy(Fibonacci(list,i+1))
    for i in range(blanknum/2):
        print(" ")
    for i in list:
        #print str(i).ljust(6)
        print str(i).ljust(6)
    print(" ")

