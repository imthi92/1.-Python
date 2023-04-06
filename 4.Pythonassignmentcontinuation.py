#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Create Function. percentage(). Subject1= 23Subject2= 45Subject3= 34Subject4= 23Subject5= 23Total :  148Percentage :  29.599999999999998


# In[ ]:





# In[15]:


def percentage():
    sub1=int(input("Subject1:"))
    print("Subject1:", sub1)
    variable="Subject1"

    sub2=int(input("Subject2:"))
    print("Subject2:", sub2)
    variable="Subject2"          
                 
    sub3=int(input("Subject3:"))
    print("Subject3", sub3)
    variable="Subject3"
                
    sub4=int(input("Subject4:"))
    print("Subject4", sub4)
    variable="Subject4"           
    
    sub5=int(input("Subject5:"))
    print("Subject5", sub5)
    variable="Subject5"   
    perc=(sub1+sub2+sub3+sub4+sub5)/5
    return perc


# In[16]:


percentage()


# In[ ]:





# In[ ]:


# Create Function. Elegible(). Your Gender:MaleYour Age:18NOT ELIGIBLE


# In[13]:


def Eligible():
    gendervalue=input("Your Gender")
    age=int(input("Your age"))
    if (gendervalue=="Male" and age>21):
            print ("ELIGIBLE")
            variabledeclaration="ELIGIBLE FOR MARRIAGE"
    elif(gendervalue==Female and age>18):
         print ("ELIGIBLE")
         variabledeclaration="ELIGIBLE FOR MARRIAGE"
    else:
            print ("NOT ELIGIBLE")
            variabledeclaration="NOT ELIGIBLE FOR MARRIAGE"
            return variabledeclaration


# In[14]:


Eligible()


# In[ ]:





# In[ ]:


# Create Function. triangle(). Height:3Breadth:4Area formula: (Height*Breadth)/2Area of Triangle:  6.0Height1:3Height2:4Breadth:45Perimeter formula: Height1+Height2+BreadthPerimeter of Triangle:  52


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




