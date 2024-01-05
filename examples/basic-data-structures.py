# A list is a collection objects that will keep the order, 
# can be changed and can contain duplicates
my_list = [1, 1, 3, 3, 4, 5]

# A dictionary is an unordered collection of key-value pairs.
# Each key is unique but values can be duplicated.
# Just like a list, you can add or remove elements
my_dict = {"a": 1, "b": 2, "c": 2}

# A set is an unordered collection of unique elements
my_set = {1, 2, 3, 4, 4, 5}

# Some common operations

# Adding an element to the collection
my_list.append(6)
my_dict["d"] = 3
my_set.add(6)

# Removing an element from the collection
my_list.pop(5) # Remove the nth element from the list
my_dict.pop("a")
my_set.remove(4)

# Check if the element is in the collection
print(3 in my_list)
print("b" in my_dict)
print(2 in my_set)

# Joining two collections
print([1,2,3] + [4,5,6])
print({"a": 1, "b": 2} | {"c": 3, "d": 4})
print({1,2,3} | {4,5,6})
print({1,2,3}.union({4,5,6}))

# Comprehensions are a pythonic way to create new collections
# from an existing one
print([i * 2 for i in my_list])
print({i: i * 2 for i in my_dict})
print({i * 2 for i in my_set})
# Checkout the "for" page to learn more about loops