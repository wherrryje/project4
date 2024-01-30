class TargetNotFound(Exception):
    pass

def linear_search(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    # enumerate lets you iterate through both the elements of the list and their indices
    for index, el in enumerate(a_list):
        if el == target:
            return index
    raise TargetNotFound

# abc = linear_search([1,2,3,4,],4)
# print(abc)