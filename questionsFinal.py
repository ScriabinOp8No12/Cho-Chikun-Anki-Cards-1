# 1. For each image, look for the word "Pattern" at the top of the page to determine if there's a question on that page
# 1a. If there is the word "Pattern" at the top, then it must have a question/puzzle right below it.
# 2. Within these images, look for the word "Solution" or "Variation" at y-location 250:350
# 2a. These 2 words are case-sensitive, and only appear in one location (just before the answer/solution begins)
# 3. Split the page from y = 0 to the y-value found in 2.
# 4. Make sure code is correctly cropping the image, ex. if y-location is 290, need to crop at y = 40 (290 minus 250)

import pytesseract
import cv2
import os

path_to_folder = r'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

pages_with_pattern_at_top = []
substring = "Pattern"

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
    cropped_top_of_page = img[0:110, 168:542]  # crop is in format img[y:y+h, x:x+w]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)
    if substring in result:
        pages_with_pattern_at_top.append(each_image)

path_to_folder = r'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

y_values_split_page = []
counter = 1

for each_image in pages_with_pattern_at_top:
    y_offset = 250 # since we crop the image from y = 250, the values start at 0 when y = 250, so we need to add 250 below
    path_to_img = rf'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[y_offset:375, :]  # Detect word "Solution" or "Variation" in y value range 250-375
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_data(cropped_top_of_page, config='--psm 6', output_type=pytesseract.Output.DICT)

    # Iterate through the data and find the "top" value (y-position of where "Solution" or "Variation" is located)
    data_filtered = [(i, x) for i, x in enumerate(data["text"]) if "Solution" in x or "Variation" in x] # now when grabbing first or last item in data_filtered
    assert len(data_filtered) > 0, (data["text"], each_image)   # bug catching line
    assert len(data_filtered) == 1, (data["text"], each_image)  # bug catching line
    i, x = data_filtered.pop()

    name_of_file = 'PuzzleNumber'

    cropped_question = img[0: y_offset+data["top"][i]]
    print(rf'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\question_images_FINAL\{name_of_file}{counter}.jpg')
    cv2.imwrite(rf'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\question_images_FINAL\{name_of_file}{counter}.jpg', cropped_question)
    counter += 1


# Below block of code is the list comprehension broken up into a for loop. Good for understanding / bug testing

# data = pytesseract.image_to_data(cropped_top_of_page, config='--psm 6', output_type=pytesseract.Output.DICT)
# data_filtered = []
#
# for i in range(len(data["text"])):
#     x = data["text"][i]
#     if "Solution" in x or "Variation" in x:
#         data_filtered.append((i, x))
#
# i, x = data_filtered.pop()

# -----------------------------------------------------------------------------------------------------------------
# top: cropped_question = img[0: y_offset+data["top"][i]]

# isdigit only true when isdigit contains exactly 1 digit (won't take letters)
# could split off the .jpg by using code like this: "10.jpg".split(".")[0]
# os.path.splitext (better way)
# after stripping out number, assert filter(str.isdigit, sorted_images)

# assert str.isdigit("1")    #debugging tool
# assert str.isdigit("10")
# assert not str.isdigit("Banana")
# assert str.isdigit("Banana")

# for i in range(len(data["text"])): # won't need this here now
# if len(data_filtered) > 1:
#     data_filtered = [(i, x) for i, x in data_filtered if data["text"][i+1] == "1."]

# y_values_split_page.append(["top"][i])

# if "solution" in data["text"][i].lower() or "variation" in data["text"][i].lower():
# for bug testing:   print(data["top"][i], each_image)

# don't forget to add the .jpg at the end of the file name, otherwise cv2 gets mad
# these 3 lines are used for bug testing (opens up the cropped part of the image)
# cv2.imshow("imagetest.jpg", cropped_question)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# clickable board like on OGS, 'image map' in html browser would tell you where you clicked
