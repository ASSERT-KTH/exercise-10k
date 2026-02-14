## Exercise
Write a program that uses a for loop to play a game of Hangman with the user. The program should think of a word, and the user should try to guess the word by suggesting letters.

## Reference Solution
```python
import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def hangman():
    # Choose a random word from the list
    word = random.choice(word_list)
    word_length = len(word)

    # Initialize a list to store the guessed letters
    guessed = ['_'] * word_length
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(guessed))
    print("\n")

    for i in range(tries):
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
                    guessed[index] = guess
        elif len(guess) == word_length and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = list(guess)
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(' '.join(guessed))
        print("\n")
        if '_' not in guessed:
            print("Congratulations, you guessed the word!")
            break
    if '_' in guessed:
        print("Sorry, you ran out of tries. The word was " + word)

def display_hangman(tries):
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

if __name__ == "__main__":
    hangman()
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
                
_ _ _ _


Please guess a letter or word: Good job, e is in the word!

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
_ _ _ e


Please guess a letter or word: Good job, a is in the word!

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
_ a _ e


Please guess a letter or word: Good job, t is in the word!

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
_ a t e


Please guess a letter or word: 
Traceback (most recent call last):
  File "/tmp/tmpj5gilo63.py", line 134, in <module>
    hangman()
  File "/tmp/tmpj5gilo63.py", line 23, in hangman
    guess = input("Please guess a letter or word: ").lower()
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
