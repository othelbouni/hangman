import random

print("H A N G M A N")
words_list = ['python', 'java', 'swift', 'javascript']
wins = 0
losses = 0

while True:
    computer_choice = random.choice(words_list)
    player_letters = []
    word = set(computer_choice)
    lives = 8
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    choice = input()
    if choice == "play":
        while True:
            print()
            for letter in computer_choice:
                if letter in player_letters:
                    print(letter, end='')
                else:
                    print('-', end='')
            print()
            player_letter = input("Input a letter: ")
            if len(player_letter) != 1:
                print("Please, input a single letter.")
                continue
            if not player_letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if player_letter.isupper():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if player_letter in player_letters:
                print("You've already guessed this letter.")
                continue
            player_letters.append(player_letter)
            if player_letter in word:
                word.remove(player_letter)
                if not word:
                    print("You guessed the word {}!".format(computer_choice))
                    print("You survived!")
                    wins += 1
                    break
            else:
                lives -= 1
                print("That letter doesn't appear in the word. You have {} lives left.".format(lives))
                if lives == 0:
                    print("You lost! The word was {}.".format(computer_choice))
                    losses += 1
                    break
    elif choice == "results":
        print("You won: {} times".format(wins))
        print("You lost: {} times".format(losses))
    elif choice == "exit":
        break
    else:
        continue
