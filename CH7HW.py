#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Rectangle():
    def __init__(self, width, height, name='unnamed', x=0, y=0):
        self.width = width
        self.height = height
        self.name = name
        self.area = self.width*self.height
        self.x = x
        self.y = y
    
    @property
    def tester(self):
        return f'Name of rectangle: {self.name}, x = {self.x}, y = {self.y}, height = {self.height}, area = {self.area}' 
    
    def __str__(self):
        return f'Name of rectangle: {self.name}, x = {self.x}, y = {self.y}, height = {self.height}, area = {self.area}' 
    
    @tester.setter
    def tester(self, val_input):
        print('inside setter')
        self.x = val_input[0]
        self.y = val_input[1]
        
        


# In[2]:


large = Rectangle(4,5, 'large_rectangle', 10, 12)


# In[3]:


large.__str__()


# In[4]:


large.tester
large.tester = [20, 21]
large.x
large.y


# In[6]:


class Vehicle():
    
    def __init__(self, name, speed, odometer=0):
        self.name = name
        self.speed = speed
        self.odometer = odometer
    
    def drive(self, minutes):
        self.minutes = minutes
        self.miles = self.speed * (self.minutes/60)
        
        self.odometer += self.miles
        
        
        


# In[9]:


car1 = Vehicle('mustang', 70)
car1.drive(100)


# In[10]:


print(car1.minutes)
print(car1.speed)
print(car1.miles)
print(car1.odometer)


# In[11]:


car2 = Vehicle('tarus', 40)
car2.drive(2000)


# In[12]:


print(car2.minutes)
print(car2.speed)
print(car2.miles)
print(car2.odometer)


# In[275]:





# In[25]:


class Special_rectangle(Rectangle):

    def __add__(self, width_rect2):
        self.width = self.width + width_rect2.width
        return self.width
    
    def __eq__(self, ar2):
        return self.area == ar2.area
    
    def __str__(self):
        return f'name = {self.name}, x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}, area = {self.area}' 
    


# In[31]:


r1 = Special_rectangle(30, 20, 'uno')
r2 = Special_rectangle(50, 20, 'dos')
r3 = r1+r2
print(r3)


# In[34]:


print(r1 == r2)
print(r2.__str__())


# In[29]:


class Vehicle():
    def __init__(self, size='none', wheels=0, color='none', gas='none'):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas
        
    def __add__(self, vech_2):
        self.gas = self.gas + vech_2.gas
        return self.gas
    
    def __eq__(self, vech_2):
        return self.wheels == vech_2.wheels
    
class Car(Vehicle):
    def __init__(self, size = 'small', wheels=4, terrain='concrete', gas=45):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas

class Truck(Vehicle):
    def __init__(self, size = 'large', wheels=4, terrain='off-road', gas=120):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas

class Boat(Vehicle):
    def __init__(self, size='small', wheels=0, terrain='water', gas=45):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas

class Scooter(Vehicle):
    def __init__(self, size='petite', wheels=2, terrain='single_track', gas=0):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas
        
class Motorcycle(Vehicle):
    def __init__(self, size='petite', wheels=2, terrain='concrete', gas=20):
        self.size = size
        self.wheels = wheels
        self.terrain = terrain
        self.gas = gas


# In[30]:


car1 = Car()
truck1 = Truck()
scooter1 = Scooter()
scooter2 = Scooter('petite', 2, 'concrete', gas=45)

#using __add__ method
scooter_sum = scooter2.gas + scooter1.gas
print(scooter2.gas, scooter1.gas)

print(scooter_sum)

#using __eq__ method
print(car1.gas == truck1.gas)
print(car1.wheels == truck1.wheels)


# In[ ]:




