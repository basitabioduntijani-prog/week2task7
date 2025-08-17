

#Store names and phone numbers in tuples

names = ("Alice", "Bob", "Charlie")
numbers = ("08012345678", "08123456789", "09098765432")

#Combine using zip and convert to dictionary

contacts = dict(zip(names, numbers))

#Ask user for a name

search_name = input("Enter the name to look up: ")

#Retrieve phone number safely using .get()

phone = contacts.get(search_name)

#Display result

if phone:
    print(f"{search_name}'s phone number is {phone}")
else:
    print("Name not found in contacts.")
