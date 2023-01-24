#0  Start a loop with a counter at 0, write the following images to a new folder (see #5.)
#1 If number at bottom of page doesn't go up by one from images in folder "bottom half solutions", then
#2. Append the image from the folder "2nd page solutions" to this image current image
#3. Increase the counter by 1 for images in folder "2nd page solutions" ONLY IF ABOVE IMAGE APPENDED TO PREVIOUS IMAGE
#4. Keep name / counter of bottom half solution consistent (don't change the name of this image)
#5. Write the new images to a separate folder here: C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_final


# basically I'm looping through each image in the "2nd half answer solutions" folder
# and attaching each one to the image from the other folder if the page number didn't go up by 1


import cv2
import os
import pytesseract

y_page_number = 905

path_to_2ndPageSolutions = r'C:\Users\nharw\Desktop\PDF2Anki Project\2ndPageSolutions'
sorted_2ndPageimages = os.listdir(path_to_2ndPageSolutions)
sorted_2ndPageimages.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

path_to_1stPageSolutions = r'C:\Users\nharw\Desktop\PDF2Anki Project\bottom_half_solution'
sorted_1stPageimages = os.listdir(path_to_1stPageSolutions)
sorted_1stPageimages.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

for each_image in sorted_2ndPageimages:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\2ndPageSolutions\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_bottom_of_page = img[940:, 310: 410]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result_page_number = pytesseract.image_to_string(cropped_bottom_of_page)
    print(result_page_number)