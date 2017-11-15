class User(object):
    def __init__(self, first_name, last_name, age, location, occupation, login_attempts):
        """Initialize info on a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = login_attempts

    def describe_user(self):
        """Prints a summary of user's information."""
        print("\n" + self.first_name.title() + " " + self.last_name.title() + " is a " + str(self.age) + "-year-old " + self.occupation + " from " + self.location.title() + ".")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print("Hello, " + self.first_name.title() + "! Thanks for adding your information.")

    def increment_login_attempts(self):
        """increments value of login_attempts by 1."""
        self.login_attempts += 1
        print("You have attempted to log in " + str(self.login_attempts) + " times.")

    def reset_login_attempts(self):
        """resets value of login_attempts to 0."""
        self.login_attempts = 0
        print("You have reset your login attempts.")

user_erika = User('erika', 'carpenter', '29', 'decatur', 'archaeologist', 3)
user_george = User('george', 'granberry', '25', 'atlanta', 'computer programmer', 1)
user_sarah = User('sarah', 'dickey', '29', 'oxford', 'lawyer', 4)

user_erika.increment_login_attempts()
user_erika.reset_login_attempts()
