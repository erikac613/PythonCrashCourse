from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation, login_attempts):
        super(Admin, self).__init__(first_name, last_name, age, location, occupation, login_attempts)
        self.privelages = Privelages()

class Privelages():
    def __init__(self):
        self.privelages = ['can ban users', 'can add post', 'can delete post']

    def show_privelages(self):
        print("The administrator can do the following: " + str(self.privelages))
