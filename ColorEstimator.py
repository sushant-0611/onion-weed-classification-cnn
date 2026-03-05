import numpy
from PIL import Image, ImageFilter 
import os
 
def getGreenPercentage(image_path):
    tg=0
    count=0
    if os.path.isfile(image_path):
        imageob = Image.open(image_path).convert('RGB')
        width, height = imageob.size
        pix=imageob.load()
        for i in range(width):
            for j in range(height):
                col=pix[i,j]
                R=col[0]
                G=col[1]
                B=col[2]
                
                if(R<=110 and G>=110 and B<=110):
                    pix[i,j]=(0,255,0)
                    count=count+1
                else:
                    pix[i,j]=(255,255,255)
                # if(G>150):
                #     tg=tg+G
                #     count=count+1
                   # print(R,G,B)
               
        # percentage=tg/count          
        # return percentage    
    #    imageob.save("green.jpg") 
     #   print('count ',count)
        percentage=(count/(width*height))*100 
        finalpercentage=100-percentage
        return finalpercentage
       # print("Count ",count)
       

                  
           
 
# inputpath="testinginput/w1.jpg"
# percentage=getGreenCount(inputpath)   
# print("green Percentage ",percentage)