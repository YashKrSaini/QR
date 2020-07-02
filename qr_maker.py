import cv2
import qrcode

def make_qr(text=''):
    if len(text)==0:
        text=str(input("Enter QR code Text :"))
    file_loc="C:\yash_kumar\qrcode\\"
    print("Don't give space in file name ")
    code_name=str(input("Enter QR code picture file Name :"))
    file=file_loc+code_name+".png"
    img=qrcode.make(text)
    img.save(file)
    print(" Done ")

# This PC\Galaxy J7 Nxt(Yash)\Card\DCIM\Camera
#C:\yash_kumar\qrcode
def read_qr(frame,file_loc="C:\yash_kumar\qrcode"):
    ch=3
    if ch==2:
        print("Current Folder Location : "+file_loc)
        import os
        os.chdir(file_loc)
        img_list=[]
        num=0
        for i in os.listdir():
            if ".jpg" in i:
                print(num+1,'.) '+i)
                img_list.append(i)
                num=num+1
        img_num=int(input("Enter PNG Image number : "))
        file=file_loc+"\\"+img_list[img_num-1]
        img=cv2.imread(file)
        detector=cv2.QRCodeDetector()
        if detector:
            data, bbox, straight_qrcode = detector.detectAndDecode(img)
            print(">>>",data)
        else:
            print("No Data Found")
    else:
        detector=cv2.QRCodeDetector()
        if detector:
            data, bbox, straight_qrcode = detector.detectAndDecode(frame)
            return(data)
        else:
            pass
        

def video_qr():
    vid=cv2.VideoCapture(0)
    while(True):
        ret,frame=vid.read()
        cv2.imshow('Frame',frame)
        data=read_qr(frame)
        
        
        if len(data)>0:
            print('>>> ',data)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
    vid.release()
    cv2.destroyAllWindows()
