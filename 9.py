import cv2
img=cv2.imread("E:/exam/col.jpg")
resize=cv2.resize(
    img, None,fx=5,fy=5,interpolation=cv2.INTER_NEAREST
    )
cv2.imshow("resize",img)
cv2.waitKey(0)
cv2.destroyAllWindows()