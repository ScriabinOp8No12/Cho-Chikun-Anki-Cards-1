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

path_to_questions = os.listdir(r"C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\question_images_FINAL")

my_package = genanki.Package(my_deck)
my_package.media_files = []

for x in range(1, len(path_to_questions)+1):  # loop through all images in the question_images_FINAL folder
    my_note = genanki.Note(
        model=my_model,
        fields=[f'<img src="PuzzleNumber{x}.jpg"/>', f'<img src="SolutionNumber{x}.jpg"/>'])

    my_deck.add_note(my_note)
    my_package.media_files.append(rf"C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\question_images_FINAL\PuzzleNumber{x}.jpg")
    my_package.media_files.append(rf"C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\solution_images_FINAL\SolutionNumber{x}.jpg")

my_package.write_to_file(r'C:\Users\nharw\PycharmProjects\PDF2Anki\output_Folders\anki_output_FINAL\output_test_FINAL.apkg')
