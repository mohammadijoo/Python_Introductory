my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
#my_list2 = ["" , '']

def empty_dict(x):
    return all(not d for d in x)

print(empty_dict(my_list))
print(empty_dict(my_list1))
#print(empty_dict(my_list2))
