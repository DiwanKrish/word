import cv2 as cv
import sys
img=cv.imread("E:/exam/old2.jpg")
if img is None:
    print("image not found")
    sys.exit(1)
cv.imshow("original image",img)
cv.waitKey(0)
cv.destroyAllWindows()
#if img is not None:
 #   cv.imwrite("E:/exam/rgb1.tiff",img)
  #  cv.imwrite("E:/exam/rgb2.webp",img)