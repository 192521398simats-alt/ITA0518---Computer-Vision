"""8. Scaling an image to its Bigger and Smaller sizes."""
import cv2
from IPython.display import HTML, display

image_path = 'sample image.jpg'
img_bgr = cv2.imread(image_path)

if img_bgr is not None:
    h, w = img_bgr.shape[:2]

    # Generate smaller and larger versions
    img_smaller = cv2.resize(img_bgr, (int(w * 0.35), int(h * 0.35)), interpolation=cv2.INTER_AREA)
    img_bigger  = cv2.resize(img_bgr, (int(w * 1.5), int(h * 1.5)), interpolation=cv2.INTER_CUBIC)

    # Save to disk
    cv2.imwrite("smaller.jpg", img_smaller)
    cv2.imwrite("bigger.jpg", img_bigger)

    # Display sequentially using HTML img tags with explicit widths
    html_code = f"""
    <h3>1. Smaller Image (35% scale: {img_smaller.shape[1]}x{img_smaller.shape[0]} px)</h3>
    <img src="smaller.jpg" style="width:{img_smaller.shape[1]}px;"><br><br>

    <h3>2. Original Image ({w}x{h} px)</h3>
    <img src="{image_path}" style="width:{w}px;"><br><br>

    <h3>3. Bigger Image (150% scale: {img_bigger.shape[1]}x{img_bigger.shape[0]} px)</h3>
    <img src="bigger.jpg" style="width:{img_bigger.shape[1]}px;">
    """
    display(HTML(html_code))
