import cv2 

b = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

c = cv2.VideoCapture(0)

while True:
    d_rec, e_image = c.read()
    f = cv2.cvtColor(e_image, cv2.COLOR_BGR2GRAY)
    g = b.detectMultiScale(f, 1.3, 6)
    
    for (x1,y1,w1,h1) in g:
        cv2.rectangle(e_image,(x1,y1), (x1+w1,y1+h1),(255,0,0),5)
    
    cv2.imshow('img', e_image)
    h= cv2.waitKey(40) & 0xff
    if h == 40:
        break 
    
c.release()
cv2.destroyAllWindows()
    
    
    