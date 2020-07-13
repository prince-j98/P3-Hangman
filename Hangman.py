import random

print("Welcome to Hangman! \nGuess the word correctly before the figure forms (max: 6 tries) \n")

hangman = ["      ________ ", "     |        |"]

hangman_body = (
    "    / \       |",
    "    \ /       |",
    "   __|__      |",
    "  /     \     |",
    "     |        |",
    "    / \       |"
)

# read sowpods file and converts each word/line into one element of a long list
words = open("sowpods.txt", "r")
words_list = list(words)

# pick one word at random
rand_word = words_list[random.randint(1, len(words_list))]


rand_list = list(rand_word)

# display empty spaces equivalent to length of the word
empty_word = ""
while len(empty_word) < (len(rand_word) - 1):
    empty_word = empty_word + "_"

print("Extracting your first word. The word has " + str(len(empty_word)) + " letters! ")
print("Word: " + empty_word)

empty_list = list(empty_word)
print("\n")

mistakes = 0
max_mistakes = 6

# scanning the guess in the selected word and replacing it if right, or incrementing no. of mistakes if guess is wrong
def scan():
    global mistakes
    global max_mistakes
    scan_guess = 0
    while scan_guess < len(empty_word) + 1:
        if rand_list[scan_guess] == guess:
            empty_list[scan_guess] = rand_list[scan_guess]
        scan_guess += 1

    if empty_list.count(guess) == 0:
        mistakes = mistakes + 1
        print("Oh Oh! Wrong Guess!")
        print("You have " + str(max_mistakes - mistakes) + " wrong guess(es) remaining.")
        if mistakes == max_mistakes:
            fig()
            print("Game over. You have exhausted your chances.")
            print("The correct word was " + rand_word)
            exit()
    else:
        print("Great guess!")
        print("You still have " + str(max_mistakes - mistakes) + " wrong guesses remaining.")

# forming the hangman figure
def fig():
    global mistakes
    global max_mistakes
    hangman_loading = 0
    while len(hangman) > hangman_loading:
        print(hangman[hangman_loading])
        hangman_loading += 1
    if mistakes > 0:
        add = 0
        while add < mistakes:
            print(hangman_body[add])
            add += 1


# storing the guesses
guess_list = [" "]
# Running the functions
while mistakes <= max_mistakes:
        # ask for user's guess
    guess = input("Please enter your guess (only alphabets): ").upper()

    if len(guess) != 1:                         # length of input should not be more than 1 letter
        print("Please enter only one alphabet digit! \n")
        continue
    if guess_list.count(guess) != 0:            # guesses should not be repeated
        print("Please enter a new letter. This has been guessed before.\n")
        continue
    if guess.isdigit():                         # no digit inputs allowed
        print("You entered a number. Only alphabets are allowed. \n")
        continue
    guess_list.extend(guess)


    scan()
    print("Word: " + ''.join(empty_list) + "\n")
    fig()
    print("\n")
    if empty_list.count("_") == 0:
        print("Congratulations!")
        print("You guessed the word correctly: " + str(rand_word))
        break
