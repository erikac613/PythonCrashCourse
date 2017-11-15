favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
friends = ['jen', 'tom', 'george', 'edward']

for name in friends:
    if name in favorite_languages.keys():
        print("Hi " + name.title() + ", thanks for taking the poll!")
    else:
        print(name.title() + ", you should take our poll!")
