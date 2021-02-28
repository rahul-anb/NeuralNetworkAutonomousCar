import pandas
import os
import cv2
from datetime import datetime

global imgList,steeringList
countFolder=0
count=0
imgList=0
steeringList=0

myDirectory=os.path.join(os.getcwd(),'DataCollected')
#print(myDirectory)

#creating new folder depending on the prev folder count
while os.path.exists(os.path.join(myDirectory,f'IMG{str(countFolder)}')):
    countFolder+=1
newPath=myDirectory+'/IMG'+str(countFolder)
os.makedirs(newPath)

#trying to save all the images in the folder
def saveData(img,steering):
    global imgList,steeringList
    now=datetime.now()
    timestamp =str(datetime.timestamp(now).replace('.',''))
    #print("timestamp =",timestamp)
    fileName=os.path.join(newPath,f'Image_{timestamp}.jpg')
    cv2.imwrite(fileName,img)
    imgList.append(fileName)
    steeringList.append(steering)

#saving log file after session ends
def saveLog():
    global  imgList,steeringList
    rawData={'Image':imgList,
             'steering':steeringList}
    df=pandas.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory,f'log_{str(countFolder)}.csv'),index=False,header=False)
    print('Log Saved')
    print('TOtalImages: ',len(imgList))

if __name__=='__main__':
    cap=cv2.VideoCapture(1)
    for x in range(10):
        _,img=cap.read()
        saveData(img,0.5)
        cv2.waitKey(1)
        cv2.imshow("Image",img)
    saveLog()
