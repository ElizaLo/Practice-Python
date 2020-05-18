# Use map to apply str.upper to each element in names
names_map  = map(lambda name: name.upper(), names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
