import pytesseract
import cv2
import os

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

pages_with_pattern_at_top = []
substring = "Pattern"

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
    cropped_top_of_page = img[0:110, 168:542]  # crop is in format img[y:y+h, x:x+w]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)
    if substring in result:
        pages_with_pattern_at_top.append(each_image)

print(pages_with_pattern_at_top)




# if substring of "Pattern" in [result] of pytesseract.image_to_string,
# then save as puzzle number 1, loop and add 1 each time

