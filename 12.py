import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("E:/exam/col.jpg",0)
noisy=np.clip(img+ np.random.normal(0,20,img.shape),0,255).astype(np.uint8)
sizes=[3,5,9,15]
plt.figure(figsize=(14,4))
plt.subplot(1,5,1)
plt.imshow(noisy,cmap='gray')
plt.title("noisy")
for i,k in enumerate(sizes):
    out=cv2.blur(noisy, (k,k) )
    plt.subplot(1,5,i+2)
    plt.imshow(out,cmap='gray')
    plt.title(str(k)+"x"+str(k))
plt.show()