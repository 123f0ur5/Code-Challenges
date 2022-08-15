import cv2
from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image_path = r"C:\\Users\\Lucas\Desktop\\qwe.png"

img = cv2.imread(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

print(text[:-1])