# (24) Write a program that repeatedly asks the user to enter product names and prices.
# Store all of these in a dictionary whose keys are the product names and whose values are the price

products = {}

while True:
    keys = products.keys()
    product_name = input("Name of Product : ")
    if product_name.lower() == "done":
        print("All Items have been recorded")
        break
    price = input("Price of Product : ")
    if product_name not in keys and price.replace(".", "").isdigit():
        products.update({product_name: price})
    elif not price.replace(".", "").isdigit():
        print("Invalid Price Entered")
    else:
        print(
            product_name, "is already entered and has price =>", products[product_name]
        )
