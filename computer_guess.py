# Pass in a guess

secret_word = ''

def color_word(word_guessed):
    """
    word_guessed : str - the guess to be colored.

    The rules for coloring following the following rules:
    1. If the letter is in the correct position, the letter gets
    colored green.
    2. If the letter is in the word but is somewhere else in the
    word and has not been colored yellow or green already, then
    we color it yellow.
    3. Otherwise, the letter is colored black.

    Useful examples:
    Throughout, the secret word is assumed to be 'BROOM':

    'ANKLE' would be colored 'BBBBB'
    'BANDS' would be colored 'GBBBB'
    'BABLE' would be colored 'GBBBB'
    'RIGHT' would be colored 'YBBBB'
    'MUMMY' would be colored 'YBBBB'
    'OBOES' would be colored 'YYGBB'

    Return :
    colors : str - A sequence of colors, representing
    the guess. e.g. 'BBYBG' = 'Black Black Yellow Black Green'
    """
    return