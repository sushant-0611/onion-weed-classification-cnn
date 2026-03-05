import numpy as np
from keras.models import load_model
import keras.utils as image
import cv2
import collections
import datetime
import operator
import os
import ColorEstimator
import WhatsAppSender

def initDetection(mobile_number, name):
    mymodel = load_model('model/weed_trained_data.h5')
    cap = cv2.VideoCapture(1)

    # Read the first frame to get dimensions
    _, img = cap.read()
    frame_height, frame_width = img.shape[:2]

    # Set width and height of the detection rectangle
    w, h = 220, 380

    # Center the rectangle
    x = (frame_width - w) // 2
    y = (frame_height - h) // 2

    resultlist = []
    while cap.isOpened():
        _, img = cap.read()
        cr_img = img[y:y+h, x:x+w]
        dim = (150, 150)
        cr_img = cv2.resize(cr_img, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite('temp.jpg', cr_img)
        defpercentage = ColorEstimator.getGreenPercentage('temp.jpg')
        print('green', defpercentage)

        if defpercentage < 97:
            test_image = image.load_img('temp.jpg', target_size=(150, 150, 3))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            pred = mymodel.predict(test_image)[0][0]
            resultyype = ""
            percentstr = str(defpercentage)

            print("Prediction number", pred)
            if pred == 1:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(img, 'Weed', ((x+w)//2, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                resultyype = "Weed"
            else:
                resultstr = 'non-weed'
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(img, resultstr, ((x+0)//2, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                resultyype = "Non-weed"

            cv2.imshow('ONION WEED DETECTION SYSTEM', img)

            resultlist.append(resultyype)
            frequency = collections.Counter(resultlist)
            cropfreq = dict(frequency)
            sorted_d = sorted(cropfreq.items(), key=operator.itemgetter(1))
            index = len(sorted_d) - 1
            mxvaluecrop = sorted_d[index]

            print("Matched", mxvaluecrop)
            typename = mxvaluecrop[0]
            typecount = mxvaluecrop[1]
            print("typename", typename)
            print("typecount", typecount)
            count = int(typecount)

            if count >= 100:
                if typename == 'Weed':
                    print("Weed Detected")
                    WhatsAppSender.sendInfoWA(mobile_number, name)
                    resultlist.clear()
                    break
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            cv2.putText(img, 'NO Crop AREA', ((x+w)//2, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.imshow('ONION WEED DETECTION SYSTEM', img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    initDetection()
