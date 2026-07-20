"""2. Perform basic Image Handling and processing operations on the image
• Read an image in python and Convert an Image to Blur using GaussianBlur."""
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Option A: Upload your image file directly in Colab
print("Please upload your image file:")
uploaded = files.upload()

# Get the filename of the uploaded image
image_path = list(uploaded.keys())[0]

# Step 1: Read the image using OpenCV
img_bgr = cv2.imread(image_path)

# Step 2: Convert BGR to RGB (OpenCV uses BGR by default, Matplotlib uses RGB)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Step 3: Apply Gaussian Blur
# Kernel size must be positive and ODD numbers, e.g., (15, 15), (25, 25)
# Higher kernel sizes result in stronger blurring
kernel_size = (15, 15) 
img_blurred = cv2.GaussianBlur(img_rgb, kernel_size, sigmaX=0)

# Step 4: Display the Original and Blurred images side-by-side
plt.figure(figsize=(12, 6))

# Display Original Image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display Blurred Image
plt.subplot(1, 2, 2)
plt.imshow(img_blurred)
plt.title(f"Gaussian Blurred {kernel_size}")
plt.axis("off")

plt.tight_layout()
plt.show()
