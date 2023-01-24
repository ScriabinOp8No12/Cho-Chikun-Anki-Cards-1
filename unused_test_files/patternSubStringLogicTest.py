# string is the output pytesseract is giving me
# substring is the word "Pattern"

# 1. return boolean value using if logic and in operator to see if Pattern is within the pytesseract output
# 2. if True, crop image of certain section of top of page (where puzzle is) --> save as puzzle NUMBER + QUESTION
# 3. if False, just crop the entire page -> save as puzzle NUMBER + ANSWER
# 3a. save these into file names of page number and puzzle (one has QUESTION, one has ANSWER in file name)
# 3a. --> this makes it easier to load into front and back of anki card
# 4. to crop certain section of top of page, look for the word "solution" near the top of the page, then
# 4a. find location of the word "solution" and then crop from Y - LOCATION just below "PATTERN" to ~5px above "SOLUTION"

string = "Pattern 1"
substring = "Pattern"


def pattern_checker():
    if substring in string:
        return "substring in string"
    else:
        return "substring NOT in string"


print(pattern_checker())
