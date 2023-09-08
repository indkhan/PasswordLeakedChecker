import requests
import hashlib

text = "Hello, world!"
password = hashlib.sha1(text.encode('utf-8')).hexdigest()
print(password)