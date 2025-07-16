my_tuple = ("red", "green", "blue", "green", "yellow",)
print (f"initial tuple: {my_tuple}")
# access tuple items
# access the element at index 0 
print (f"element at index 0: {my_tuple[0]}")

# access element from index 1 to 3 (exclusive of 4)
print (f"element from index 1 to 3: {my_tuple[1:4]}")

# attempt to change tuple items (and observe the error): self-correction: Remind students that tuples are immutable. You can not directly changean item. If you need a modifiedversion, you typically create a new tuple.

# try to change "red" to "purple" - this will cause an error!
# uncomment the line below to see the typeError:
# my_tuple[0] = "purple"
# print (f"attempted to change: {my_tuple}")
print ("attempting to change tuple items will result in a typeError because are immutable")

# loop through a tuple 

# print each item in the tuple
print ("looping through tuple:") 
for item in my_tuple:
    print (item)

# count() operation:

# count how many times "green" appears in the tuple 
green_count = my_tuple.count("green")
print (f"countof 'green': {green_count}")

# index () operation 
# find the number of items in the first occurence of "blue"
blue_index = my_tuple.index("blue")
print(f"index of 'blue': {blue_index}")

# lenght of a tuple (len()): 

# get the number of items in the tuple 
tuple_lenght = len(my_tuple)
print(f"lenght of the tuple: {tuple_lenght}")






