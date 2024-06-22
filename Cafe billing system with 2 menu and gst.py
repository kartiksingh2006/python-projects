print("welcome to our cafe!! 😊🙏🏻")
print("here is our food list")
print("pizza :40\nburger :30\nsalad :20\npasta :50\nsushi :60\nnoodles :50")
print("here is our fruits list")
print("pumpkin :40\npapaya :30\nkiwi :20\nmango :50\napple :60\ngrape :50")

menu1 = {
    "pizza": 40,
    "burger": 30,
    "salad": 20,
    "pasta": 50,
    "sushi": 60,
    "noodles": 50
}
menu2 = {
    "pumpkin": 40,
    "papaya": 30,
    "kiwi": 20,
    "mango": 50,
    "apple": 60,
    "grape": 50
}

order_total_food = 0
order_total_fruit = 0

while True:
    item = input("enter the name of the food you want to order : ")
    if item in menu1:
        order_total_food += menu1[item]
        print(f"your item {item} has been added to your cart !!")
    else:
        print(f"sorry, we dont have that item in our menu !!")

    another_order = input("do you want to add another item ? ")
    if another_order.lower() != "yes":
        break

while True:
    item = input("enter the name of the fruit you want to order : ")
    if item in menu2:
        order_total_fruit += menu2[item]
        print(f"your item {item} has been added to your cart !!")
    else:
        print(f"sorry, we dont have that item in our menu !!")

    another_order = input("do you want to add another item ? ")
    if another_order.lower() != "yes":
        break

order_total = order_total_food + order_total_fruit

if order_total_food > 0:
    gst_food = 9
else:
    gst_fruit = 8

if order_total_fruit > 0:
    gst_fruit = 8
else:
    gst_food = 9

gst = (gst_food + gst_fruit) / 2

sp = float(order_total)

tax = (gst / 100) * sp

print("-------------Invoice-------------")
print("Item Name-------------Price")
print("Product X-------------", sp, "Rs")
print("GST%------------------", gst, "%")
print("Total GST tax---------", tax, "Rs")
print("CGST%-----------------", gst / 2, "%")
print("CGST Tax--------------", tax / 2, "Rs")
print("SGST%-----------------", gst / 2, "%")
print("SGST Tax--------------", tax / 2, "Rs")
print("Total Amount----------", sp + tax, "Rs")
