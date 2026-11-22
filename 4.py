import cv2
gray=cv2.imread("E:/exam/col.jpg",cv2.IMREAD_GRAYSCALE)
blur=cv2.GaussianBlur(gray, (5,5), 0)
otsu_thresh,segmented=cv2.threshold(
    blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU
    )
print(f"optimal otsu threshold :{otsu_thresh}")
cv2.imshow("otsu segmentation",segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()