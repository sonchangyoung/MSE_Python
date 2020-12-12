#!/usr/bin/env python
# coding: utf-8

# In[54]:


def message1(): # message1()이 입력되면 A를 출력한다
    print("A")

def message2(): #message2()이 입력되면 B 를출력한다
    print("B")

def message3():
    for i in range (3) : #message3()이 입력되면B를 출력하는데 그 뒤에 C도 출력한다 그걸 for 문으로 3번 반복한다
        message2()
        print("C")
    message1()    #그후 for 문에 포합되지 않은 message1()을 마지막으로 독립시행한다. 

message3()


# In[ ]:





# In[ ]:




