import random


def play():
    end_of_game = False
    lives = 6
    word_list = ["mango", "apple", "banana", "grapes", "papaya", "pineapple", "peach", "strawberry"]
    chosen_word = random.choice(word_list)
    print("Hint!!    Word is a fruit name.")

    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")
    while not end_of_game:
        guess = input("Guess the word : ")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("You guess the wrong letter! Try again.")
            lives -= 1
            print(f"You have only {lives} chances left.")
            if lives == 0:
                end_of_game = True
                print("You Lose!\n Game Over!!")
        if "_" not in display:
            end_of_game = True
            print("You Won!\n Game Over!!")
        print(f" {''.join(display)}")
    choice = input("Do you want play again ? press Y for yes and N for no\n").lower()
    if choice == "y":
        play()
    else:
        print("You exited")


print("Welcome to the Word guess game.\n")
play()
