def all_true(tuple):
    return all(tuple)

my_tuple = (True, True, 1, True)
if all_true(my_tuple):
    print("All elements of the tuple are true")
else:
    print("Not all elements of the tuple are true")