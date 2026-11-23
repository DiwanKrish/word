import cv2

gray = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image at input.jpg")

T = 127
_, global_seg = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

cv2.imshow(f"Global Threshold (T={T})", global_seg)
cv2.waitKey(0)
cv2.destroyAllWindows()