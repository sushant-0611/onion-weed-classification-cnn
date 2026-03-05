import cv2
import os

# De-Forestation,Forestation"
datasetpath="DATASET"
typename="test"
state_type="non-weed" 


if not os.path.exists(datasetpath):
    os.makedirs(datasetpath)         
    

type_datasetpath=datasetpath+"//"+typename
if not os.path.exists(type_datasetpath):
    os.makedirs(type_datasetpath)          
        

dataset_state_type=type_datasetpath+"//"+state_type
if not os.path.exists(dataset_state_type):
    os.makedirs(dataset_state_type)      
    
      
cap=cv2.VideoCapture(0)
imgeno=1
x=200
y=50
h=300
w=265
while cap.isOpened():
    _,capimg=cap.read()
    img = capimg[y:y+h, x:x+w]
      
    cv2.rectangle(capimg,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Capture Image( Press ESC to quit)',capimg)
    k = cv2.waitKey(1) 
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
    # SPACE pressed
        filename=str(imgeno)   
        newfilepath=dataset_state_type+"//"+filename+".jpg"
        dim = (150, 150)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            
        cv2.imwrite(newfilepath,img)
        imgeno=imgeno+1
        print("Captured  path is ",newfilepath)
      
                
          


cap.release()
cv2.destroyAllWindows()