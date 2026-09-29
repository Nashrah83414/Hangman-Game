import random

# List of 5 predefined words
words = ["apple", "tiger", "house", "water", "chair"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_incorrect_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_incorrect_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the entire word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get a letter from the player
    guess = input("Enter a letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Incorrect guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

# If the player runs out of guesses
if incorrect_guesses == max_incorrect_guesses:
    print("\n💀 Game over!")
    print("The word was:", word)