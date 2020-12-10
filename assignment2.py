#!/usr/bin/env python
# coding: utf-8

# #### 1. Create the below pattern using nested for loop in Python. 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# 

# In[9]:


n = 4
for i in range(n):
    for j in range(0, i+1):
        print('*', end = "")
    print("\r") 
for i in range(n, -1, -1):
    for j in range(0, i+1):
        print('*', end = '')
    print('\r')    
        


# #### 2. Write a Python program to reverse a word after accepting the input from the user. Sample Output: 
# Input word: ineuron 
# Output: norueni
#  

# In[14]:


#print("enter input")
inp = input('Input word: ')

out = inp[::-1]

print("Output:",out)


# In[ ]:




