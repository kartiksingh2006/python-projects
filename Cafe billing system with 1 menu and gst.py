print("welcome to our cafe!! 😊🙏🏻")
print("pizza :40\nburger :30\nsalad :20\npasta :50\nsushi :60\nnoodles :50")

menu = {
    "pizza": 40,
    "burger": 30,
    "salad": 20,
    "pasta": 50,
    "sushi": 60,
    "noodles": 50
}

order_total = 0

while True:
    item = input("enter the name of the item you want to order : ")
    if item in menu:
        order_total += menu[item]
        print(f"your item {item} has been added to your cart !!")
    else:
        print(f"sorry, we dont have that item in our menu !!")

    another_order = input("do you want to add another item ? ")
    if another_order.lower() != "yes":
        break
sp=float(order_total)
gst=float(9)
tax=(gst/100)*sp
print("-------------Invoice-------------")
print("item name-------------Price")
print("Product X-------------",sp,"Rs")
print("GST%------------------",gst,"%")
print("Total GST tax---------",tax,"Rs")
print("CGST%-----------------",gst/2,"%")
print("CGST Tax--------------",tax/2,"Rs")
print("SGST%-----------------",gst/2,"%")
print("SGST Tax--------------",tax/2,"Rs")
print("Total Amount----------",sp+tax,"Rs")



# print(f"your total order is : {order_total}")