def show_magicians(magicians):
    for magician in magicians:
        print("Hello, " + magician.title() + "!")


def make_great(magicians):
    for magician in magicians:
        print(magician.title() + " the Great")



magicians_names = ['quentin', 'alice', 'penny', 'elliot', 'margot', 'julia']

great_magicians = make_great(magicians_names[:])

print(magicians_names)
print(great_magicians)
