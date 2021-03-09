from requests import Request,Session
import requests
from bs4 import BeautifulSoup
import hashlib

s = requests.Session()
url = "http://206.189.121.131:31678/"


pag = s.get(url)

soup = BeautifulSoup(pag.text,'html.parser')

hash = soup.find('h3')
hash_string = hash.text.strip()
hashed_string = hashlib.md5(hash_string.encode('utf-8'))
hashed_real = hashed_string.hexdigest()


data = {'hash':hashed_real}
post = s.post(url=url,data = data)



print('String was: {}'.format(hash_string))
print('Md5 hashed string is: {}'.format(hashed_string.hexdigest()))
print(post.text)







