import os
import numpy as np #can use pillow library as well (PIL -> Python Image Library)
import cv2
import pytesseract

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)


counter = 1

substring = "Pattern"

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[0:110, 168:542]  # looks for the word "Pattern"
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)

    if substring not in result and result != "":

        name_of_file = 'Page2Solutions '
        print(name_of_file, counter)
        cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\2ndPageSolutions\{name_of_file}{counter}.jpg', img)
        counter += 1

