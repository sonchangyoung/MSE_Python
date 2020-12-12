#!/usr/bin/env python
# coding: utf-8

# In[69]:


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#순서를 보면 함수 2에 2를 넣는다 num=12 가되고 return 을 이용하여 함수 1 에 12를 넣는다 num= 14r가 되고
#return 하여 함수 0에 14를 넣는다 값=28이된다.


# In[ ]:





# In[ ]:




