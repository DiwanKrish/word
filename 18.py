import cv2
import matplotlib.pyplot as plt

gray = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image at input.jpg")

blur = cv2.GaussianBlur(gray, (5, 5), 1.0)

# 1. Sobel (First-order directional gradient)
sx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.magnitude(sx, sy))

# 2. Laplacian (Second-order isotropic derivative)
laplacian = cv2.convertScaleAbs(cv2.Laplacian(blur, cv2.CV_64F, ksize=3))

# 3. Canny (Multi-stage non-maximum suppression + hysteresis)
canny = cv2.Canny(blur, 50, 150)

plt.figure(figsize=(14, 3.5))
for i, (t, im) in enumerate(
    [
        ("Original", gray),
        ("Sobel", sobel),
        ("Laplacian", laplacian),
        ("Canny", canny),
    ],
    1,
):
    plt.subplot(1, 4, i)
    plt.imshow(im, cmap="gray")
    plt.title(t)
    plt.axis("off")

plt.tight_layout()
plt.show()