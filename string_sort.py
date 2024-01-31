def string_sort(list):
    """
    sorts through a list by comparing two values at consecutive indexes and swaps if the lesser index is greater
    in value than the higher index.
    """
    for index in range(1, len(list)):
        value = list[index]
        pos = index - 1
        while pos >= 0 and list[pos] > value:
            list[pos + 1] = list[pos]
            pos -= 1
        list[pos + 1] = value


# example = ["hello", "worLd", "Goodbye", "moon"]
#
# string_sort(example)
# print(example)