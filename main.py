import random
from words import listOfWords


def get_word():
    answer = random.choice(listOfWords)
    return answer

def play(answer):
    fillInBlacks = "_" * len(answer)
    correct = False
    correct_letters = []
    tries = 6

    print("Hangman Start!")
    print(hangmanPicture(tries))
    print(fillInBlacks)

    while not correct and tries > 0:
        guess = input("\nPlease guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in correct_letters:
                print("You already guessed the letter", guess)
            elif guess not in answer:
                print(guess, "is not in the word.")
                tries -= 1
                correct_letters.append(guess)
            else:
                print(guess, "is in the word")
                correct_letters.append(guess)
                word_as_list = list(fillInBlacks)

                #?
                indices = [i for i, letter in enumerate(answer) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                fillInBlacks = "".join(word_as_list)
                if "_" not in fillInBlacks:
                    correct = True
                #?
        else:
            print("Wrong input")

        print(hangmanPicture(tries))
        print(fillInBlacks)

    if correct:
        print("You guessed the correct word!")
    else:
        print("No more tires. The word was " + answer + ". Try again!")

def hangmanPicture(tries):
    stages = [
        "_________\n"
        "|	|\n"
        "|   O\n"
        "|  \|/\n"
        "|   |\n"
        "|  / \\\n"
        "|________\n",

        "_________\n"
        "|	|\n"
        "|   O\n"
        "|  \|\n"
        "|   |\n"
        "|  / \\\n"
        "|________\n",

        "_________\n"
        "|	|\n"
        "|   O\n"
        "|   |\n"
        "|   |\n"
        "|  / \\\n"
        "|________\n",

        "_________\n"
        "|	|\n"
        "|   O\n"
        "|   |\n"
        "|   |\n"
        "|  /\n"
        "|________\n",

        "_________\n"
        "|	|\n"
        "|   O\n"
        "|   |\n"
        "|   |\n"
        "|\n"
        "|________\n",

        "_________\n"
        "|	|\n"
        "|   O\n"
        "|   |\n"
        "| \n"
        "|\n"
        "|________\n",

        "_________\n"
        "|	 |\n"
        "|\n"
        "|\n"
        "|\n"
        "|\n"
        "|________\n"]
    return stages[tries]

def main():
    word = get_word()
    play(word)

main()

