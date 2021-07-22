#!/usr/bin/env python
# coding: utf-8

# In[1]:


#定義一函數，經由此函數能將輸入數字反轉
def reverse(number):
    reverse_number=0
    while number!=0:
        #找出輸入數字除以10的餘數
        remainder=number%10
        #將餘數加到reverse_number中
        reverse_number=reverse_number*10+remainder
        #將輸入數值除以10，這個數字會再次進入迴圈，進行取餘數，加到reverse_number
        number=number//10
    print(reverse_number)


# In[2]:


num = int(input('Enter an integer:'))
reverse(num)

