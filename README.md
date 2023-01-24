This project takes a specific Cho Chikun PDF and converts it into an Anki deck using Computer Vision to detect keywords.

The images2ankiFinal.py, questionsFinal.py and solutionsFinal.py modules save the outputs in the output_Folders folder.
Please make sure your file paths in the above modules are correct to avoid any bugs.

The outputs are saved into the anki_output_FINAL, questions_images_FINAL, and solutions_images_FINAL folders respectively. 

All you have to do is open (by double-clicking) the output_test_FINAL.apkg and Anki will open the deck.  


Method:

1. For each image, look for the word "Pattern" at the top of the page to determine if there's a question on that page.
   If the word "Pattern" is at the top, then it must have a question right below it.

2. Within these images, look for the word "Solution" or "Variation" at a specific y-location (it always appears between 250 - 350)
   This Solution or Variation keyword is always right above where the answer begins. 

3. Split the page from the top (y = 0) to the y-value found in part 2 above (where the answer begins). 
   This is equivalent to taking a screenshot of just the question.
   Save these images as files with the following names: 1.jpg, 2.jpg, 3.jpg, etc.

4. For the answers that are associated with these questions, since some answers go for more than one page, we can't 
   just put Question 1 on the front of the anki card, and Answer 1 on the back of the anki card. 
   The pages that don't have the word "Pattern" at the top are the continuation of the answers.
   Therefore, all we need to do is vertically concatenate this image with the image before and name them 1.jpg, 2.jpg, 3.jpg, etc.
   so that the answer images will be aligned with the question images when we put them into our anki deck.

5. Once we have all the questions and answers with the correct numbering saved in separate folders, we use the genanki 
   library to automate putting question1 onto the front of the anki card, and answer1 onto the back of the anki card.


   
