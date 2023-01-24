import os
import genanki

my_model = genanki.Model(
    150983405,
    'Test Model',
    fields=[

        {'name': 'ImageFront'},
        {'name': 'ImageBack'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{ImageFront}}', # 'qfmt' stands for question format, don't change this
            'afmt': '{{ImageBack}}',
        },
    ],
    css="""
        img {
            max-width: 100%;
            max-height: 100%;
        }
        """
)

my_deck = genanki.Deck(
    230498230,
    'Eric Cho Chikun PDF1')  # this is the name of the deck that you see on Anki

path_to_questions = os.listdir(r"C:\Users\nharw\Desktop\PDF2Anki Project\question_images_FINAL")

my_package = genanki.Package(my_deck)
my_package.media_files = []

for x in range(1, len(path_to_questions)+1):  # loop through all images in the question_images_FINAL folder
    my_note = genanki.Note(
        model=my_model,
        fields=[f'<img src="PuzzleNumber{x}.jpg"/>', f'<img src="SolutionNumber{x}.jpg"/>'])  # PuzzleNumber2.jpg, SolutionNumber2.jpg  (original Eric code modification)
        # fields=['front of card text', 'back of card text', '<img src="PuzzleNumber1.jpg"/>', '<img src="SolutionNumber1.jpg"/>']) # original code

    my_deck.add_note(my_note)
    my_package.media_files.append(rf"C:\Users\nharw\Desktop\PDF2Anki Project\question_images_FINAL\PuzzleNumber{x}.jpg")
    my_package.media_files.append(rf"C:\Users\nharw\Desktop\PDF2Anki Project\solution_images_FINAL\SolutionNumber{x}.jpg")

my_package.write_to_file(r'C:\Users\nharw\Desktop\PDF2Anki Project\anki_output_FINAL\output_test_FINAL.apkg')


# Notes below / original code

# generate deck first, then loop through just new notes (just moved "my_deck" up from below "my_note" originally)
# while looping through note, add that note to the media file
# can do actual work in first loop, or not
# change order of these variables?

# 2 lines below: original modification code
#'qfmt': '<img src="{{ImageFront}}"/>',   # combination didn't work for some reason -> image wasn't showing up in anki
#'afmt': '<img src="{{ImageBack}}"/>',
