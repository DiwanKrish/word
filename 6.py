import cv2
gray=cv2.imread("E:/exam/col.jpg",cv2.IMREAD_GRAYSCALE)
blurred=cv2.GaussianBlur(gray,(5,5),1.4)
edges=cv2.Canny(blurred,threshold1=50,threshold2=150)
cv2.imshow("canny edge",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()