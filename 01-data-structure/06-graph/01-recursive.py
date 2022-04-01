numbers = [3, 1, 4, 1, 5, 9]


def recursive(number, number_list):
    print(f"recursive({number}, {number_list})")
    if not number_list:
        print(f"return {number}")
        return number

    number += number_list.pop(0)
    return recursive(number, number_list)


recursive(0, numbers)


numbers = [3, 1, [4, 1, [5, 9]]]


def recursive_deep(number, number_list):
    print(f"recursive_deep({number}, {number_list})")

    if not number_list:
        print(f"return {number}")
        return number

    if isinstance(number_list[0], int):
        number += number_list.pop(0)
        return recursive_deep(number, number_list)
    else:
        new_number_list = number_list.pop(0)
        return recursive_deep(number, new_number_list)


recursive_deep(0, numbers)
