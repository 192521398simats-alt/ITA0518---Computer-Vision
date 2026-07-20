"""10. Perform moving of an image from one place to another. """
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a realistic room background (Floor, Couch, Chair/Desk)
room_h, room_w = 400, 500
bg = np.zeros((room_h, room_w, 3), dtype=np.uint8)

# Room Floor (Beige)
bg[100:, :] = [180, 185, 190]
# Wall (Cream)
bg[:100, :] = [210, 225, 235]
# Black Couch at bottom left
cv2.rectangle(bg, (50, 250), (250, 380), (40, 40, 40), -1)
# Blue Desk/Cabinet top right
cv2.rectangle(bg, (250, 50), (350, 150), (180, 100, 30), -1)

# Step 2: Create a Person Patch (Moving Object)
def get_person():
    person = np.zeros((80, 40, 3), dtype=np.uint8)
    # Head
    cv2.circle(person, (20, 15), 10, (200, 220, 240), -1)
    # Shirt (Striped / Blue)
    cv2.rectangle(person, (10, 25), (30, 55), (230, 120, 50), -1)
    # Pants
    cv2.rectangle(person, (12, 55), (28, 80), (60, 60, 60), -1)
    return person

person_img = get_person()
p_h, p_w, _ = person_img.shape

# Function to place person at specific (X, Y) coordinates in the room
def move_person_to(background, person, x, y):
    canvas = background.copy()
    # Ensure coordinates stay within bounds
    canvas[y:y+p_h, x:x+p_w] = person
    return canvas

# Step 3: Move person to 4 different positions across the room
scene1 = move_person_to(bg, person_img, x=180, y=80)   # Pos 1: Standing Center
scene2 = move_person_to(bg, person_img, x=380, y=100)  # Pos 2: Standing Right
scene3 = move_person_to(bg, person_img, x=270, y=120)  # Pos 3: Near Chair
scene4 = move_person_to(bg, person_img, x=300, y=280)  # Pos 4: Lying on Floor

# Step 4: Display 4-panel movement layout (matching reference image style)
plt.figure(figsize=(12, 9))

# Panel 1
plt.subplot(2, 2, 1)
plt.imshow(scene1)
plt.title("Position 1: Standing Center (X=180, Y=80)", color='green', fontweight='bold')
plt.axis("off")

# Panel 2
plt.subplot(2, 2, 2)
plt.imshow(scene2)
plt.title("Position 2: Moved Right (X=380, Y=100)", color='green', fontweight='bold')
plt.axis("off")

# Panel 3
plt.subplot(2, 2, 3)
plt.imshow(scene3)
plt.title("Position 3: Moved Near Chair (X=270, Y=120)", color='green', fontweight='bold')
plt.axis("off")

# Panel 4
plt.subplot(2, 2, 4)
plt.imshow(scene4)
plt.title("Position 4: Moved to Floor (X=300, Y=280)", color='green', fontweight='bold')
plt.axis("off")

plt.tight_layout()
plt.show()

print("✓ Successfully moved the person across 4 distinct positions inside the room scene.")
