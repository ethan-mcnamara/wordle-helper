# Ethan McNamara
# 2022-01-30

# These import statements take a short while, the print statement shows that process is ongoing
print("Downloading word list...")
from nltk.corpus import words
import re
from time import sleep

def main():
    # Get a list of every word in English language and reduce it to only 5-letter words
    wordle_words = [word for word in words.words() if len(word) == 5]

    # Sort the list alphabetically
    wordle_words.sort()

    # Player instructions
    print("Ready\n")
    sleep(0.3)
    print("Instructions:\n")
    sleep(0.05)
    print("Enter the words you've tried in Wordle, with each letter seperated by a space")
    print("Letters can be entered in either upper or lowercase\n")
    sleep(0.05)
    print("For each GRAY letter, do not add any characters to the letter")
    print("For every YELLOW letter, surround the letter with \'-\' characters")
    print("\tExample: If the letter F was shown in YELLOW, enter -F-")
    print("For every GREEN letter, surround the letter with \'*\' characters")
    print("\tExample: If the letter A was shown in GREEN, enter *A*")
    print("-------------------------------------------------------------------------------\n")
    sleep(0.3)
    input("Press enter to continue\n")

    # Get the number of words already tried by the user
    num_words = int(input("How many words have you tried in Wordle?\n"))
    print("\n")

    # List to store the raw input from the user
    user_input = []

    # List of lists to store the individual letters for each work inputted by the user
    formatted_input = []

    # List to store the possible letters for each index in the word
    final_word = [[], [], [], [], []]

    # List to store the letters seen in green, known to be in correct position
    green_letters = ["", "", "", "", ""]

    # List to store all words that match the Wordle conditions
    output_words = []

    # List to store all letters known to be in the final word
    known_letters = []

    # List to store all letters known to not be in the final word
    invalid_letters = []

    # Get the input words from the user
    for num in range(num_words):
        # Get the words and their colour from the user
        user_input.append(input("Enter a word, remember above formatting:\n"))
        # Seperate the letters, using spaces as seperators
        formatted_input.append(user_input[-1].lower().split())
        # All Wordle words must be 5 letters
        # Keep asking for words until a 5-letter word is recieved
        while (True):
            if (len(formatted_input[-1]) != 5):
                print("\n**Your word was not 5 letters, try again**\n")
                user_input.pop()
                formatted_input.pop()
                user_input.append(input("Enter a word, remember above formatting:\n"))
                formatted_input.append(user_input[-1].lower().split())
            else:
                break

    # List to store the current word being processed
    cur_word = []

    # Used to determine whether a green letter can occur more than once in a word
    single_occurrence = False

    # Iterate through each word and each letter in each word
    for word in formatted_input:
        cur_word = [letter.replace("-", "").replace("*", "") for letter in word]
        single_occurrence = False
        for letter in word:
            # YELLOW word
            if (re.search("-.-", letter)):
                for index in range(5):
                    # Since it's yellow, the letter cannot be seen in this position
                    if (index == word.index(letter)):
                        continue
                    # If a green letter has already been seen in that position, skip this position
                    elif (green_letters[index] != ""):
                        continue
                    # Do not add duplicate letters to the list
                    elif (letter.replace("-", "") not in final_word[index]):
                        final_word[index].append(letter.replace("-", ""))
                        known_letters.append(letter.replace("-", ""))
                # If this letter has previously been declared invalid, reverse that
                if (letter in invalid_letters):
                    invalid_letters.remove(letter)
            # GREEN letter
            elif (re.search("\*.\*", letter)):
                # Clear all other letters from that position and replace them with this letter
                final_word[word.index(letter)] = []
                final_word[word.index(letter)].append(letter.replace("*", ""))
                # Add this letter to the green_letters list
                green_letters[word.index(letter)] = letter.replace("*", "")
                # Add this letter to the known_letters list
                known_letters.append(letter.replace("*", ""))
                # If this letter has previously been declared invalid, reverse that
                if (letter in invalid_letters):
                    invalid_letters.remove(letter)
            # GRAY letter
            else:
                # If this letter occurs more than once in this word, adjust the boolean
                if (cur_word.count(letter) > 1):
                    single_occurrence = True
                # If this GRAY letter is present more than once in this word
                # and the letter has previously been seen as a GREEN letter,
                # then it is known that the letter can not appear again and
                # thus is removed from all other positions.
                # If this is not true, a GREEN letter may occur again in a different position
                if (single_occurrence and (letter in green_letters)):
                    for index in range(5):
                        if (index != green_letters.index(letter)):
                            final_word[index].remove(letter)
                # If it does not fall in the prior conditions, it is an invalid letter
                elif(letter not in known_letters):
                    invalid_letters.append(letter)

    # Boolean used to store whether the word matches the conditions
    word_match = True

    # Add to output_list all words that contain the green letters in their spots and the yellow letters in any spots
    # May include other letters not yet seen
    for word in wordle_words:
        word_match = True

        # Ensure that of the green words seen, all match
        for index in range(5):
            # Ensure the current position of the word does have a green letter
            # If not, skip this position
            if (green_letters[index] != ""):
                if (word[index] != green_letters[index]):
                    word_match = False
                    break
        if (word_match):
            # Ensure that all yellow letters, whose position is not yet known are found in the word
            for letter in known_letters:
                if (word.find(letter) == -1):
                    word_match = False
                    break
        if (word_match):
            # Ensure that no invalid letters appear in the word
            for letter in invalid_letters:
                if (word.find(letter) != -1):
                    word_match = False
                    break
        # If the word matches all conditions, add it to the output list
        if (word_match):
            output_words.append(word)

    print("-------------------------------------------------------------------------------\n")
    print("Possible words:")

    # Sort the list of possible words
    output_words.sort()

    # Print each of the possible words
    for word in output_words:
        print("\t- " + word)

if __name__ == "__main__":
    main()