#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = [1,5,30,50,150]
var = 0

while var == 0:
    print(max(num))
    var += 1    


# In[3]:


num = [0.5,5,30,50,100]

for var in num:
    print(min(num))
    break


# In[4]:


running_total = []

while True:
    user_input = input('I am an adding machine, give me a number!')

    if user_input == "quit":
        break
    
    if user_input.isdigit() == True:
        running_total.append(int(user_input))
        
        print(running_total)
        print(sum(running_total))
        
        continue
    
    if user_input.isalpha() == True:
        print(f'Error, you\'ve entered {user_input}, which is not a number.')
    
    
print('Out of Loop')



# In[31]:


a = list(range(121))
b = list(range(121))
combo = []

for a_num in a:
    for b_num in b:
        if a_num*b_num == 120:
            combo.append(str(f'{a_num}*{b_num}'))
combo.sort()
print(combo)
            
#print(f'{a_num}*{b_num}'))


# In[5]:


rows = input('How many rows do you want?')
digit = 0

for row in range(1, int(rows)+1): 
    for col in range(1, int(row)+1):
        print(digit+1, end = " ")
        digit = digit + 1
    print()
print(f'You\'ve entered {rows} rows')


# In[7]:


mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
newlist = []

for var in mylist:
    if var.isalpha() is True:
        newlist.append(var)
print(newlist)


# In[6]:


num_list = [60, 100, 200, 500, 3000, 35, 450, 560, 21]

new_num_list = [num * 0.0254 for num in num_list]
print(new_num_list)

