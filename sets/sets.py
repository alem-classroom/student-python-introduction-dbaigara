def size_of_set(set):
    return len(set)# return size of set  
def is_elem_in_set(set, elem):
    if elem in set:
        return True
    else:
        return False
    # return true if elem exists in set, false otherwise

def are_sets_equal(first_set, second_set):
    if first_set == second_set:
        return True
    else:
        return False
    # return true if sets have the same elements inside, otherwise false

def add_elem_to_set(set, elem):
    if elem in set:
        return set
    set.add(elem)
    return set
    # add elem to the set if elem does not exist in set, and return the set
    # if elem exists in set, return set

def remove_elem_if_exists(set, elem):
    if elem in set:
        return set.remove(elem)
    return set
    # remove elem from set if it exists, and return the set

def delete_first_element(set):
    set.pop()
    return set
    # delete first elemenent of set

'''
set = {1.0, "Hello", (1, 2, 3)}
set1 = {1.0, "Hello", (1, 2, 3)}
print('Size of set is ', size_of_set(set))
print('Is elem in set ', is_elem_in_set(set,"Hello"))
print('Are sets equal ', are_sets_equal(set, set1))
print('Add elem to set ', add_elem_to_set(set, 235))
print('Remove elem if exists ', remove_elem_if_exists(set, 2))
print('Delete first element ', delete_first_element(set))
'''