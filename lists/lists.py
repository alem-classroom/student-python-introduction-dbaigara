def size_of_list(list):
    return len(list)
    # return size of list

def add_elem_to_list(list, elem):
    list.append(elem)
    return (list)
    # add elem to list and return the list

def delete_elem_from_list(list, index = -1):
    if index >= 0 and index <= len(list):
        list.pop(index)
    else:
        list.pop(-1)
    return (list)
        # delete element from list, such that its index is index

def count_elements_in_list(list, x):
    return list.count(x)
    # count elements in the list that are equal to x and return the count

def sort_list(list):
    list.sort()
    return list
    # return sorted list

def reverse(list):
    list.reverse()
    return list
    # return reversed list
