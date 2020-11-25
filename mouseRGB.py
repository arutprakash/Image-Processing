import cv2

 
image = cv2.imread("p.jpg")
 
cv2.imshow("MouseRGB", image) #Image show
cv2.moveWindow("MouseRGB", 0, 0) #Image move to 0,0 position on screen
cv2.waitKey(0)
 
height, width, channels = image.shape # Get image height and width
 
while True:
   
    x, y = cv2.EVENT_MOUSEMOVE#get mouse x,y position)
 
    if(x-8>=width or y-30>=height): # subtract window border values
 
        print("Out of bound")
 
    else:
        colorsB = image[y-30,x-8,0]
        colorsG = image[y-30,x-8,1]
        colorsR = image[y-30,x-8,2]
        colors = image[y-30,x-8]
 
    state_left = setMouseCallback #mouse left click values
 
    if state_left < 0: # Left button down = 0 or 1. Button up = -127 or -128
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print(colors)
        print(x-8,y-30)
 
        while(state_left < 0): #If you keep press left button its prevent infinite prints
            state_left = setMouseCallback
           
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
               
   
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break