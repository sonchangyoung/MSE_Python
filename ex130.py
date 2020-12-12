#!/usr/bin/env python
# coding: utf-8

# In[28]:


#비트코인의 데이터를 가져온다
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭, 시가 , 최고가 , 최저가의 값을 불러온다
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
최저가 = float(btc['min_price'])
# (시가+변동폭)이 최고가 보다 높으면 "상승장"을, 그렇지 않으면 "하락장"을 출력하도록 if else 를 사용한다.
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장") 


# In[ ]:





# In[ ]:




