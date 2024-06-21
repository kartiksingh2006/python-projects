#we will first write a greeting message 
a= ("welcome to our random password generetor service!! ")
print(a.upper())
#then import random and string
import random

import string
#define paswrod length
pass_len=12
#then add different cases , string , number and symbols.
charactervalues = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
# print(charactervalues)

password=""
for i in range(pass_len):
    password+= random.choice(charactervalues)

print(" your random password is : " , password )

b= ("thank you for contacting us!!")
print(b.upper())

