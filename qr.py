import cv2 as cv

print(cv.__version__)

_path='D:\coding\PRML\lab4\gitrepo.png'

def qrReader(path):
    img=cv.imread(path)

    qcd=cv.QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
    print(retval) # returns true if QR code is detected

    print(decoded_info[0]) # url or wtever string is encoded in qr...decoded_info returns tuple

qrReader(_path)