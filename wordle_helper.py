#import nltk
#nltk.download()
print("Downloading word list...")
from nltk.corpus import words
import re

def main():
    # Get a list of every word in English language and reduce it to only 5-letter words
    wordle_words = [word for word in words.words() if len(word) == 5]

    # Sort the list alphabetically
    wordle_words.sort()

    # Player instructions
    print("Ready\n")
    print("Instructions:\n")
    print("Enter the words you've tried in Wordle, with each letter seperated by a space")
    print("For each GRAY letter, do not add any characters to the letter")
    print("For every YELLOW letter, surround the letter with \'-\' characters")
    print("\tExample: If the letter F was shown in YELLOW, enter -F-")
    print("For every GREEN letter, surround the letter with \'*\' characters")
    print("\tExample: If the letter A was shown in GREEN, enter *A*")
    print("-------------------------------------------------------------------------------\n")
    input("Press enter to continue\n")

    # Get the number of words already tried by the user
    num_words = int(input("How many words have you tried in Wordle?\n"))

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

    # List to store all letters known to be in the word
    known_letters = []

    for num in range(num_words):
        # Get the words and their colour from the user
        user_input.append(input("Enter a word, remember above formatting:\n"))

        # Seperate the letters, using spaces as seperators
        formatted_input.append(user_input[-1].lower().split())

        # All Wordle words must be 5 letters
        if (len(formatted_input[-1]) != 5):
            print("**Your word was not 5 letters, try again**")
            exit()

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

            # GREEN letter
            elif (re.search("\*.\*", letter)):
                final_word[word.index(letter)] = []
                final_word[word.index(letter)].append(letter.replace("*", ""))
                green_letters[word.index(letter)] = letter.replace("*", "")
                known_letters.append(letter.replace("*", ""))

            # GRAY letter
            else:
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

    # Boolean used to store whether the word matches the conditions
    word_match = True

    # Print out all words that could be Wordle solutions
    for word in wordle_words:
        word_match = True
        for index in range(5):
            if ((word[index].lower() not in final_word[index])):
                word_match = False
                break
        if (word_match):
            # Make sure every YELLOW and GREEN letter encountered is found in the word
            for letter in known_letters:
                if (word.find(letter) == -1):
                    word_match = False
                    break
        # If all conditions have been met, add the word to the output list
        if (word_match):
            output_words.append(word)

    print("-------------------------------------------------------------------------------\n")
    print("Possible words:")
    for word in output_words:
        print("\t- " + word)

if __name__ == "__main__":
    main()