import random
import string


words = ['python', 'java', 'swift', 'javascript']
word = random.choice(words)
print(*'HANGMAN')


def menu(won, lost):
    user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').lower()
    if user_choice == 'play':
        if game() == 'won':
            won += 1
        else:
            lost += 1
        menu(won, lost)

    elif user_choice == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lost} times.')
        menu(won, lost)

    elif user_choice == 'exit':
        print('Thanks for playing!')
        exit()

    else:
        menu(won, lost)


def game():
    attempts = 8
    guess = ['-'] * len(word)
    guess_set = set()

    while attempts > 0 and ''.join(guess) != word:
        print()
        print(''.join(guess))
        letter = input('Input a letter: ')

        if len(letter) != 1:
            print('Please, input a single letter.')

        elif letter not in string.ascii_lowercase:
            print('Please, enter a lowercase letter from the English alphabet.')

        else:
            if letter in guess_set:
                print("You've already guessed this letter.")
                continue

            guess_set.add(letter)

            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guess[i] = letter
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1

    if ''.join(guess) != word:
        print('\nYou lost!')
        return 'lost'
    else:
        print(f'You guessed the word {word}!\nYou survived!')
        return 'won'


if __name__ == '__main__':
    menu(0, 0)
