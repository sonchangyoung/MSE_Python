#!/usr/bin/env python
# coding: utf-8

# In[53]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)
#수익금은 마감-오픈 이다 그래서 4번째에서 1번째를 뺀값이다
# 수익금을 for 문을 이용하여 계속 더한값이 출력값이 된다.


# In[ ]:





# In[ ]:




