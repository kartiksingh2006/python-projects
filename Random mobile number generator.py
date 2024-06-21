
import random

charactervalues = '0123456789'

num_len = 10
number = ""
for i in range(num_len):
    number += random.choice(charactervalues)

print("Your random mobile number is :", number)

b = "Thank you for contacting us!!"
print(b.upper())