import os

path_to_folder = r'C:\Users\nharw\Desktop\PDF2Anki Project\Image of each page'
images = os.listdir(path_to_folder)
images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Python doesn't sort properly so this line is needed

image_number = 1

for each_image in images:
    os.rename(os.path.join(path_to_folder, each_image), os.path.join(path_to_folder, str(image_number) + '.jpg'))
    image_number += 1


# os.rename() and os.path.join() syntax are as follows:

# os.rename(OLD FILE NAME, NEW FILE NAME)
# os.path.join(part 1 of file path to join, part 2 of file path to join, part 3, etc.)