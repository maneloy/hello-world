# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"
NUM_GUESSES = 8

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

def hangman():
    """Main function of the hangman program. Starts and carries out a game of hangman."""
    
    word = choose_word(wordlist)
    letters_entered = list()
    letter_entered = ""
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    word_displayed = ""
    won = False
    guesses = NUM_GUESSES
    
    print()
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(word)))
    print("____________________________")
    
    while (not won):
        print("You have {} guesses left.".format(guesses))
        print("Available letters: " + available_letters)
        
        letter_entered = input("Please guess a letter: ")       # Take letter from user
        while (not letter_entered.isalpha()):
            letter_entered = input("You must enter a letter: ")            
        letter_entered = letter_entered.lower()        
        letters_entered.append(letter_entered)
        
        if (letter_entered in word):                            # See if correct or not
            print("Good guess: ", end='')
        else:
            print("Oops! That letter is not in my word: ", end='')
            guesses -= 1
            
        for letter in word:                                     # Show user current state of game
            if letter in letters_entered:
                word_displayed += letter
            else:
                word_displayed += " _ "
        print(word_displayed)

        if (guesses == 0):                                      # Is the user out of guesses?
            print("Sorry, you ran out of guesses. Better luck next time!")
            print("The word was: " + word)
            return 0
        
        won = True                                              # Check if user has won
        for letter in word:
            if not (letter in letters_entered):
                won = False
                break
            
        word_displayed = ""                                     # Refresh available letters and reinitialize the state display.
        available_letters = ""
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if not (letter in letters_entered):
                available_letters += letter

        print("____________________________")
        
    print("Congratulations, you won!")
    return 0

hangman()
        
            
        
        
