import cv2
import numpy as np

"""
This is mostly test code for now.
Will clean up and comment when I figure out
what I am doing
great idea, luis
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
        im2, contours, heirarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        c_indx = 0
        max_area = 0
        for i in range(len(contours)):
            cur = contours[i]
            area = cv2.contourArea(cur)
            if area > max_area:
                max_area = area
                c_indx = i
        M = cv2.moments(contours[c_indx])

        # THE CENTROID X AND Y
        CX = int(M['m10'] / M['m00'])
        CY = int(M['m01'] / M['m00'])

        print(CY, CX)
        mask = cv2.circle(mask, (CX, CY), 20, (255, 255, 255), 1)
        # Display mask
        cv2.imshow("test", mask)

def GetCentroid(img):
    """
    Use the method I used to calculate CY and CX up there ^ to
    implement this function. This function takes a parameter img
    that is in BGR (rgb backwards), convert it to HSV and calculate
    CX and CY.
    :param img: the image in BGR, find the centroid
    :return: (CX, CY)
    """

    # Gave you a hint here, fill in the second parameter
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_value = np.array([HSV[0] - 5, 50, 50])
    upper_value = np.array([HSV[1] + 5, 255, 255])

    mask = cv2.inRange(img, lower_value, upper_value)
    print (CY, CX)

# Window title
IMAGE_NAME = "image"

# Values will be filled in later
LOWER_H = 81
LOWER_S = 50
LOWER_V = 50

UPPER_H = 101
UPPER_S = 255
UPPER_V = 255

# This creates video streaming from the camer
cap = cv2.VideoCapture(0)

# Read test image
img = cv2.imread('test.png', 1)

# Display image
cv2.imshow(IMAGE_NAME, img)
# Tell OpenCV to use mouseCallback for mouse functionality
cv2.setMouseCallback(IMAGE_NAME, mouseCallback)
print(GetCentroid(img))

# Convert image from RGB to HSV
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Hand images and clear memory
cv2.waitKey(0)
cv2.destroyAllWindows()

