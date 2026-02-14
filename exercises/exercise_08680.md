## Exercise
Write a program that plays Hangman with the user, using multiple words and keeping track of the score.

## Reference Solution
```python
import random

# List of words to use in the game
words = ["apple", "banana", "cherry", "date", "elderberry"]

def hangman(word):
    """
    Play a round of Hangman with the given word.

    Args:
    word (str): The word to use for this round.

    Returns:
    int: The score for this round (1 for win, 0 for loss).
    """
    word_list = ["_"] * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_list)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word)
                indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
                for index in indices:
                    word_list[index] = guess
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_list = list(word)
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_list)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word!")
        return 1
    else:
        print("Sorry, you ran out of tries. The word was " + word)
        return 0

def display_hangman(tries):
    """
    Display the current state of the Hangman figure.

    Args:
    tries (int): The number of tries remaining.

    Returns:
    str: The Hangman figure as a string.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    score = 0
    play_again = "y"
    while play_again.lower() == "y":
        word = random.choice(words)
        score += hangman(word)
        print("Your current score is:", score)
        play_again = input("Would you like to play again? (y/n): ")
    print("Thanks for playing! Your final score is:", score)

if __name__ == "__main__":
    main()
```

## Generated Output
```
Let's play Hangman!

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
['_', '_', '_', '_', '_', '_']


Please guess a letter or word: a is not in the word.

                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                
['_', '_', '_', '_', '_', '_']


Please guess a letter or word: 
Traceback (most recent call last):
  File "/tmp/tmpsfxp3ey9.py", line 162, in <module>
    main()
  File "/tmp/tmpsfxp3ey9.py", line 156, in main
    score += hangman(word)
  File "/tmp/tmpsfxp3ey9.py", line 28, in hangman
    guess = input("Please guess a letter or word: ").lower()
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
