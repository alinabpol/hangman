import random

print("*********************************")
print("----- Welcome to Hangman! -------")
print("*********************************")

dictionary = [
    "algorithm",
    "variable",
    "function",
    "loop",
    "debugging",
    "syntax",
    "class",
    "recursion",
    "inheritance",
]


class Word:

    # constructor
    def __init__(self):

        self.identity = "word"
        self.split_word = []
        self.word = random.choice(dictionary)
        self.guesses = 0

    # split the word up into a list of dictionaries with 2 attributes:
    # the letter and a boolean representing whether or not it has been guessed
    def split_chosen_word(self):
        for letter in self.word:
            split_letter = {"letter": letter, "guessed": False}
            self.split_word.append(split_letter)
        print(self.split_word)
        return self.split_word

    # print undescores for the letters that are 'guessed'= False and actual letters for 'guessed'= True
    def print_word(self):
        printed_word = ""
        for letter in self.split_word:
            if letter["guessed"]:
                printed_word += letter["letter"]
            else:
                printed_word += "_ "
        print(f"Word: {printed_word}")

    # swap underscores with letters if the letters have been guessed
    def check_letter(self, input_letter):
        letter_guessed = False
        for letter in self.split_word:
            if letter["letter"] == input_letter:
                letter_guessed = True
                letter["guessed"] = True
        return letter_guessed

    # loop through all letters in the word and return True if letters have been guessed
    def is_word_guessed(self):
        for letter in self.split_word:
            if not letter['guessed']:
                return False
        return True

class Game:

    # constructor
    def __init__(self):
        self.word = Word()
        self.guesses = 8
        self.letters_guessed = []

    # run methods from word class to split a word to dict and print underscores
    def start(self):
        self.word.split_chosen_word()
        self.word.print_word()

    # cverify wether user input is valid
    # check if the letter appears in teh word, and if so append it to the letters_guessed list. if user_input is wrond decrement guesses value by 1
    def play_game(self):
        while self.guesses > 0:
            user_input = input("Enter a letter: ").lower()
            if len(user_input) != 1:
                print("********* Please enter a single letter *********")
            elif user_input.isdigit():
                print("********** Only letters are allowed ************")
            elif user_input.lower() in self.letters_guessed:
                print("**** This letter has been already guessed! *****")
            elif self.word.check_letter(user_input):
                self.letters_guessed.append(user_input)
                print("----------- You've found the letter! ------------")      
            else:
                self.guesses -= 1
                print(f"This is wrong! You have {self.guesses} guesses left!")
            self.word.print_word()

            if self.word.is_word_guessed():
                print("-------------------------------------------------")
                print("***** Congrats, you have guessed the word! ******")
                print("-------------------------------------------------")
                break

        if self.guesses == 0:
            print("=================================================")
            print("----------------- Game over! --------------------")
            print("=================================================")


game = Game()
game.start()
game.play_game()