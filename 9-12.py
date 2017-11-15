from user import User
from admin_privelages import Admin, Privelages

user_admin = Admin('erika', 'carpenter', '29', 'decatur', 'archaeologist', 3)

user_admin.privelages.show_privelages()
