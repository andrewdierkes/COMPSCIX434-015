#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import pathlib
import glob


# In[27]:


#Question 1: Write a regular expression to match words that begin with at least two uppercase letters or two lowercase letters. For example, it will match UCX, AM, PM or hello, but reject University or Programming. 

pattern_match = re.compile(r'\b[a-z]{2,}\b|\b[A-Z]{2,}')
string_test = 'THIS is a Test STRING, BUT it Should only give CAPITAL or Lowercase IF they REPEAT It More THAN twice.'

case_sensitive = pattern_match.findall(string_test)
print(case_sensitive)


# In[3]:


# this is a comment
print("hello world") # this is another comment


# In[4]:


#Question 2: Write a program that reads a Python file and removes any comments that it may have.  Comments include anything that starts with #.

_path = pathlib.Path.cwd()

for _filepath in _path.iterdir():

    if _filepath.stem != 'comment':
        continue
    
    if _filepath.stem == 'comment':
        with open(_filepath) as file:
            data = file.read()
            #before
            print(data)
            
            comment_remover = re.compile(r'#.*\n')
            remove_comment = comment_remover.sub('',data)
            #after
            print(remove_comment)
            
            
            


# In[30]:


#this is my email file I used for problem 3

_1 = 'andy.dierkes@yahoo.com'
_2 = 'andi-dierkes_112@gmail.com'
_3 = 'the_st@hey.o'
_4 = '1121a@yahoooo.c1mm'
_5 = 'this sky is calling'
_6 = 'thie_t@ya-h.org'


# In[31]:


#Question 3: Write a program that reads a file and prints out all of the valid email addresses. A valid email address has a pattern of prefix@domain.
# Prefix can contain letters, numbers, underscore, dots and dashes.
# Domain can also contain letters, numbers, dashes. However, the last portion must contain a dot followed by at least two characters (example: .com, .cc, .edu, etc…)

for _filepath in _path.iterdir():
    if _filepath.stem != 'email':
        continue
        
    if _filepath.stem == 'email':
        with open(_filepath) as file:
            data = file.read()

            email_pattern = re.compile(r'[^_\'][a-z,0-9].*@[a-z,0-9,-].*\.[a-z,0-9]{2,}')
            email_finder = email_pattern.findall(data)
            print(email_finder)
            
            
            #{2,} = match 2 or more occurences of last


# In[39]:


#Question 4: Write a regular expression that will accept following phone numbers and reformat them into a standard format.

numbers = ['(415)555-1212',
'510-778-1234',
'408 555 4321',
'650.444.1213']

#REGEX to omit the ( initially
phone_num_finder = re.compile(r'[0-9].*')

#REGEX to match the spacers
pattern_finder = re.compile(r'[),-,\.,\s]')

#make a new list of phone numbers with no ( in the front of 415
phone_num_list = [phone_num_finder.findall(var1) for var1 in numbers]
phone_num_list_final = [var for small_list in phone_num_list for var in small_list]

#sub '-' for the spacers defined 
connection_replacer = [pattern_finder.sub('-', var) for var in phone_num_list_final]

print(connection_replacer)

