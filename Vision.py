import cv2
import numpy as np

"""
This is mostly test code for now.
Will clean up and comment when I figure out
what I am doing
"""

def mouseCallback(event, x, y, flags, param):
    """
    This function handles mouse events. Currently just
    creates a binary mask for the test image where the
    user clicks. It finds the HSV value of the pixel
    where the user clicks and masks the pixels with
    similar values.

    :param event: The specific mouse event.
    :param x: Horizontal position of the mouse
    :param y: Vertical position of the mouse
    :param flags:  N/A
    :param param:  N/A
    :return: None
    """

    # Detect when the left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the HSV value of the picture, image coordinates are in Y, X
        HSV = img[y, x]
        # Create upper and lower HSV bounds
        lower_value = np.array([HSV[0]-5,50,50])
        upper_value = np.array([HSV[0]+5,255,255])
        print(HSV)

        # Create binary image mask
        mask = cv2.inRange(img, lower_value, upper_value)

        # Display mask
        cv2.imshow("test", mask)



def GetCentroid():
    """
    Will compute the centroid of a binary image
    :return:
    """
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# Window title
IMAGE_NAME = "image"

# Values will be filled in later
LOWER_H = 0
LOWER_S = 0
LOWER_V = 0

UPPER_H = 0
UPPER_S = 0
UPPER_V = 0

# This creates video streaming from the camera
# cap = cv2.VideoCapture(0)

# Read test image
img = cv2.imread('test.png', 1)

# Display image
cv2.imshow(IMAGE_NAME, img)
# Tell OpenCV to use mouseCallback for mouse functionality
cv2.setMouseCallback(IMAGE_NAME, mouseCallback)

# Convert image from RGB to HSV
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Hand images and clear memory
cv2.waitKey(0)
cv2.destroyAllWindows()

