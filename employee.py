class Employee(object):
    """Records name and annual salary of a given employee."""
    def __init__(first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        raise = self.give_raise
