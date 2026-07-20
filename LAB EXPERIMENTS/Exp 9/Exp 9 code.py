"""9. Perform Rotation of an image to clockwise and counter clockwise direction."""
import cv2
import urllib.request
import matplotlib.pyplot as plt

# Step 1: Download a standard sample image directly into Colab
image_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/butterfly.jpg"
image_path = "sample_image.jpg"
urllib.request.urlretrieve(image_url, image_path)

# Step 2: Read the image
img_bgr = cv2.imread(image_path)

if img_bgr is not None:
    # Convert BGR to RGB for correct color display in Matplotlib
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Step 3: Perform Rotations using OpenCV
    # Clockwise Rotation (90 Degrees)
    img_clockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

    # Counter-Clockwise Rotation (90 Degrees Counter-Clockwise / 270 Degrees)
    img_counter_clockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Step 4: Display Original, Clockwise, and Counter-Clockwise images side-by-side
    plt.figure(figsize=(15, 5))

    # Original Image
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Clockwise Rotated Image
    plt.subplot(1, 3, 2)
    plt.imshow(img_clockwise)
    plt.title("Rotated Clockwise (90°)")
    plt.axis("off")

    # Counter-Clockwise Rotated Image
    plt.subplot(1, 3, 3)
    plt.imshow(img_counter_clockwise)
    plt.title("Rotated Counter-Clockwise (-90°)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

else:
    print("Error: Could not load the image.")
