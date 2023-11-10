import numpy as np
import pandas as pd
import seaborn as sns
import cv2

from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import GridSearchCV, cross_validate, RandomizedSearchCV, validation_curve
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

from lightgbm import LGBMClassifier
df = pd.read_csv("data.csv")

color_dict = {0: "Black",
             1: "Blue",
             2: "Brown",
             3: "Green",
             4: "Grey",
             5: "Orange",
             6: "Pink",
             7: "Purple",
             8: "Red",
             9: "White",
             10: "Yellow"}
             
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

model = LGBMClassifier().fit(X_train, y_train)

picsel_centers = [(50,50), (50,150), (50,250),
              (150,50), (150,150), (150, 250),
              (250,50), (250,150), (250,250)]
              
              
              
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
        #print(clicked)
        if count != 6:
            #print("!!")
            img = cv2.imwrite(f"ecisev{count}.jpg", frame)
            #print(img)
            if img:
                
                count = count + 1
                print(count)
                
               
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()



cv2.destroyAllWindows()


import cv2
for i in range(6):
    image = cv2.imread(f'ecisev{i}.jpg')

    # Kırpma koordinatlarını belirle (x, y, genişlik, yükseklik)
    crop_coordinates = (x, y, w, h)

    # Resmi kırp
    cropped_image = image[crop_coordinates[1]:crop_coordinates[1] + crop_coordinates[3], crop_coordinates[0]:crop_coordinates[0] + crop_coordinates[2]]

    # Kırpılmış resmi göster veya kaydet
    cv2.imwrite(f'ecisev{i}.jpg', cropped_image)
    
for i in range(6):
    img = cv2.imread(f'ecisev{i}.jpg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, (300, 300))

    rnge1 = -50
    rnge2 = -50
    for i in range(3):
        rnge2 = -50
        rnge1 = rnge1 + 100 
        for j in range(3):

            rnge2 = rnge2 + 100

            color_area = img_rgb[rnge1-25: rnge1+25, rnge2-25: rnge2+25]
            red_mean = int(color_area[:,:,0].mean())
            green_mean = int(color_area[:,:,1].mean())
            blue_mean = int(color_area[:,:,2].mean())
            #print(red_mean)
            #print(green_mean)
            #print(blue_mean)
            picsels = np.array([red_mean, green_mean, blue_mean])
            picsels = picsels.reshape(1, 3)

            #print(picsels)
            print(color_dict[model.predict(picsels)[0]])
