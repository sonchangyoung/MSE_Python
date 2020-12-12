#!/usr/bin/env python
# coding: utf-8

# In[47]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    diff= high_prices[i] - low_prices[i]
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)    
#변동폭 diff를 고가차-저가차 로 설정하고 인덱싱 숫자가 동일한것끼리 차를 구한다 
# volatility = [] 따로 숫자를 나열하기 위해 리스트를 만들고 출력한다.


# In[ ]:





# In[ ]:




