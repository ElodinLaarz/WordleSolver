class WorldleAI:
  
  def __init__(self, dictionary, difficulty = 1, WORD_LENGTH = 5):

    self.WORD_LENGTH = WORD_LENGTH
    # a - z
    self.alphabet = [chr(x) for x in range(97, 123)]
    self.good_letters = [set(alphabet) for i in range(WORD_LENGTH)]

    # loads all possible words for all guesses
    self.dictionary = dictionary
    
    # word_space is the current collection of possible
    # words for the current word
    self.word_space = dictionary
    self.sort_word_space()

    self.difficulty = difficulty


  def guess_word(self):
    if self.word_space:
      return self.word_space[0]


  # Send along some colors, e.g. BYGGB (B = Black, G = Green, Y = Yellow)
  # that describes the given word
  def guessed_word_colors(self, colors, word = self.guess_word()):

    cur_yellow_letters = set()

    for index, color in enumerate(colors):
        if color == 'G':
            self.good_letters[index] = set([word[index]])
        elif color == 'Y':
            cur_yellow_letters.add(word[index])
            self.good_letters[index].remove(word[index])
        else:
            if word[index] not in cur_yellow_letters:
              for i in range(len(self.good_letters)):
                  if len(self.good_letters[i]) != 1:
                      if word[index] in self.good_letters[i]:
                          self.good_letters[i].remove(word[index])

    self.word_space = list(filter(lambda x: all([x[i] in self.good_letters[i] 
                        for i in range(len(self.good_letters))]+
                        [letter in x for letter in cur_yellow_letters]), self.word_space))
    self.sort_word_space()

  # Call this when the word is correct!
  def correct(self):
    self.word_space = self.dictionary
    self.sort_word_space()
    self.good_letters = [set(alphabet) for i in range(WORD_LENGTH)]

  # Choosing how to sort will be based upon difficulty 

  def sort_word_space(self):
    self.word_space.sort(key = self.word_score, reverse = True)

  # Helps sort the words

  def word_score(self, word):
    letter_scores = {}
    for letter in alphabet:
      letter_scores[letter] = 0
    
    for word in self.word_space:
      for letter in word:
        letter_scores[letter] += 1
    
    return sum([letter_scores[letter] for letter in word])
