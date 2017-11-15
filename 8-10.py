def show_magicians(magicians):
    for magician in magicians:
        print("Hello, " + magician.title() + "!")


def make_great(magicians):
    for i in xrange(len(magicians)):
        magicians[i] = '{} the Great'.format(magicians[i].title())


magicians_names = ['quentin', 'alice', 'penny', 'elliot', 'margot', 'julia']
make_great(magicians_names)
print(magicians_names)
