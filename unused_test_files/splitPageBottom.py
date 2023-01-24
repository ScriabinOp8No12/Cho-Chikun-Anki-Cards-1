import pytesseract
import cv2
import os
# from patternSubStringFINAL import pages_with_pattern_at_top

# for puzzle/image numbers that have one page of solutions, look for the word "solution" at location 250:350 in
# the y-axis, then split the page up into 2 'screenshots',
# so it's the part above where solution shows up, and the part below

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

# isdigit only true when isdigit contains exactly 1 digit (won't take letters)
# could split off the .jpg by using code like this: "10.jpg".split(".")[0]
# os.path.splitext (better way)
#after stripping out number, assert filter(str.isdigit, sorted_images)

# assert str.isdigit("1")    #debugging tool
# assert str.isdigit("10")
# assert not str.isdigit("Banana")
# assert str.isdigit("Banana")

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



path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

y_values_split_page = []
counter = 1

# constants should be put in variables (refactor them into a single variable)
# same with "path_to_img"

for each_image in pages_with_pattern_at_top:
    path_to_img = rf'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page\{each_image}'
    img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
    cropped_top_of_page = img[250:375, :]  # crop is in format img[y:y+h, x:x+w]  # detect the word solution in y value range 250-350 (should be just one)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_data(cropped_top_of_page, config='--psm 6', output_type=pytesseract.Output.DICT)
    # Iterate through the data and check for the "top" value (y position of where the word "solution" is located)
    data_filtered = [(i, x) for i, x in enumerate(data["text"]) if "Solution" in x or "Variation" in x] #now when grabbing first or last item in data_filtered
    assert len(data_filtered) > 0, (data["text"], each_image)
    # for i in range(len(data["text"])): # won't need this here now
    # if len(data_filtered) > 1:
    #     data_filtered = [(i, x) for i, x in data_filtered if data["text"][i+1] == "1."]
    assert len(data_filtered) == 1, (data["text"], each_image)

    i, x = data_filtered.pop()

         # if "solution" in data["text"][i].lower() or "variation" in data["text"][i].lower():
    # for bug testing:   print(data["top"][i], each_image)
    name_of_file = 'SolutionNumber'
    # y_values_split_page.append(["top"][i])
    y_offset = 240 # using 240 to crop it slightly above the word solution now (word solution top is at y = 250)
    cropped_question = img[y_offset+data["top"][i]:]   # cropping from 250 to end
    print(rf'C:\Users\nharw\Desktop\PDF2Anki Project\bottom_half_solution\{name_of_file}{counter}.jpg')
    cv2.imwrite(rf'C:\Users\nharw\Desktop\PDF2Anki Project\bottom_half_solution\{name_of_file}{counter}.jpg', cropped_question)
    counter += 1


            # don't forget to add the .jpg at the end of the file name, otherwise cv2 gets mad
            # these 3 lines are used for bug testing (opens up the cropped part of the image)
            # cv2.imshow("imagetest.jpg", cropped_question)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

# clickable board like on OGS, 'image map' in html browser would tell you where you clicked