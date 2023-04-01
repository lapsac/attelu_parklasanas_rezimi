#1. režīms: Burn/Color
#====================================
# algoritma funkcija attela apstradei:
# C = 1-((1-B)/A) 
#
#A-priekšplāna attēls
#B-fona attels
#C-rezultats
#====================================
import numpy as np
from numpy import asarray
import math
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
image_A = cv2.imread('koks.png') # bildes nolasisana
image_B = cv2.imread('kalni.png') # bildes nolasisana
im_rgb_A = cv2.cvtColor(image_A, cv2.COLOR_BGR2RGB)
im_rgb_B = cv2.cvtColor(image_B, cv2.COLOR_BGR2RGB)

resized_img_A = cv2.resize(im_rgb_A, (500,500))# pieskir atteliem izmerus x-500 px, y-500 px
resized_img_B = cv2.resize(im_rgb_B, (500,500))# pieskir atteliem izmerus x-500 px, y-500 px

cv2.imwrite('koks.png', resized_img_A)
cv2.imwrite('kalni.png', resized_img_B)
colorburn = 1-((1-im_rgb_A)/im_rgb_B) # matematiska funkcija color burn effektam

fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='b') # raksturo fona krasu grafikiem un izmeru raksturojuma krasu
ax1 = fig.add_subplot(1,3,1) #pozicija kreisa puse
ax1.title.set_text('input img 1') # nosaukums attelam kreisaja puse
ax1.imshow(im_rgb_A) # output
ax2 = fig.add_subplot(1,3,2) # pozicija vidus
ax2.title.set_text('input img 2') # nosaukums attelam vidu
ax2.imshow(im_rgb_B) # output
ax3 = fig.add_subplot(1,3,3) # pozicija laba puse
ax3.title.set_text('Color Burn') # nosaukums attelam labaja puse
ax3.imshow(colorburn) # output
