import random

print('*********************************')
print('----- Welcome to Hangman! -------')
print('*********************************')

dictionary = ['algorithm', 'variable', 'function', 'loop', 'debugging', 'syntax', 'class', 'recursion', 'inheritance']
new_list = []

class Word():

  # constructor
  def __init__(self):

    self.identity = "word"
    self.split_word = []
    self.word = random.choice(dictionary)
    self.printed_word = ' '
    self.guesses = 0

  
    # split the word up into a list of dictionaries with 2 attributes:
    # the letter and a boolean representing whether or not it has been guessed
  def split_chosen_word(self):
    for letter in self.word:
      split_word = {'letter': letter, 'guessed': False}
      new_list.append(split_word)
    print(new_list)
    return new_list
  
  # print undescores for the letters that are 'guessed'= False and actual letters for 'guessed'= True
  def print_word(self):
    for letter in new_list:
      if letter['guessed']:
        self.printed_word += [letter['letter']]
      else:
        self.printed_word += '_ '
    print(f' printed_word in print_word: {self.printed_word}')

  # swap underscores with letters if the letters have been guessed
  def check_letter(self, input_letter ):
    letter_guessed = False
    for letter in self.split_word:
      if letter['letter'] == input_letter:
        letter_guessed = True
        letter['guessed'] = True
      else:
        letter_guessed = False
        letter['guessed'] = False
    return letter_guessed
  
  # loop through all letters in the word and return True if letters have been guessed
  def is_word_guessed(self):
    for letter in self.split_word:
      if letter['guessed']:
        return True
      else:
        return False
  
  # join guessed letters back to a word
  def unsplit_word(self):
      return ''.join(letter['letter'] for letter in self.split_word)




  

word = Word()
word.split_chosen_word()
word.print_word()


user_input = input("Enter a letter: ")
letter_guessed = word.check_letter(user_input)




# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop
