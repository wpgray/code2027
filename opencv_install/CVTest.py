import cv2


# Read the image file
img = cv2.imread('original_phpS63uWD.fig', 1)

# Create window and display the image with title 'Hello World'
cv2.imshow('Hello World', img)

# Hold the window until closed
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()