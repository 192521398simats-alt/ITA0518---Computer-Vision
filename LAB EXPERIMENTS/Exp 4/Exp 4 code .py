import cv2
import numpy as np
import matplotlib.pyplot as plt

# Replace with your actual file name
image_path = 'image_20b4b2.jpg' 

# Step 1: Read the image
img_bgr = cv2.imread(image_path)

if img_bgr is not None:
    # Convert to RGB for visualization
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
    # Step 2: Extract outlines using Canny (Dilation works best on binary/edge images)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 200)
    
    # Step 3: Define a Structuring Element (Kernel) for Dilation
    # A larger kernel or more iterations increases the dilation (thickness) effect
    kernel = np.ones((5, 5), np.uint8)
    
    # Step 4: Apply Dilate Function
    img_dilated = cv2.dilate(img_edges, kernel, iterations=1)
    
    # Step 5: Display the results
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")
    
    plt.subplot(1, 3, 2)
    plt.imshow(img_edges, cmap="gray")
    plt.title("Edges (Before Dilation)")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.imshow(img_dilated, cmap="gray")
    plt.title("Dilated Edges (Thicker)")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()
else:
    print(f"Error: Could not find '{image_path}'. Please verify the filename.")
