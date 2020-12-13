#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
#계좌번호를 랜덤으로 설정하려고 랜덤을 불러온다  
    
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"    #은행이름은 SC은행 으로 하고 3자리 2자리 6자리로 
                                #xxx-xx-xxxxxx 이런식으로 숫자배열은 랜덤으로 설정한다 

        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
#입금은 최소 1원 이상해야한다.
    @classmethod 
    def get_account_num(cls): 
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):  #account 에서 입금을위한 deposit 함수를 만든다 
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 입금 횟수가 5회가 될때마다 총 잔고의 1% 이자가 붙는다
                # 이자 지금
                self.balance = (self.balance * 1.01)

#통장 잔고 이상은 출금 할 수 없다 
#account 에서 출금을 하기위한 withdraw 함수를 만든다 
    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):    #account 에서 정보를 출력하는 display 함수를 만든다
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):    #for 문을 이용해서 입금과 출금값을 출력하는  withdraw_history 와  deposit_history 함수를 만든다
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
#계좌에 입금한다
k.deposit(100) 
k.deposit(200)
k.deposit(300)
k.deposit_history()

#계좌에서 출금한다
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()


# In[ ]:




