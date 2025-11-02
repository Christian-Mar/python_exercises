# Create a Python script that removes all the elements of a list that are duplicate.

l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
l1 = list(set(l1))
print(l1)

# Write a Python function that takes a list as argument and returns a new list with unique
# elements of the first list in the same order.

def unique_list(my_list):
    tmp_list = list()
    for x in my_list:
        if x not in tmp_list:
            tmp_list.append(x)
    return tmp_list


friends = ['Dan', 'Maria', 'Dan', 'Dan', 'John', 'Dan']
print(unique_list(friends))