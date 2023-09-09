import requests
import hashlib

password = input("Enter your password: ")
hashedpassword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


lst = []
def get_password():
    leak = requests.get(f"https://api.pwnedpasswords.com/range/{hashedpassword[:5]}")
    numandpass = leak.text
    lines = numandpass.splitlines()
    for line in lines:
        lst.append(line)

get_password()


def times():
    for line in lst: 
        che = line.split(":")
        if hashedpassword[5:] == che[0]:
            return(f"Your password {password} has been leaked {che[1]} times.")

leak = times()
if leak:
    print(leak)
else:
    print(f"Your password {password} has not been leaked")