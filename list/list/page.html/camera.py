import cv2 
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('first.png',frame)
        break
vid.release()
cv2.destroyAllWindows()

# import cv2 as cv
# cam = cv.videoCapture(0)
# while True:
#     ref,frame=cam.read()
#     cv.imshow('press q to quit',frame)
#     if cv.waitkey==ord('c'):
#         cv.imwrite('first.phy',frame)
#         break
#     cam.release()
# import turtle
# turtle.bgcolor('')
# turtle.speed(0)
# turtle.pensize(2)
# turtle.pencolor('blue')
# def drawcircel(radius):
#     for i in range(10):
#         turtle.circel(radius)
#         radius=radius-4
# def drawdesign():
#     for i in range(10):
#         drawcircel(150)
#         turtle.right(36)
# drawdesign()
# turtle.done()