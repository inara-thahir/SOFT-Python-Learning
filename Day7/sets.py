# Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length
print(len(it_companies))

# 2. Add Twitter
it_companies.add('Twitter')

# 3. Add multiple companies
it_companies.update(['Netflix', 'Intel', 'Cisco'])

# 4. Remove one company
it_companies.remove('Oracle')

# 5. Difference between remove and discard
# remove() gives an error if the item does not exist.
# discard() does not give an error if the item does not exist.


# Exercises: Level 2

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Join A and B
print(A.union(B))

# Intersection
print(A.intersection(B))

# Is A a subset of B?
print(A.issubset(B))

# Are A and B disjoint?
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# Symmetric difference
print(A.symmetric_difference(B))

# Delete the sets
del A
del B


# Exercises: Level 3

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Length of list:", len(ages))
print("Length of set:", len(ages_set))

# The list is bigger because it contains duplicate ages.


# Difference between data types:
# String = text
# List = ordered and changeable collection
# Tuple = ordered and unchangeable collection
# Set = unordered collection of unique items


# Unique words
sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))