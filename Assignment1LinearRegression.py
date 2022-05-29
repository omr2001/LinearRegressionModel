#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import metrics 


# In[2]:


Data=pd.read_csv('assignment1_dataset.csv')
print(Data.describe())


# In[3]:


# First Trial
X=Data['house age']
Y=Data['house price of unit area']
print(X.shape)


# In[4]:


plt.scatter(X,Y)
plt.xlabel('house age',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.show()


# In[5]:


L=0.001
epochs=20000
a=0
b=0
n=float(len(X))


# In[6]:


for i in range(epochs):
    Ypred=a*X+b
    da=(-1/n)*sum((Y-Ypred)*X)
    a = a- L*da
    db=(-1/n)*sum((Y-Ypred))
    b= b- L*db


# In[7]:


Prediction=a*X+b
plt.scatter(X,Y)
plt.xlabel('house age',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.plot(X,Prediction,color='red',linewidth=3)
plt.show()
print('The Mean Square Error',metrics.mean_squared_error(Y,Prediction))
# The End of The First Trial


# In[8]:


#Second Trial


# In[9]:


X=Data['distance to the nearest MRT station']
Y=Data['house price of unit area']
print(X.shape)


# In[10]:


plt.scatter(X,Y)
plt.xlabel('distance to the nearest MRT station',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.show()


# In[11]:


L=0.0000001
epochs=200000
a=0
b=0
n=float(len(X))


# In[12]:


for i in range(epochs):
    Ypred=a*X+b
    da=(-1/n)*sum((Y-Ypred)*X)
    a = a- L*da
    db=(-1/n)*sum((Y-Ypred))
    b= b- L*db


# In[13]:


Prediction=a*X+b
plt.scatter(X,Y)
plt.xlabel('distance to the nearest MRT station',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.plot(X,Prediction,color='red',linewidth=3)
plt.show()
print('The Mean Square Error',metrics.mean_squared_error(Y,Prediction))
#End of The Second Trial


# In[14]:


#Third Trial 
X=Data['number of convenience stores']
Y=Data['house price of unit area']
print(X.shape)


# In[15]:


plt.scatter(X,Y)
plt.xlabel('number of convenience stores',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.show()


# In[16]:


L=0.001
epochs=10000
a=0
b=0
n=float(len(X))


# In[17]:


for i in range(epochs):
    Ypred=a*X+b
    da=(-1/n)*sum((Y-Ypred)*X)
    a = a- L*da
    db=(-1/n)*sum((Y-Ypred))
    b= b- L*db


# In[18]:


Prediction=a*X+b
plt.scatter(X,Y)
plt.xlabel('number of convenience stores',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.plot(X,Prediction,color='red',linewidth=3)
plt.show()
print('The Mean Square Error',metrics.mean_squared_error(Y,Prediction))
#End of The Third Trial


# In[19]:


#Fourth Trial 
X=Data['latitude']
Y=Data['house price of unit area']
print(X.shape)


# In[20]:


plt.scatter(X,Y)
plt.xlabel('latitude',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.show()


# In[21]:


L=0.001
epochs=1000
a=0
b=0
n=float(len(X))


# In[22]:


for i in range(epochs):
    Ypred=a*X+b
    da=(-1/n)*sum((Y-Ypred)*X)
    a = a- L*da
    db=(-1/n)*sum((Y-Ypred))
    b= b- L*db


# In[23]:


Prediction=a*X+b
plt.scatter(X,Y)
plt.xlabel('latitude',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.plot(X,Prediction,color='red',linewidth=3)
plt.show()
print('The Mean Square Error',metrics.mean_squared_error(Y,Prediction))
#End of The Fourth Trial


# In[24]:


#Fifth Trial 
X=Data['longitude']
Y=Data['house price of unit area']
print(X.shape)


# In[25]:


plt.scatter(X,Y)
plt.xlabel('longitude',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.show()


# In[56]:


L=0.0001
epochs=400
a=0
b=0
n=float(len(X))


# In[57]:


for i in range(epochs):
    Ypred=a*X+b
    da=(-1/n)*sum((Y-Ypred)*X)
    a = a- L*da
    db=(-1/n)*sum((Y-Ypred))
    b= b- L*db


# In[58]:


Prediction=a*X+b
plt.scatter(X,Y)
plt.xlabel('longitude',fontsize=20)
plt.ylabel('house price of unit area',fontsize=20)
plt.plot(X,Prediction,color='red',linewidth=3)
plt.show()
print('The Mean Square Error',metrics.mean_squared_error(Y,Prediction))
#End of The Fifth Trial


# In[ ]:





# In[ ]:




