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

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation, login_attempts):
        super(Admin, self).__init__(first_name, last_name, age, location, occupation, login_attempts)
        self.privelages = ['can ban users', 'can add post', 'can delete post']

    def show_privelages(self):
        print("The administrator can do the following: " + str(self.privelages))

user_admin = Admin('erika', 'carpenter', '29', 'decatur', 'archaeologist', 3)

user_admin.show_privelages()
