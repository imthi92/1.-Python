#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:


def traingle():
    heightvalue=int(input("Height:"))
   # print("Height", heightvalue)
    var=heightvalue, "height in cm"
    
    breadthvalue=int(input("Breadth:"))
    # print("breadth", breadthvalue)
    var=breadthvalue, "breadth in cm"

    Areaformula=(heightvalue*breadthvalue)/2
    print("Aarea of the triangle is:", Areaformula)
    
    height1=int(input("Height1:"))
    var="height1 in cm"
    
    height2=int(input("Height2:"))
    var="height2 in cm"
    
    breadth=int(input("breadth:"))
    var="breadth in cm"
    
    Perimeterformula=height1+height2+breadth
    print("Perimeter of the triangle is:", Perimeterformula)
    return Perimeterformula


# In[12]:


traingle()


# In[ ]:




