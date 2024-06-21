a= ("welcome to our random password generetor service!! ")
print(a.upper())

import random

import string

pass_len=12

charactervalues = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
# print(charactervalues)

password=""
for i in range(pass_len):
    password+= random.choice(charactervalues)

print(" your random password is : " , password )

b= ("thank you for contacting us!!")
print(b.upper())

