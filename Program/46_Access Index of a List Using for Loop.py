my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)
    
    
# Start the indexing with non zero value
# Example 2

my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)
