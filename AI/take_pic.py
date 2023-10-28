import cv2
clicked = False
count = 0

def take_pic(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_RBUTTONDOWN:
        clicked = True
        
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', take_pic) 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width//3
y = height//3

w = width//3
h = width//3

while True:
    ret, frame = cap.read()
    
    cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,0,255),thickness= 4)
    
    cv2.imshow('Test', frame)
    
    if clicked == True:
        clicked = False
        print(clicked)
        if count != 6:
            print("!!")
            img = cv2.imwrite(f"ecisev{count}.jpg", frame)
            print(img)
            if img:
                count = count + 1
                print(count)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
cv2.destroyAllWindows()