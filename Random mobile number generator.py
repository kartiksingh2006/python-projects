#firt we will import random number\alphabets .
import random
#then we will write values we need for generating a number .
charactervalues = '0123456789'
#noe we will define number length of how many numbers of number we need .
num_len = 10
number = ""
for i in range(num_len):
    number += random.choice(charactervalues)

print("Your random mobile number is :", number)

b = "Thank you for contacting us!!"
print(b.upper())
