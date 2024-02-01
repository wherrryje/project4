def bubble_count(b_list):
    """
    Sorts a_list in ascending order while counting individual comparisons and exchanges. returns
    a tuple with both.
    """
    comparisons = 0
    exchanges = 0

    for pass_num in range(len(b_list) - 1):
        for index in range(len(b_list) - 1 - pass_num):
            comparisons += 1
            if b_list[index] > b_list[index + 1]:
                exchanges += 1
                b_list[index], b_list[index + 1] = b_list[index + 1], b_list[index]

    return comparisons, exchanges


def insertion_count(list):
    comparisons = 0
    exchanges = 0

    for index in range(1, len(list)):
        key = list[index]
        j = index - 1
        while j >= 0:
            comparisons += 1
            if list[j] > key:
                exchanges += 1
                list[j + 1] = list[j]
                j -= 1
            else:
                break

        list[j + 1] = key

    return comparisons, exchanges

#
# list = [5, 3, 1, 29, 28, 17, 4, 2]
# b_list = [5, 3, 1, 29, 28, 17, 4, 2]
# print(insertion_count(list))
# print(bubble_count(b_list))

# temp = list[index]
# list[index] = list[index + 1]
# list[index + 1] = temp