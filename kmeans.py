# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:28:06 2020

@author: Arpita
"""

import math 
from PIL import Image
from pylab import *
import matplotlib as plt
import scipy as sp
import random
import cv2
import os
import matplotlib.image as mpimg 
import matplotlib.patches as mpatches 
from matplotlib.colors import from_levels_and_colors


#################### Input ####################
## directory path
path="C:/..."
Image_list=[x,y,z.....,.]
k= 5 # number of clusters
#########################################


############## Create a 3D array by stacking images #############################

arr= np.array([np.array(Image.open(os.path.join(path,fname))) for fname in file])
print("Shape of the array:", arr.shape)


#################### Define initial centers ############################
h=arr.shape[1]
w=arr.shape[2]
centers=[[] for i in range(k)]
for i in range(k):
  x=random.randrange(h)
  y=random.randrange(w)
  for rep in range (len(file)):
     cent=arr[rep][x,y]
     centers[i].append(cent)

print("initial centers:", centers)


############ Function for Distance Calculation ###############
def calculatedistance(pixel, centroids):
    distance=[]
    minindex=0
    for c in centroids:
      sum=0
      sum=np. linalg. norm(np.array(pixel)-np.array(c)) #euclidean distance
      distance.append(sum)
      #for i in range(len(file)):
        #dis=(pixel[i]-c[i])**2
        #sum=sum+dis
              
    minindex=np.argmin(distance)
    clus[minindex].append(pixel)
    return minindex



#################### Function for New Center Calculation ###################
def calculateNewCenter(cen):
    #new_centers=[]
    n_mean=np.mean(cen, axis=0)
    #new_centers[k]=n_mean
    #new_centroids=np.concatenate(new_centers, axis=0)
    return (n_mean)


##########m Main function of K-means #########################
    
##if __name__ == "__main__":
oldcentroids= [[] for i in range(k)]
iterations=0
while not (np.array_equal(centers,oldcentroids)):
  global clus
  clus=[[] for i in range(k)]
  labels=np.zeros(arr[1].shape).astype('int')
  print(iterations+1)
  for x in range(h):
    for  y in range(w):
      print("running:", x,y)
      pixel_pt=[]
      for image in range(len(file)):
        pixel_pt.append(arr[image][x,y])
      labels[x,y]=calculatedistance(pixel_pt,centers)
  for c in range(len(clus)):
      oldcentroids[c] =centers[c]
      centers[c]=calculateNewCenter(clus[c])
      
else:
    print("Image has Coverged")      
    
    

##########################   Add color based on clusers    ##############################

#def plotcolmap(ar,f):
cmap, norm = from_levels_and_colors([0,1,2,3,4],['red','blue','green','yellow'])
plt.imshow(ar, cmap=cmap, norm=norm)  
plt.title('colormap_'+str(f)+'title)      
    
    