import cv2
import numpy as np
import matplotlib.pyplot as plt
def add_noise(img,prob=0.02):
    noisy=img.copy()
    rnd=np.random.rand(*img.shape[:2])
    noisy[rnd<prob]=255
    noisy[rnd>1-prob]=0
    return noisy
img=cv2.imread("E:/exam/old2.jpg")
noisy=add_noise(img)
avg=cv2.blur(noisy, (5,5))
gaussian=cv2.GaussianBlur(noisy, (5,5), 1)
median=cv2.medianBlur(noisy, 5)
image=[img,noisy,avg,gaussian,median]
title=["original","noisy","average","gaussian","median"]
plt.figure(figsize=(8,2))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(image[i],cmap="gray")
    plt.title(title[i])
    plt.axis("off")
plt.tight_layout()
plt.show()