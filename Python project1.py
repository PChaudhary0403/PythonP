# Creating a list, a dictionary, and a set
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3, 4, 5}

# Performing basic operations

# List operations
my_list.append(6)        # Adding an element
my_list.remove(3)        # Removing an element
my_list[1] = 10          # Modifying an element

# Dictionary operations
my_dict['d'] = 4         # Adding an element
del my_dict['b']         # Removing an element
my_dict['a'] = 10        # Modifying an element

# Set operations
my_set.add(6)            # Adding an element
my_set.remove(2)         # Removing an element
# Modifying elements is not directly applicable to sets, so we'll demonstrate other operations
my_set.update([7, 8])    # Adding multiple elements

# Printing the results
print("Updated list:", my_list)
print("Updated dictionary:", my_dict)
print("Updated set:", my_set)

