# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(51)]

# Create a list of integers (0-50) by unpacking range
%timeit nums_unpack = [range(51)]

# Create a list using the formal name
%timeit formal_list = list()

# Create a list using the literal syntax
%timeit literal_list = []
