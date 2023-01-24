import os

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

prefix = 'SolutionNumber'

for each_image in sorted_images:
    # construct the full path of the file
    file_path = os.path.join(path_to_folder, each_image)
    # construct the new name
    new_name = prefix + each_image
    # construct the full path of the new name
    new_path = os.path.join(path_to_folder, new_name)
    # rename the file
    os.rename(file_path, new_path)



