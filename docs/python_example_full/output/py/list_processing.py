def split_list(full_list, group1, group2):
    """Splits a list of items into two empty groups
    of even and odd items.
    A copy of the original list is made"""
    i = 0
    # make a copy to preserve the original list
    # used to simplify the examples
    full_list_cp = full_list[::-1]
    while full_list_cp:
        i += 1
        item = full_list_cp.pop()
        if i % 2 != 0:
            group1.append(item)
        else:
            group2.append(item)


def print_items(list):
    """Prints the items in a list"""
    for item in list:
        print(f"- {item}")
