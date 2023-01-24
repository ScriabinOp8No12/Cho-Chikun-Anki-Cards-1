import os
import cv2
import pytesseract

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)


solution_images = []
counter = 1

substring = "Pattern"

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[0:110, 168:542]  # looks for the word "Pattern"
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)

    if substring in result:
        pass
        # cropped_solution = img[]

    elif substring not in result and result != "":
        # vertically stack this image with the one before it
        # convert filename (which is a number) to "int" so we can combine with image before

        each_image_int = each_image.split(".")[0]
        each_image_int = int(each_image_int)
        previous_image_int = each_image_int-1
        previous_image_path = str(previous_image_int) + ".jpg"

        combined_solution_image = cv2.vconcat(each_image, previous_image_path)

        # change name of combined_solution_image to "FullSolution" + each_image   --> this will make the file names "FullSolution1, FullSolution2, etc."
        # write this name to a file (cv2.imwrite)
    else:
        pass
        # write name of file to the same folder with "FullSolution" added in front of the number
        # --->  example.   solution_image  = "FullSolution" + each_image (each_image will be a number)

    counter += 1





# cv2.imwrite(rf"C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_final{name_of_file}{counter}.jpg'", result)
