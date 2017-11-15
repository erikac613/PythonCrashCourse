class User(object):
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize info on a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """Prints a summary of user's information."""
        print("\n" + self.first_name.title() + " " + self.last_name.title() + " is a " + str(self.age) + "-year-old " + self.occupation + " from " + self.location.title() + ".")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print("Hello, " + self.first_name.title() + "! Thanks for adding your information.")

user_erika = User('erika', 'carpenter', '29', 'decatur', 'archaeologist')
user_george = User('george', 'granberry', '25', 'atlanta', 'computer programmer')
user_sarah = User('sarah', 'dickey', '29', 'oxford', 'lawyer')

user_erika.describe_user()
user_erika.greet_user()

user_george.describe_user()
user_george.greet_user()

user_sarah.describe_user()
user_sarah.greet_user()
