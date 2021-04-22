
import random
from hangman_words import word_list


HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

name = input("What is your name? ").capitalize()


# Function Picks a random word from list
# Returns a random word from word_list in UPPERCASE
def get_word():
    word = random.choice(word_list)
    return word.upper()


# Function defines the game

def play(word):
    # Shows the word as a series of underscores
    word_completion = "_" * len(word)
    # Initialise variable guessed to false
    guessed = False
    # Create list to hold letters the user guesses
    guessed_letters = []
    # Create list to hold words the user guesses
    guessed_words = []
    # How many guesses the user has initially
    tries = 7
    print(f"Hello {name}. Let's start the Hangman Game!" "\n")
    print(word_completion, "\n")

    # Tell user how long their word is
    length_of_word = len(word)
    print(f"{name} your word is {length_of_word} characters long.")

    # Creating a while loop to run until word is guessed or user loses
    while not guessed and tries > 0:
        # Ask user to input letter and show them previous guesses
        print("These are the letters you have already guessed:""\n" + "-".join(guessed_letters))
        guess: str = input("Please guess a letter or word: ").upper()

        # If user guesses a single letter
        if len(guess) == 1 and guess.isalpha():

            # If user guess has already been guessed
            if guess in guessed_letters:
                print(f"{guess} has already been guessed")
                # This prints hangman pic corresponding to number of incorrect guesses
                print(HANGMAN_PICS[7 - tries])

            # If user guess is incorrect
            elif guess not in word:
                print(guess, "is not in the word.")
                # This prints hangman pic corresponding to number of incorrect guesses
                print(HANGMAN_PICS[7-tries])
                tries -= 1
                guessed_letters.append(guess)
                print(f"{name} you have {tries} lives remaining")

            # If user guess is correct
            else:
                print(f"Yes! {guess} is in the word")
                # This prints hangman pic corresponding to number of incorrect guesses
                print(HANGMAN_PICS[7 - tries])
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # Create new iterable object from word
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # for loop
                for index in indices:
                    # To replace all underscores at the indexed point with guess
                    word_as_list[index] = guess
                # UPDATE word_completion
                word_completion = "".join(word_as_list)
                # If there are no underscores left in the entire word the the word has been guessed
                if "_" not in word_completion:
                    guessed = True

        # If the user guesses the entire word
        elif len(guess) == len(word) and guess.isalpha():

            # If the word has already been guessed
            if guess in guessed_words:
                print(f"You have already guessed {guess}")
                # This prints hangman pic corresponding to number of incorrect guesses
                print(HANGMAN_PICS[7 - tries])

            # If the word is incorrect
            elif guess != word:
                print(f"{guess} is not the word")
                # This prints hangman pic corresponding to number of incorrect guesses
                print(HANGMAN_PICS[7 - tries])
                tries -= 1
                guessed_words.append(guess)
                print(f"{name} you have {tries} lives remaining")
            # If the word is correct
            else:
                guessed = True
                word_completion = word

        # If the user does not guess a single letter or a word with the correct length
        else:
            print("That is not a valid guess.")
        print(word_completion)
        print("\n")

    # If user guesses the word
    if guessed:
        print(f"Congratulations {name}! You guessed the word!")

    # If user runs out of tries
    else:
        print(f"Unluckeeeeeeeee {name}, you ran out of tries. The word was {word}")


# Show them the letters they have already picked
# Starting the game
def hangman():
    hang_word = get_word()
    play(hang_word)

    # Offer to play again
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        hang_word = get_word()
        play(hang_word)


if __name__ == "__main__":
    hangman()
