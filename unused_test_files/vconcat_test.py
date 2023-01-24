import os
import cv2
import numpy as np

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\test_images_for_vconcat'
sorted_images = os.listdir(path_to_folder)

solution_images = []

for each_image in sorted_images:
    path_to_img = os.path.join(path_to_folder, each_image)
    img = cv2.imread(path_to_img)
    solution_images.append(img)

combined_image = cv2.vconcat(solution_images)

output_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\output_folder'  #writes image to output_folder

# converts 5.jpg and 6.jpg to an int by splitting off anything past the "." and then just taking the first part
file_name1, file_ext1 = os.path.splitext(sorted_images[0])
file_name2, file_ext2 = os.path.splitext(sorted_images[1])
file_name1_int = int(file_name1)
file_name2_int = int(file_name2)

# saves the file name as the first .jpg
if file_name1_int < file_name2_int:
    output_path = os.path.join(output_folder, "FullSolution"+file_name1 + ".jpg")
else:
    output_path = os.path.join(output_folder, "FullSolution"+file_name2 + ".jpg")

cv2.imwrite(output_path, combined_image)
