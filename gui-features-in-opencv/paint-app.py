import numpy as np
import cv2

drawing = False
color, thickness, eraser_thickness = (0, 0, 0), 2, 4
erasing = False

def draw(event, current_x, current_y, flags, param):
    global drawing, erasing, color, thickness, prev_x, prev_y, eraser_thickness

    # when left mouse button is pressed start drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        prev_x, prev_y = current_x, current_y
        drawing = True
    # if mouse is moving with left button pressed, draw line
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if erasing:
                cv2.line(background, (prev_x, prev_y), (current_x, current_y), (255, 255, 255), eraser_thickness)
            else:
                try:
                    cv2.line(background, (prev_x, prev_y), (current_x, current_y), color, thickness)
                except NameError:
                    prev_x, prev_y = current_x, current_y
                    cv2.line(background, (prev_x, prev_y), (current_x, current_y), color, thickness)
            prev_x, prev_y = current_x, current_y
    # when left mouse button is released, stop drawing
    elif event==cv2.EVENT_LBUTTONUP:
        del prev_x
        del prev_y
        drawing = False

# mouse callback => empty function 
def nothing(x):
    pass

# window settings
background = np.full((512, 512, 3), 255, dtype=np.uint8)
window = cv2.namedWindow('Paint')
cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)
cv2.createTrackbar('thickness', 'Paint', 2, 20, nothing)
cv2.createTrackbar('eraser thickness', 'Paint', 4, 25, nothing)
cv2.setMouseCallback('Paint', draw)

while True:
    cv2.imshow('Paint', background)
    key = cv2.waitKey(1) & 0xFF

    if key==ord('q'):
        break
    elif key==ord('e'):
        # toggle erasing mode
        erasing = not erasing

    # changing drawing setting with trackbar position
    r = cv2.getTrackbarPos('R', 'Paint')
    g = cv2.getTrackbarPos('G', 'Paint')
    b = cv2.getTrackbarPos('B', 'Paint')
    eraser_thickness = cv2.getTrackbarPos('eraser thickness', 'Paint')
    thickness = cv2.getTrackbarPos('thickness', 'Paint')
    color = (b, g, r)

cv2.destroyAllWindows()

