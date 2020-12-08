#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

print('numpy のバージョンは：',np.__version__)


# In[4]:


a = np.array([1, 2, 3])
print('a=', a)


# In[6]:


a * 3


# In[8]:


a + 2


# In[10]:


b = np.array([1, 1, 4])
print('b=', b)


# In[12]:


a + b


# In[14]:


a - b


# In[15]:


a / b


# In[16]:


a * b


# In[17]:


np.dot(a, b)


# In[18]:


c =np.array([[1, 2], [3, 4]])
print("c=", c)
d =np.array([[3, 4], [1, 2]])
print("d=", d)


# In[19]:


np.dot(c, d)


# In[20]:


e = np.array([[1, 2, 3], [0.1, 0.2, 0.3], [7, 8, 9]])
print("e=", e)
f = np.array(([[0.1, 0.2, 0.3], [1, 2, 3], [7, 8, 9]]))
print('f=', f)


# In[23]:


np.dot(f, e)


# In[24]:


g = np.arange(9).reshape((3, 3))
print('g=',g)


# In[25]:


g = g.reshape((9, 1))
print(g)


# In[26]:


zeros = np.zeros((3, 4))
print('zeros=', zeros)


# In[27]:


h = np.ones((3, 3))
print('h=', h)


# In[29]:


p = np.empty((2, 3))
print('p=', p)


# In[30]:


k = np.matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print('k=', k)


# In[31]:


l = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print('l=', l)

m = np.dot(k, l)
print('m=', m)


# In[32]:


m.shape
print('m.shape', m.shape)


# In[39]:


g.shape
print('g.shape', g.shape)


# In[34]:


m.ndim
print('m.ndim', m.ndim)


# In[36]:


m.dtype.name
print('m.dtype.name', m.dtype.name)


# In[37]:


m.itemsize
print('m 配列内，各要素のbyte数：', m.itemsize)


# In[41]:


m.size
print('m 総要素数：', m.size)


# In[42]:


q  = np.arange(1000000).reshape(1000, 1000)
print('q=', q)


# In[43]:


x = np.arange(10)
print(x)


# In[44]:


x = np.arange(start=100, stop=600, step=100)
print(x)


# In[45]:


x_float = x.astype('float32')
print('x_float.dtype.name', x_float.dtype.name)
print(x_float)


# In[ ]:




