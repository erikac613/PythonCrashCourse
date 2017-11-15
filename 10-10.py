def common_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except IOError:
        pass
    else:
        words = contents.split()
        word_count = words.count('the')
        print(word_count)

filename = 'dracula.txt'
common_words(filename)

filename = 'jane_eyre.txt'
common_words(filename)
