class TargetNotFound(Exception):
    pass

def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, raises exception of TargetNotFound
    """
    # enumerate lets you iterate through both the elements of the list and their indices
    for index, el in enumerate(a_list):
        if el == target:
            return index
    raise TargetNotFound

# abc = linear_search([1,2,3,4,],4)
# print(abc)