#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:
  def __init__(self): 
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()
# 프린트로 자식 생성을 하면 super을 이용해 부모에 명시적으로 접근하여 부모도 출력을 한다 .

나 = 자식()


# In[ ]:




