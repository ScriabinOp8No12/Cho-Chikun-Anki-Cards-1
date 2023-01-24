import easyocr
import cv2
import os

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorting_images = os.listdir(path_to_folder)
sorting_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

for each_image in sorting_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    result = reader.readtext(img, detail=0) #cropped_images_contrast, detail=0, allowlist='0123456789') # add "-" minus sign?
    print(result, f"{each_image}")

