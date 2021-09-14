from os import access
import dropbox,time,random
import cv2

start_time = time.time()

def takePicture():
    number = random.randint(0,100)
    cvObject = cv2.VideoCapture(0)
    result = True
    while (result):
        flag,frame = cvObject.read()
        imgname = "img"+str(number) + ".png"
        cv2.imwrite(imgname,frame)
        start_time = time.time()
        result = False
    return imgname
    print("Photo taken")
    cvObject.release()
    cv2.destroyAllWindows

def uploadFile(imgname):
    access_token = 'sl.A4UBbDcOZ5KFS_bZ5HRvJKBZrVcH3OF66q9nufaMVOjJ3cc3PRT8R6obAuQpOZjxUL6APjUhghaLVB-xB-egw42NcORXweyTZts7c0pIrR0TQE3AI9NLeKzppBlFJ3xMt_qcPTT5oyM'
    file = imgname
    file_from = file
    file_to = "/folder3234/"+ (imgname)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file got uploaded')
def main():
    name = takePicture()
    uploadFile(name)

main()