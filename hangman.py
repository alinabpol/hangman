import random
print('Welcome to Hangman!')

dictionary = ['apple', 'book', 'travel', 'boat', 'baloon', 'shoes']

class Word():

  
  def __init__(self):

    self.identity = "word"

  
    # this method will split the word up into a list of dictionaries with 2 attributes:
    # the letter/character, and a boolean representing whether or not it has been guessed
  def split_chosen_word(self):
    chosen_word = random.choice(dictionary)
    new_list = []
    for letter in chosen_word:
      split_word = {'letter': letter, 'guessed': False}
      new_list.append(split_word)
    print(new_list)
    return new_list
  
  # ...other methods here... (refer back to JS hangman for ideas -- may not translate exactly, but
  # should be close enough)
  
word = Word()
word.split_chosen_word()




# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop
