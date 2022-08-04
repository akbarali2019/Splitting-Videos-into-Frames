#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import glob, os


# In[53]:


#Path
source="C:/Users/admin/Desktop/datasetB/basevids2022 (49).mp4"
Destination="C:/Users/admin/Desktop/vidsB/vids525/vids525_"
dsize = (640, 640)


# In[54]:


#video
currentFrame = 0
cap = cv2.VideoCapture(source)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = Destination + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    

    # resize image
    output = cv2.resize(frame, dsize)

    cv2.imwrite(name, output)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# In[5]:


'''
image_path = 'C:/Users/admin/Desktop/videos/images/a (1).jpg'
filename = 'C:/Users/admin/Desktop/videos/imgs/img_10.jpg'
img = cv2.imread(image_path)
output = cv2.resize(img, dsize)
cv2.imwrite(filename, output)
'''


# In[21]:


counter = 1
file_dir = 'C:/Users/admin/Desktop/videos/imgs/'
data_dir = 'C:/Users/admin/Desktop/videos/images'
for pathAndFilename in glob.iglob(os.path.join(data_dir, "*.jpg")):
    img = cv2.imread(pathAndFilename)
    output = cv2.resize(img, dsize)
    filename = (file_dir + 'img_' + str(counter) + '.jpg')
    cv2.imwrite(filename, output)
    print ('Creating...' + filename)
    counter = counter + 1


# In[ ]:




