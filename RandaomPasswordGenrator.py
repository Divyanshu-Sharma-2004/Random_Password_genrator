'''
import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
pass_len = int(input("Enter your desired password length : "))


password = ""

for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is : ",password)
'''

# List comprehension technique

import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
pass_len = int(input("Enter your desired password length : "))

password = "".join([random.choice(charValues) for i in range(pass_len)])   # ("".join() is concatinate the list)
print("your random password is :",password)