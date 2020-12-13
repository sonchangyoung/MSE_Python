#!/usr/bin/env python
# coding: utf-8

# In[2]:


per = ["10.31", "", "8.00"]

for i in per:
    try: #실행 코드
        print(float(i))
    except: #예외가 발생했을 때 수행할 코드
        print(0)
    else:#예외가 발생하지 않았을 때 수행할 코드
        print("clean data")
    finally:#예외 발생 여부와 상관없이 항상 수행할 코드
        print("변환 완료")


# In[ ]:




