import pytesseract
import cv2
import os
import numpy as np

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

substring = "Pattern"
answer_counter = 1  # start at 1 because I want my image names to start at 1 and not 0

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[0:110, 168:542]  # img[y:y+h, x:x+w]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)

    if substring in result:
        cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\{answer_counter}.jpg', img)
        answer_counter += 1

    elif substring not in result:
        cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\{answer_counter}.jpg', img)
        prev_image = cv2.imread(
            rf'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\{answer_counter-1}.jpg', 0) # "-1" is important
        curr_image = cv2.imread(rf'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\{answer_counter}.jpg', 0)

        combined_solution = np.vstack((prev_image, curr_image))  # vertically concatenates the 2 images

        file_name = f"{answer_counter-1}.jpg"  # saves it as the first answer's file name to stay consistent with question numbers
        cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\{file_name}', combined_solution)
