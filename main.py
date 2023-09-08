import requests
import hashlib

text = "1234565545"
password = hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
print(password)

leak = requests.get(f"https://api.pwnedpasswords.com/range/{password[:5]}")
print(leak.text)