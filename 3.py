import cv2
color_img=cv2.imread("E:/exam/col.jpg")
gray_img=cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
