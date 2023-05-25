#!/usr/bin/env python
# coding: utf-8

# In[114]:


prac_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

new_values = []
new_keys = []

for key in prac_dict.keys():
    new_values.append(key)
    
for value in prac_dict.values():
    new_keys.append(value)

print(dict(zip(new_keys, new_values)))
    


# In[115]:


string = 'Somebody once told me the world was macaroni, I took a bite just to see. It tasted kind of funky, so I spit it at a monkey'
words = string.split()
word_count = {word: (words.count(word)) for word in words}
print(word_count)


# In[116]:


_dict_1 = {'a': 1, 'b': 2, 'c': 3}
_dict_2 = {'a': 10, 'c': 30, 'f': 50}
_dict_final = {}

_dict_final.update(_dict_1)
_dict_final.update(_dict_2)

for _key1, _val1 in _dict_1.items():
    for _key2, _val2 in _dict_2.items():
        if _key1 == _key2:
            _dict_final[_key1] = _val1 + _val2

print(_dict_final)


# In[117]:


big_list= [['C++', 'Java', 'Python', 'Swift'],
['San Francisco','Berkeley','Oakland'],
['Apple', 'Banana', 'Cherry', 'Dragonfruit', 'Grape']]

final_list = [[len(var) for var in small_list] for small_list in big_list]

print(final_list)


# In[118]:


import numpy as np

score = [{'name': 'Lisa', 'score': 93},
{'name': 'Jeff', 'score': 85},
{'name': 'Elon', 'score': 89},
{'name': 'Satya', 'score': 90},
{'name': 'Tim', 'score': 82}]

#create list of only score values for each small dictionary
score_list = [small_dict['score'] for small_dict in score]

#create list of names for each small dictionary
name_list = [small_dict['name'] for small_dict in score]

#zip name, score into key:value for new dictionary
name_score_dict = dict((zip(name_list, score_list)))

#take average of all scores
AVG_Score = np.average(score_list)
print(AVG_Score)

#create function to return unknown key for known value if inputted val is a dictionary value
def name_max_score(val):
    for key, value in name_score_dict.items():
        if val == value:
            return key

#prints key of associate max value in name_score_dict
print(name_max_score(max(name_score_dict.values())))

