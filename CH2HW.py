#!/usr/bin/env python
# coding: utf-8

# In[11]:


s = "Programming Python"

print(s[0])
print(s[-6])
print(s[0:1])

print(s[-6:])
print(s[12:])


# In[12]:


code = "   I am    Programming    Python!       "
qik = code.replace('   ', '')
qik.rstrip()


# In[14]:


length = 5
width = 2.5
height = 2.73

print(f'The box has a length: {length}, width: {width} and height: {height}. The volume is:'+ str(((length) * (width) * (height))))


# In[15]:


num = [1, 2, 3, 4, 5, 6, 7, 8]
new_num = (num[1::2])
final_num = new_num + [10,12,14]

print(final_num)


# In[16]:


num = [1, 2, 3, 4, 5, 6, 7, 8]

#remove odds
for var in num:
    if var % 2 !=0:
        num.remove(var)

#add new numbers
new_num = [10,12,14]
num.extend(new_num)

print(num)


# In[9]:


t = ('anita', 0, 'brandon', 'chitra', 5, 7)

tup = (t[0].capitalize(), 0, t[2].capitalize(), t[3].capitalize(), 5, 7)
t = tup[0], tup[2], tup[3]
print(t)

