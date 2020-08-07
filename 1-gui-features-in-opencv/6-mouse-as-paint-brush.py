import numpy as np
import cv2 as cv

drawing = False # True if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    # if left button is pressed start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # if mouse is moving
    elif event == cv.EVENT_MOUSEMOVE:
        # and drawing is True i.e left button is pressed
        if drawing == True:
            # draw rectangle if mode = True
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            # else draw circle
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    # if left mouse buttion is up disable drawing
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        
        # when left buttion is released, draw rectangle on image if mode == True
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # if mod==False draw circle
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

# create blank window and bind the mouse callback function
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
# display the blank window
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    # when 'm' is pressed toggle drawing mode
    if k==ord('m'):
        mode = not mode
    # when 'q' is pressed, exit the program
    elif k==ord('q'):
        break
cv.destroyAllWindows()
