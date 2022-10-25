import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r'C:\Users\marcu\PycharmProjects\HiveLabels\labelDir\labels0.pdf')

# image = cv2.imread('letnumlabels/threeleft.jpg')
# mask = np.zeros(image.shape, dtype=np.uint8)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imwrite('letnumlabels/threstest.jpg', thresh)
# cv2.imshow('letnumlabels/threeleft.jpg', thresh)
# cv2.waitKey()
#
text = pytesseract.image_to_string('finalversion/tresright.jpg')
print(text)