import cv2
img=cv2.imread("E:/exam/col.jpg",cv2.IMREAD_GRAYSCALE)
blurred=cv2.GaussianBlur(img, (3,3), 0)
laplacian=cv2.Laplacian(blurred, cv2.CV_64F,ksize=3)
laplacian=cv2.convertScaleAbs(laplacian)
cv2.imshow("laplacian edges",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()