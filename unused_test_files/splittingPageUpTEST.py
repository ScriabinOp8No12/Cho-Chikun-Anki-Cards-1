import pytesseract
import cv2
import os
from patternSubStringFINAL import pages_with_pattern_at_top

# for puzzle/image numbers that have one page of solutions, look for the word "solution" at location 250:350 in
# the y-axis, then split the page up, so it's the part above where solution shows up, and the part below

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
    cropped_top_of_page = img[250:350, :]  # crop is in format img[y:y+h, x:x+w]  # detect the word solution in y value range 250-350 (should be just one)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_data(cropped_top_of_page, config='--psm 6', output_type=pytesseract.Output.DICT)
    # Iterate through the data and check for the "top" value (y position of where the word "solution" is located)
    for i in range(len(data["text"])):
        if "solution" in data["text"][i].lower() or "variation" in data["text"][i].lower():
            # Print the "top" value of the word "solution" or "variation"
            print(data["top"][i], each_image)    # for bug testing:   print(data["top"][i], each_image)


# if using img[200:320, :], REMEMBER TO ADD 200 to Y value of output, since it would start at a crop location of Y = 200
