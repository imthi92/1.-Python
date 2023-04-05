#!/usr/bin/env python
# coding: utf-8

# In[4]:


# print 0 to 20 by using range
range(0,20)
for num in range(0,20):
    print(num)


# In[10]:


# print range 10 to 20

range(10,20)
for num in range(10,20):
    print(num)


# In[13]:


# Print number of items in the list by using 'len'
Lists=[10, 20, 14, 55, 43, 87, 76]
print(len(Lists))


# In[27]:


print("Artificial Intelligence")


# In[32]:


Name=input("-Your Name-")
Age=int(input("-Your Age-"))
Profession=input("-Your Profession-")


# In[41]:


# 1, 'Welcome', 2, 'Hope'
lists = [1,2,3,4,5]
print(tuple(lists))


# In[42]:


Tuple1=(1, 'Welcome', 2, 'Hope')
print(Tuple1)


# In[43]:


Tuple1=(0,1,2,3)
Tuple2=('python', 'HOPE')
Tuple3=Tuple1,Tuple2
print(Tuple3)


# In[66]:


lists=[20,10,16,19,25,1,276,188]
for num in (lists):
    if(num % 2) == 1:
        print(num,"Odd number")
else:
     print(num,"Even number")


# In[69]:


lists=[20,10,16,19,25,1,276,188]
for num in (lists):
    if(num % 2) == 0:
        print(num,"Even number")


# In[ ]:




