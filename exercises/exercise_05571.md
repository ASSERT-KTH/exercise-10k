## Exercise
Create a program that generates a random word and allows the user to guess letters, providing feedback if the letter is in the word or not.

## Reference Solution
```python
import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

def game():
    # Choose a random word from the list
    word_to_guess = random.choice(word_list)
    word_length = len(word_to_guess)

    # Initialize display with underscores
    display = ['_'] * word_length
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(display))
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word_to_guess:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_to_guess)
                indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
                for index in indices:
                    display[index] = guess
        elif len(guess) == word_length and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word_to_guess:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                display = list(guess)
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(' '.join(display))
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was " + word_to_guess)

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
    game()
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
                
_ _ _ _ _


Please guess a letter or word: Not a valid guess.

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                
_ _ _ _ _


Please guess a letter or word: 
Traceback (most recent call last):
  File "/tmp/tmpny7vdd2v.py", line 137, in <module>
    game()
  File "/tmp/tmpny7vdd2v.py", line 24, in game
    guess = input("Please guess a letter or word: ").lower()
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
