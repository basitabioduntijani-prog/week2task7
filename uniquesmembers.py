

#Ask for names input

names_input = input("Enter three names separated by commas: ")

#Convert to set to remove duplicates

set_of_names = set(names_input.split(","))

#Create dictionary with name as key and length as value

name_lengths = {name.strip(): len(name.strip()) for name in set_of_names}

#Display the dictionary
print("\n--- Name Lengths ---")
for name, length in name_lengths.items():
    print(f"{name}: {length}")
