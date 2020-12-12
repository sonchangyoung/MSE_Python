#!/usr/bin/env python
# coding: utf-8

# In[38]:


list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
  split = i.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(i)
# for 함수를 이용해 하나씩 출력하고 조건을 건다 split 함수로.을 기준으로 분류한후에
#if 함수로 조건을 건다 쪼개는것의 첫번째단어가 h 나 c 면 변수를 출력하라


# In[ ]:





# In[ ]:




