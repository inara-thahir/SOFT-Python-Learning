 # Create an empty tuple
empty_tuple = ()

# Tuple containing names of sisters and brothers
sisters = ("Hooriya", "Hawwa")
brothers = ("Mohammed" , "Mammu")

# Join brothers and sisters
siblings = brothers + sisters
print("My siblings:", siblings)

# Number of siblings
print("Number of siblings:", len(siblings))

# Add father and mother
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)


# 1. Unpack siblings and parents from family_members
brother1, brother2, sister1, sister2, father, mother = family_members

# 2. Create fruits, vegetables and animal products tuples
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "potato", "tomato")
animal_products = ("milk", "egg", "cheese")

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change tuple to list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item(s)
middle = food_stuff_lt[len(food_stuff_lt)//2]

# 5. First three and last three items
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6. Delete the tuple
del food_stuff_tp

# 7. Check if countries are Nordic countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
