#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
vid_path = 'C:\\Users\\admin\\Desktop\\basevids2022_1\\imagesnew\\'
capture = cv2.VideoCapture(vid_path)


#video_width = int(capture.get(3))
#video_height = int(capture.get(4))
fps = int(capture.get(cv2.CAP_PROP_FPS))


#for cropping make unsharp
#row = int(video_width*0.2)
#col = int(video_height*0.1)
#row_end = int(video_width-row)
#col_end = int(video_height-col)
dim = (512,512)


filepath = 'C:/Users/admin/Desktop/vidsmine/'
count = 0

while True:

    _, frame = capture.read()
    if frame is None:
        print("End of stream")
        break
        
    filename = (filepath+str(count)+'.jpg')  
    
    #resized = cv2.resize(frame[col:col_end, row:row_end], dim, interpolation = cv2.INTER_AREA) #for cropping also make unsharp
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(filename, resized)    
    cv2.imshow("output", resized)
    
    count = count + 1
    
    if cv2.waitKey(1) > -1:
        print("finished by user")
        break

capture.release()

cv2.destroyAllWindows() 


# In[ ]:


import cv2
 
img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[142]:


import cv2
import glob
import os

inputFolder = 'C:\\Users\\admin\\Desktop\\vidsmine\\imagesnew'
os.mkdir('Resized Folder2')

i=0

for img in glob.glob(inputFolder + "/*.jpeg"):
    image = cv2.imread(img)
    imgResized = cv2.resize(image, (512, 512))
    cv2.imwrite("Resized Folder2/image%04i.jpeg" %i, imgResized)

    i +=1
    #cv2.imshow('image', imgResized)
    #cv2.waitKey(30)

cv2.destroyAllWindows()


# In[ ]:




