#!/usr/bin/env python
# coding: utf-8

# In[1]:


# matplotlibの宣言をする
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


plt.plot([1, 2, 3, 4])
plt.show()


# In[3]:


plt.plot([4, 3, 2, 1])
plt.show()


# In[4]:


# 配列を作成し，折れ線を出力
x = np.array([1, 2, 3, 4, 5])
y = np.array([100, 200, 300, 400, 500])
# 描画
plt.plot(x, y)
# グラフ表示
plt.show()


# In[7]:


x = np.arange(5)
y = np.arange(start=100, stop=600, step=100)
print("y=", y)
plt.plot(x, y)
plt.show()


# In[11]:


volume = 30
x = np.arange(volume)
y = [x_i + np.random.randn(1) for x_i in x]
a, b = np.polyfit(x, y, 1)
_ = plt.plot(x, y, 'o', np.arange(volume), a * np.arange(volume) + b, '-')


# In[12]:


x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.show()


# In[13]:


plt.plot(x, np.cos(x))
plt.show()


# In[14]:


plt.plot(x, np.arctan(x))
plt.show()


# In[17]:


plt.plot(x, np.arctan(x))
# title
plt.title("Title for the graph")
plt.xlabel("Label for x-axis")
plt.ylabel("Label for y-axis")
plt.show()


# In[20]:


plt.plot(x, np.sin(x))
plt.title("title01")
plt.xlabel("x-line")
plt.ylabel("y-line")
plt.grid(False)
plt.show()


# In[21]:


x = np.linspace(0, 2 * np.pi)
plt.plot(x, np.sin(x))

plt.title("title")
positions = [0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2]
labels = ["0", "90", "180", "270", "360"]
plt.xticks(positions, labels)
plt.show()


# In[25]:


plt.figure(figsize = (4, 4))
x = np.linspace(0, 2 * np.pi)
plt.plot(x, np.sin(x))
plt.show()


# In[26]:


# 散布図
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
plt.show()


# In[27]:


plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2", edgecolors="red")
plt.show()


# In[28]:


plt.scatter(x, y, s=300, c=y, cmap="Greens")
plt.title("aaa")
plt.grid(True)


# In[30]:


import matplotlib.pyplot as plt
plt.subplot(211)
plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2", edgecolors="red")
plt.subplot(212)
plt.scatter(x, y, s=300, c=y, cmap="Greens")
plt.show()


# In[31]:


import matplotlib.pyplot as plt
plt.subplot(121)
plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2", edgecolors="blue")
plt.subplot(122)
plt.scatter(x, y, s=300, c=y, cmap="Greens")
plt.show()


# In[33]:


plt.subplot(221)
plt.scatter(x, y, s=600, c="white", alpha=0.5, linewidths="2", edgecolors="yellow")
plt.subplot(222)
plt.scatter(x, y, s=300, c=y, cmap="Greens")
plt.subplot(223)
plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2", edgecolors="red")
plt.subplot(224)
plt.scatter(x, y, s=300, c=y, cmap="Blues")
plt.show()


# In[36]:


from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)
random_x = np.random.randn(100)
random_y = np.random.randn(100)
random_z = np.random.randn(100)

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(1, 1, 1, projection="3d")
x = np.ravel(random_x)
y = np.ravel(random_y)
z = np.ravel(random_z)

ax.scatter3D(x, y, z)
plt.show()


# In[40]:


np.random.seed(0)

random_x = np.random.randn(100)
random_y = np.random.randn(100)
random_z = np.random.randn(100)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection="3d")
x = np.ravel(random_x)
y = np.ravel(random_y)
z = np.ravel(random_z)
c = "r"
m = "^"
s = 300,

ax.scatter3D(x, y, z, s=s, c=c, marker=m)
plt.show()


# In[ ]:




