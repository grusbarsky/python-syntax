def print_upper_words(words, letter):
    """print words with new line in all uppercase"""
    for word in words:
        if word.startswith(letter):
            caps_word = word.upper()
            print(caps_word)