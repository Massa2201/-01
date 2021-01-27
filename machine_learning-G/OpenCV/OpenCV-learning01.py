#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install opencv-python')


# In[7]:


import cv2
print(cv2.__version__)


# In[8]:


import cv2
import matplotlib.pyplot as plt


# In[ ]:


# PCから画像をuploadする
from google.colab import files
uploaded = files.upload()


# In[3]:


ls


# In[9]:


img_bgr = cv2.imread('test.jpg')
print(img_bgr)


# In[10]:


plt.imshow(img_bgr)
plt.show()


# In[ ]:


import numpy as np
x = np.array(img_bgr)
print(x.shape)


# In[11]:


img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()


# In[ ]:


img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
plt.imshow(img_hsv)
plt.show()


# In[ ]:


plt.imshow(img_rgb)


# In[ ]:


plt.show()


# In[ ]:


img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(img_gray)
plt.show()


# In[ ]:


cv2.imwrite('ff10画像.jpeg', img_gray)


# In[ ]:


ls


# In[ ]:


img_bgr = cv2.imread('ff10画像.jpeg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
size = img_rgb.shape
print(size)


# In[ ]:


new_img = img_rgb[:size[0] // 2, : size[1] // 2]
print(new_img.shape)
plt.imshow(new_img)
plt.show()


# In[ ]:


new_img = img_rgb[size[0] // 2:,  size[1] // 2:]
print(new_img.shape)
plt.imshow(new_img)
plt.show()


# In[ ]:


new_img = img_rgb[:size[0] // 3,  size[1] // 3:]
print(new_img.shape)
plt.imshow(new_img)
plt.show()


# In[ ]:


img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

size = img_rgb.shape
print(size)
resized_img = cv2.resize(img_rgb, (img_rgb.shape[1] * 2, img_rgb.shape[0] * 2))
print(resized_img.shape)
plt.imshow(resized_img)
plt.show()


# In[ ]:


resized_img = cv2.resize(img_rgb,(img_rgb.shape[1] // 4, img_rgb.shape[0] // 4))
print(resized_img.shape)
plt.imshow(resized_img)
plt.show()


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread("ff10画像.jpeg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# 画像の中心，45度，1倍
mat = cv2.getRotationMatrix2D(tuple(np.array(img_rgb.shape[:2]) / 2), 45, 1.0)

result_img = cv2.warpAffine(img_rgb, mat, img_rgb.shape[:2])

plt.imshow(result_img)
plt.show()


# In[ ]:


mat = cv2.getRotationMatrix2D(tuple(np.array(img_rgb.shape[:2]) / 2), 135, 0.5)

result_img = cv2.warpAffine(img_rgb, mat, img_rgb.shape[:2])

plt.imshow(result_img)
plt.show()


# In[1]:


from google.colab import files
uploaded = files.upload()


# In[2]:


img_bgr = cv2.imread("test.jpg")
result_img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)

plt.imshow(result_img)
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

retval, result_img = cv2.threshold(img_rgb, 95, 128, cv2.THRESH_TOZERO)
plt.imshow(result_img)
plt.show()


# In[ ]:


retval, result_img = cv2.threshold(img_rgb, 100, 255, cv2.THRESH_BINARY)

plt.imshow(result_img)
plt.show()


# In[ ]:


result_img = cv2.GaussianBlur(img_rgb, (15, 15), 0)

plt.imshow(result_img)
plt.show()


# In[ ]:


result_img = cv2.fastNlMeansDenoisingColored(img_rgb)

plt.imshow(result_img)
plt.show()


# In[14]:


import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread("test.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

filt = np.array([[0, 1, 0],
                 [1, 0, 1],
                 [0, 1, 0]], np.uint8)

result_img = cv2.dilate(img_rgb, filt)

plt.imshow(result_img)
plt.show()


# In[15]:


filt = np.array([[0, 1, 0],
                 [1, 0, 1],
                 [0, 1, 0]], np.uint8)

result_img = cv2.erode(img_rgb, filt)

plt.imshow(result_img)
plt.show()


# In[16]:


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
retval, thresh = cv2.threshold(img_gray, 88, 255, 0)
# img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result_img = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

plt.imshow(result_img)
plt.show()


# In[53]:


import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import cv2

def make_image(input_img):
  img_size = input_img.shape
  filter_one = np.ones((3, 3))

  mat1 = cv2.getRotationMatrix2D(tuple(np.array(input_img.shape[:2]) / 2), 23, 1)
  mat2 = cv2.getRotationMatrix2D(tuple(np.array(input_img.shape[:2]) / 2), 144, 0.8)

  fake_method_array = np.array([
    lambda image: cv2.warpAffine(image, mat1, image.shape[:2]),
    lambda image: cv2.warpAffine(image, mat2, image.shape[:2]),
    lambda image: cv2.threshold(image, 100, 255, cv2.THRESH_TOZERO)[1],
    lambda image: cv2.GaussianBlur(image, (5, 5), 0),
    lambda image: cv2.resize(cv2.resize(image, (img_size[1] // 5, img_size[0] // 5)), (img_size[1], img_size[0])),
    lambda image: cv2.erode(image, filter_one),
    lambda image: cv2.flip(image, 1),
  ])

  # 画像変数処理
  images = []

  for method in fake_method_array:
    faked_img = method(input_img)
    images.append(faked_img)

  return images

target_img = cv2.imread("test.jpg")

# 水増しをする
good_images = make_image(target_img)

if not os.path.exists("good_images"):
  os.mkdir("good_images")

for number, img in enumerate(good_images):
  cv2.imwrite("good_images/" + str(number) + ".jpg", img)


# In[22]:


ls good_images


# In[67]:


import numpy as np
import cv2
import matplotlib.pyplot as plt

NUM_COLUMNS = 4

ROWS_COUNT = len(good_images) % NUM_COLUMNS

COLUMS_COUNT = NUM_COLUMNS

subfig = []
fig = plt.figure(figsize=(12, 9))

for i in range(1, len(good_images) + 1):
    subfig.append(fig.add_subplot(ROWS_COUNT, COLUMS_COUNT, i))

    img_bgr = cv2.imread("good_images/" + str(i - 1) + '.jpg')
  # img_bgr = cv2.imread("good_images/" + str(i - 1) + 'jpg')

    img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    subfig[i - 1].imshow(img_rgb)
    
fig.subplots_adjust(wspace=0.3, hspace=0.3)

plt.show()


# In[ ]:


pwd


# In[ ]:


cd content/


# In[ ]:


ls


# In[ ]:


ls


# In[ ]:




