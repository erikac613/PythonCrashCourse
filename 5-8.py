usernames = ['bob37', 'woopsnerp', 'dagronald', 'admin', 'sunnybunny']
for username in usernames:
    if username == 'admin':
        print("Hello, admin. Would you like to see a status report?")
    else:
        print('Hello ' + username + ', thank you for logging in.')
