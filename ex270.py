#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Stock: 
    def __init__(self, name, code, per, pbr, 배당수익률): 
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
# class 를 이용해서 name과  code를 설정하고 리턴하게한다. 
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
# for 을 이용해서 삼성 현대차 LG전자 의 코드 변수와 이름 변수를 순서대로 3개 출력한다    


# In[ ]:




