# the kth element of the prefix sum array represents the aggregate sum of the first k elements of the original array

# determine the prefix sum of the array data
def prefix_sum(original_array_file):
    original = open(original_array_file, 'r')  # the original array array data, with read permissions only
    prefix_sum_array = []
    aggregate_sum = 0

    for num in original:
        aggregate_sum += int(num)
        prefix_sum_array.append(aggregate_sum)

    original.close()
    print(prefix_sum_array)
    return prefix_sum_array
