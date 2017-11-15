current_users = ['bob37', 'woopsnerp', 'dagronald', 'admin', 'sunnybunny']
new_users = ['admin', 'cyberface', 'BOB37', 'xxangelxx', 'c u c k']

for user in new_users:
    available = True
    for old_user in current_users:
        if user.lower() == old_user.lower():
            available = False
    if(available):
        print(user + " is available.")
    else:
        print("Please enter a new username.")






#for username in usernames:
#    if username == 'admin':
#        print("Hello, admin. Would you like to see a status report?")
#    else:
#        print('Hello ' + username + ', thank you for logging in.')
