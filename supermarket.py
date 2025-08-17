

#Predefined list of items

items = ["rice", "beans", "bread", "milk", "eggs"]

#Dictionary to store item prices

price_list = {}

#Collect prices from the user

for item in items:
    price = input(f"Enter the price for {item}: ")
    price_list[item] = price

#Display items and prices

print("\n--- Supermarket Price List ---")
for item, price in price_list.items():
    print(f"{item.capitalize()}: ₦{price}")

#Show available items using .keys()

print("\nAvailable items:", list(price_list.keys()))

#Allow user to update a price

item_to_update = input("Enter the item name to update its price: ").lower()

#Input validation

if item_to_update in price_list:
    new_price = input(f"Enter new price for {item_to_update}: ")
    price_list.update({item_to_update: new_price})
    print(f"{item_to_update.capitalize()} updated to ₦{new_price}")
else:
    print("Item not found in the list.")
