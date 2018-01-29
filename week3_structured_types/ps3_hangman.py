# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/shellytang/mycode/intro-cs-python/week3_structured_types/words.txt"


def loadWords():
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


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

# print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_copy = secretWord[:]
    for letter in secretWord_copy:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '_')
    return secretWord

# print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters = string.ascii_lowercase
    notGuessedLetters = ''
    for letter in allLetters:
        if letter not in lettersGuessed:
            notGuessedLetters += letter
    return notGuessedLetters

# print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))


def checkForUnique(lettersGuessed, current):
    '''
    lettersGuessed: list, what letters have been guessed so far
    current: string, letter that user has guessed
    returns: bool, true if letter has not already been guessed, or false if letter has already been guessed
    '''
    for letter in lettersGuessed:
        if current == letter:
            return False
    return True

# print(checkForUnique(['e', 'i', 'k', 'p', 'r', 's'], 'z'))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # initialLetters = string.ascii_lowercase
    wordLen = len(secretWord)
    lettersGuessed = []
    guessesLeft = 8
    available = getAvailableLetters(lettersGuessed)
    
    gameStatus = getGuessedWord(secretWord, lettersGuessed)

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(wordLen) + ' letters long.')
    # print('You have ' + str(guessesLeft) + ' left.')
    # print('Available letters  ' + available)
    
    while guessesLeft > 0:
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters  ' + available)
        currentGuess = input('Please guess a letter: ')
        if checkForUnique(lettersGuessed, currentGuess):
            lettersGuessed.append(currentGuess)
            result = getGuessedWord(secretWord, lettersGuessed)
            available = getAvailableLetters(lettersGuessed)
            if result == gameStatus:
                print('Oops! That letter is not in my word: ' + gameStatus)
                guessesLeft -= 1
            else:
                print('Good guess: ' + result)
                gameStatus = result
                if isWordGuessed(secretWord, lettersGuessed):
                    return('Congratulations, you won!')
        else: 
            print('Oops! You\'ve already guessed that letter: ' + gameStatus)
    
    return('Sorry, you ran out of guesses. The word was ' + secretWord + '.')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(hangman('secretWord'))


