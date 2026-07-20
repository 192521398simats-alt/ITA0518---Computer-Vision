"""5. Perform basic Image Handling and processing operations on the image
• Read an image in python  and  Erode an Image using erode function."""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Specify your image path
image_path = 'image_20b4b2.jpg' 

# Read the image
img_bgr = cv2.imread(image_path)

if img_bgr is not None:
    # Step 2: Convert to RGB for proper display with matplotlib
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
    # Convert to Grayscale and generate edge outline (Erosion works best on binary/edge maps)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 200)
    
    # Step 3: Define a Structuring Element (Kernel)
    # A 3x3 matrix of ones is a standard kernel size for subtle erosion
    kernel = np.ones((3, 3), np.uint8)
    
    # Step 4: Apply the cv2.erode function
    img_eroded = cv2.erode(img_edges, kernel, iterations=1)
    
    # Step 5: Plot results
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")
    
    plt.subplot(1, 3, 2)
    plt.imshow(img_edges, cmap="gray")
    plt.title("Original Edges")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.imshow(img_eroded, cmap="gray")
    plt.title("Eroded Edges (Thinned)")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()
else:
    print(f"Error: Could not find '{image_path}'. Check your file name in the Colab sidebar.")
