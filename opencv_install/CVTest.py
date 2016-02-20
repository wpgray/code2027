import cv2


# Read the image file
img = cv2.imread('original_phpS63uWD.fig', 1)
cap = cv2.VideoCapture(0)
# Create window and display the image with title 'Hello World'
while True:
    ret, frame = cap.read()
    cv2.imshow('Hello World', frame)
    # Hold the window until closed
    key = cv2.waitKey(1)
    if key == 27:
        break;
cap.release()

# Close window
cv2.destroyAllWindows()