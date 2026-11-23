import cv2
import matplotlib.pyplot as plt
import numpy as np

gray = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image at input.jpg")

noisy = gray.copy()
rnd = np.random.rand(*gray.shape)
noisy[rnd < 0.03] = 255
noisy[rnd > 0.97] = 0

sizes = [3, 5, 7, 11]
plt.figure(figsize=(14, 3.5))

plt.subplot(1, len(sizes) + 1, 1)
plt.imshow(noisy, cmap="gray")
plt.title("Salt & Pepper")
plt.axis("off")

for idx, k in enumerate(sizes, 2):
    out = cv2.medianBlur(noisy, k)
    plt.subplot(1, len(sizes) + 1, idx)
    plt.imshow(out, cmap="gray")
    plt.title(f"Median {k}x{k}")
    plt.axis("off")

plt.tight_layout()
plt.show()