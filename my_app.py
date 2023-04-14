import streamlit as st
import random

# Set up the game
def setup():
    st.write("# Guess the number!")
    st.write("I'm thinking of a number between 1 and 100.")
    st.write("Can you guess what it is?")
    return random.randint(1, 100)

# Main game loop
def game():
    number = setup()
    guess = None
    num_guesses = 0

    while guess != number:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
        num_guesses += 1

        if guess < number:
            st.write("Too low, try again!")
        elif guess > number:
            st.write("Too high, try again!")
        else:
            st.write(f"Congratulations, you guessed it in {num_guesses} tries!")

# Start the game
game()



if __name__ == '__main__':
    app()


