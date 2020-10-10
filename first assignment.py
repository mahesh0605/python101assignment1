#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("largest element in the list is :", max(lst)), 


# In[2]:


lst=[16,48,15,67,12,45]
lst.sort(reverse=True)
print("second largest number of the list is:{}".format(lst[1]))


# In[3]:


lst_1=[112,89,12,34,89,56]
lst_2=[67,34,78,88,1,54]
lst_merged=lst_1+lst_2
lst_merged.sort()
lst_merged


# In[4]:


mylist=[69,34,8,66,67]
size=len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print("list after swapping:",mylist)


# In[ ]:




