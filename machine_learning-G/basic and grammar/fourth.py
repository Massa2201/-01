#!/usr/bin/env python
# coding: utf-8

# In[2]:


three_item_list = [1, 0, 1]
three_item_matrix = [three_item_list, three_item_list, three_item_list]
print(three_item_matrix)


# In[4]:


three_item_list = [1, 0, 1]
three_item_matrix = [three_item_list, three_item_list, three_item_list]
three_three_matrix = [three_item_matrix, three_item_matrix, three_item_matrix]
print(three_three_matrix)


# In[6]:


print(three_item_list)


# In[8]:


string_list = ['二','三','四']
three_item_matrix = [string_list, string_list, string_list]
print(three_item_matrix)


# In[13]:


string_list = ['ゼロ番目の文字列','イチ番目の文字列','ニ番目の文字列']
print(string_list[0])
print(string_list[1])
print(string_list[2])


# In[15]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(train_data[0:6])
print(train_data[0:-6])
print(train_data[:3])
print(train_data[8:])
print(train_data[0:100])


# In[17]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_data[0] = 999
print(train_data)


# In[19]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_data = train_data  + [11]
print(train_data)
train_data += [12]
print(train_data)
train_data.append(13)
print(train_data)


# In[21]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del train_data[0]
print(train_data)


# In[23]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_data_new = train_data
train_data_copy = train_data[:]
# train_data_newは影響を受ける
del train_data[0]
print(train_data_new)
print(train_data_copy)


# In[25]:


# 条件分岐

# flowerは花を入れる変数です。
flower = 'rose'
print(flower == 'rose')

if flower == 'rose':
    print('花は薔薇ですね')


# In[27]:


flower = 'tulip'
print(flower == 'rose')

if flower == 'rose':
  print('花は薔薇ですね')
else:
  print('花は薔薇ではないですね')


# In[29]:


flower = 'tulip'
print(flower == 'rose')

if flower == 'rose':
  print('花は薔薇ですね')
elif flower == 'tulip':
  print('花はチューリップですね')
else:
  print('花は薔薇でもチューリップでもないですね。')


# In[31]:


A = True
B = True

print(A and B)
if A and B:
  print('AとBが同時にTrueの場合')


# In[33]:


A = True
B = False

print(A or B)
if A or B:
  print('AかBがどっちかTrueの場合')

A = False
B = True

print(A or B)
if A or B:
  print('AかBがどっちかTrueの場合')


# In[37]:


# for文

languages = {'English': '英語', 'French': 'フランス語', 'Japanes': '日本語'}
for one_language in languages:
  print(one_language)


# In[39]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for one_data in train_data:
  print(one_data)


# In[41]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, one_data in enumerate(train_data):
  print('index:' + str(index))
  print(one_data)


# In[42]:


for number in range(0, 6):
  print(number)


# In[44]:


for number in range(0, 110, 10):
  print(number)


# In[46]:


train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in range(0, len(train_data)):
  print(train_data[num])


# In[48]:


number_of_epoch = 10
for epoch in range(number_of_epoch):
  print('学習しました:' + str(epoch) + '回')


# In[50]:


# while文

counter = 0
while counter < 7:
  print(train_data[counter])
  counter += 1


# In[52]:


languages = {'English': '英語', 'French': 'フランス語', 'Japanese': '日本語'}
for key, value in languages.items():
  print(key)
  print(value)
  print('-------')


# In[55]:


# 関数
languages = {'English': '英語', 'French': 'フランス語', 'Japanese': '日本語'}
# 関数の定義
def printLanguageTranslation(language_list):
  for key, value in language_list.items():
    print(key)
    print(value)
    print('--------')

# 関数を使う
printLanguageTranslation(languages)


# In[57]:


import numpy as np

print(np.__version__)


# In[ ]:




