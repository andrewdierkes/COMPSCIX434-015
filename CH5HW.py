#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import numpy as np 
import pathlib

try:
    with open('gettysburg.txt', 'rt') as file:
        data= file.read()
    
        #create search parameter & search for words & new lines in data
        try:
            word = re.compile(r'\w+')
            new_line = re.compile(r'\n')
            list_word = re.findall(word, data)
            list_line = re.findall(new_line, data)
    
        except:
            print('There is an issue in regex')
    
        print(f'Number of lines: {len(list_line)}')
        print(f'Number of words: {len(list_word)}')
    
            #find average length for words in data
        length_word = [len(word) for word in list_word]
        average_word_length = np.average(length_word)
        print(f'Average length of words: {round(average_word_length, 2)}')
except OSError:
    print('file does not exist in path')



# In[3]:


try:
    with open('words.txt', 'rt') as file:
        for count, line in enumerate(file):
            pass 
        print(f'Total number of lines in words.txt: {count+1}')
except OSError:
    print('file does not exist in path')


# In[4]:


_5_word_list = []
try:
    with open('words.txt', 'rt') as file:
        for line in file.readlines():
            
            word5 = re.compile(r'\b(\w{5})\b')
            
            _5_word_list += re.findall(word5, line)

    string5 = '\n'.join(_5_word_list)
    
    with open('_5_letter_word.txt', 'wt') as file:
        file.write(string5)

         
except OSError:
    print('file does not exist in path')


# In[5]:


try:
    with open('_5_letter_word.txt', 'rt') as file:
        for count, line in enumerate(file):
            pass
    print(f'In the new file, there are {count} 5-letter words')
    
except OSError:
    print(f'file does not exist in path {pathlib.Path.cwd()}')


# In[6]:


import csv

try:
    with open('sf_buildings.csv') as file:
        rows = list(csv.reader(file))
    
        #delete use column
        for row in rows:
            del row[3]
    
        #convert height to m
        for row in rows[1:]:
            row[1] = round(float(row[1])*0.3048, 3)
        
    metadata = rows[0]
    data = rows[1:]

    with open('sf_buildings_updated.csv', 'w') as file_2:
        new_csv = csv.writer(file_2)
        new_csv.writerow(metadata)
        new_csv.writerows(data)

except OSError:
    print('file does not exist in path')


# In[7]:


import json

cities = []
city_num_list = []

try:
    with open('us_states_and_cities.json', 'r') as file_json:
        data = json.load(file_json)
    
        for state in data:
        
            #finding most cities and the associated state
            number_list = [len(state) for state in data]
            state_list = [state for state in data]
        
            big = max(number_list)
        
            indexer= number_list.index(big)

        #extract from dictionary and add values to a list of lists
        for city_list in data.values():
            cities.append(city_list)
        
            def delist(args):
                delist = [var for small_list in args for var in small_list]
                return(delist)
        
        cities_final = delist(cities)
    

        city_count = {city: int(cities_final.count(city)) for city in cities_final} 
    
    #print(isinstance(var in city_count.values(), int))
    
        for city_num in city_count.values():
            city_num_list.append(city_num)
    
        repeat_city = max(city_num_list)
          
        def get_key(arg, dictionary_name):
            for key, value in dictionary_name.items():
                if int(value) == int(arg):
                    return key
                    return value
        
    print(f'The most cities in this JSON are found in the {state_list[indexer]} with {big} cities')
    print(f'{get_key(repeat_city, city_count)} is the most repeated city name; across {repeat_city} states')  

except OSError:
    print('file does not exist in path')


# In[ ]:




