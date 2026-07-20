# Step 1: Import required libraries
import cv2
import urllib.request
import matplotlib.pyplot as plt

# Step 2: Download a sample image (or use your own file path)
# Replacing 'sample.jpg' with your image file name if uploaded to Colab
url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
urllib.request.urlretrieve(url, "sample.jpg")

# Step 3: Read the image
# Note: OpenCV reads images in BGR format by default
img_bgr = cv2.imread("sample.jpg")

# Convert BGR to RGB so Matplotlib displays true colors
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Step 4: Convert the image to Grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Step 5: Display Original and Grayscale images side by side
plt.figure(figsize=(10, 5))

# Plot Original RGB Image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image (RGB)")
plt.axis("off")

# Plot Grayscale Image
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Step 6: Basic Handling Info
print(f"Original Image Dimensions : {img_rgb.shape}")
print(f"Grayscale Image Dimensions: {img_gray.shape}")
