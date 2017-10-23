'''
Created on 2017年6月28日

@author: Administrator
'''

'''
import requests
2 response_get = requests.get(url, data, headers, cookies)
3 response_post = requests.post(url, data, headers, cookies)
'''

import requests
import json


if __name__ == '__main__':
    
    urldata='http://www.baidu.com'
    urldata1='http://www.geneedu.cn'
    r=requests.get(urldata)
    print(r.status_code)  # 获取返回状态
    
    rr = requests.get(urldata, params={'wd':'python'}) 
    print(rr.url)
    print(rr.text)
    
    #r3 = requests.post(urldata, data=json.dumps({'wd': 'data'}))
    #print(r3.json())
    
    try:
        r = requests.get(urldata1, params={'ip': '8.8.8.8'}, timeout=1)
        r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        result = r.json()
    print(type(result), result, sep='\n')
    
    