# the kth element of the prefix sum array represents the aggregate sum of the first k elements of the original array

# determine the prefix sum of the array data
def prefix_sum(original_array_file):
    original = open(original_array_file, 'r+')  # the original array array data, with read permissions only
    prefix_sum_array = []
    aggregate_sum = 0
    line_count = 0

    for num in original:
        line_count += 1
        try:
            temp = float(num)
        except ValueError:
            print("The data entry at line " + str(line_count) + " has either more than one value, contains a non-numeric "
                                                                "value, or has no value at all. Fix the data and then try again.")
            return None
        aggregate_sum += temp
        prefix_sum_array.append(aggregate_sum)

    original.close()
    return prefix_sum_array
