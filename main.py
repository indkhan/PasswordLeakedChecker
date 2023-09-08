import requests
import hashlib

text = "12345678"
password = hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
print(password)

leak = requests.get(f"https://api.pwnedpasswords.com/range/{password[:5]}")
numandpass = leak.text
lines = numandpass.splitlines()
print(numandpass)


for line in lines: 
    che = line.split(":")
    if password[5:] == che[0]:
        print(text , 'is there ',che[1],"times")


