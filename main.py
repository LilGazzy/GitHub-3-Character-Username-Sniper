import requests

# generate all possible 3 letter combinations of letters in the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
usernames = [a + b + c for a in alphabet for b in alphabet for c in alphabet]

# loop through each username and check if it exists on GitHub
available_usernames = []
for i, username in enumerate(usernames):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 404: # username is available
        available_usernames.append(username)
        print(f'[{i+1}/{len(usernames)}] {username} is available!')
    else: # username is not available
        print(f'[{i+1}/{len(usernames)}] {username} is not available.')

# print available usernames
print(f'\nAvailable usernames: {available_usernames}')

