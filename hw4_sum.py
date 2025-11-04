def sum_general_int_list(general_list):
    total = 0
    for item in general_list:
        if isinstance(item, list):
            total += sum_general_int_list(item)
        else:
            total += item
    return total

sample_list = [[1], 2, 3, [4, [5], [6, 7, [8,9]], 10], 1]

print(sum_general_int_list(sample_list))