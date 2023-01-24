# 1. Start with a counter at 1 that increments by 1 at the end of the following loop (done)
# 2. Create a loop that looks at the images to find:
#   If "Pattern" is at the top of the page, then crop the image below where the word solution or variation shows up
# 3. Otherwise, if "Pattern" doesn't show up at the top of the page, and that area isn't blank, then
#   attach the current image (based on the counter) with the image before (counter-1)
# 4. Concat the 2 images vertically using v.concat method, save the image to a folder with name Solution(counter)
# 4a. Make sure this image is saved as Solution(counter) with counter being the previous image's counter
# 5. These images will be numbered starting at 1, and will pair with question/puzzle 1 (saved into a folder already)
# 6. Since images2Anki code works for 1 image on front and 1 image on back already,
#    write a loop that will put Question1 on front, with corresponding Solution1 on the back


# watch out for counts that won't line up,  either one pass, or adopt a better numbering scheme
# name them 1a, 2a, then 2b if has

import os
import cv2
import pytesseract


path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

substring_Pattern = "Pattern"
substring_Variation = "Variation"
substring_Solution = "Solution"

counter = 1
y_start = 250
y_end = 375


for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[0:110, 168:542]  # location to look for the word "Pattern"
    cropped_middle_of_page = img[y_start:y_end, :]  # location to look for the word "Variation" or "Solution"
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result_top = pytesseract.image_to_string(cropped_top_of_page)
    result_split_point = pytesseract.image_to_string(cropped_middle_of_page, config='--psm 6')

    if substring_Solution in result_split_point or substring_Variation in result_split_point:
        pass # can't get logic to work!!!

    # for i in range(len(result_split_point["text"])):
    #     print(result_split_point["top"][i], counter)

    # if substring_Pattern in result_top:
    #     location_solution_variation = img[y_start:y_end, :]
    #     if substring_Solution in result_split_point or substring_Variation in result_split_point:

            # for i in range(len(result_split_point["text"])):
            #     print(result_split_point["top"][i], counter)


    #             cropped_answers = img[0: y_start + result_split_point["top"][i]]
    #         # write image to folder with current counter number
    #
    # elif substring_Pattern not in result_top and result_top != "":  # otherwise, if pattern not at top of page and that area isn't blank
    #     pass


        # vertically concat the current image with the one before (counter - 1)
        # write this combined image to folder (overwrite with same name so it updates Question5 to a new Question5 that is concatenated?)

    counter += 1

        # name_of_file = 'Question'
        #
        # print(rf'C:\Users\nharw\Desktop\PDF2Anki Project\top_half_puzzle\{name_of_file}{counter}.jpg')


        # cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\top_half_puzzle\{name_of_file}{counter}.jpg',
        #             cropped_question)


