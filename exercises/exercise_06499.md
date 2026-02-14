## Exercise
Write a program that plays a game of hangman with the user. The program should randomly select a word and then allow the user to guess letters. After each guess, print out the updated word with correctly guessed letters filled in.

## Reference Solution
```python
import random

# List of words to choose from
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def hangman():
    # Select a random word from the list
    word = random.choice(words)
    word_length = len(word)

    # Create a list to store the guessed letters
    guessed = ['_'] * word_length
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(guessed))

    while '_' in guessed and tries > 0:
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

    if '_' not in guessed and tries > 0:
        print("Congratulations, you guessed the word!")
    else:
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
                
_ _ _ _ _ _
Please guess a letter or word: Good job, e is in the word!

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
_ _ e _ _ _
Please guess a letter or word: 
Traceback (most recent call last):
  File "/tmp/tmpepsvz6wx.py", line 133, in <module>
    hangman()
  File "/tmp/tmpepsvz6wx.py", line 22, in hangman
    guess = input("Please guess a letter or word: ").lower()
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
