import cv2

gray = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image at input.jpg")

# Mean-based and Gaussian-weighted local thresholds
adap_mean = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=15,
    C=4,
)

adap_gauss = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=15,
    C=4,
)

cv2.imshow("Adaptive Mean", adap_mean)
cv2.imshow("Adaptive Gaussian", adap_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()