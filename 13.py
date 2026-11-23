import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("E:/exam/col.jpg",0)
noisy=np.clip(img+ np.random.normal(0,20,img.shape),0,255).astype(np.uint8)
sizes=[(3,1),(5,2),(9,3),(15,4)]
plt.figure(figsize=(14,4))
plt.subplot(1,5,1)
plt.imshow(noisy,cmap='gray')
for i,(k,s) in enumerate(sizes):
    out=cv2.GaussianBlur(noisy, (k,k), s)
    plt.subplot(1,5,i+2)
    plt.imshow(out,cmap='gray')
    plt.title(str(k)+"x"+str(k))
plt.show()
    