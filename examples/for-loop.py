# Say you want to do something 10 times
# For loop to the rescue!
for i in range(10):
    print(i)
    
# The range function returns a list of numbers
# that cannot be changed
print(range(10))

# If range is just a list, this implies that you can
# "iterate" over any list
my_list = ["a", "b", "c"]

for letter in my_list:
    print(letter)
    
# You can also iterate over a dictionary with the help
# of the items method
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(key, value)