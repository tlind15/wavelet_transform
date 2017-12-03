# determine the prefix sum of the array data
# the kth element of the prefix sum array represents the aggregate sum of the first k elements of the original array
def prefix_sum(original_array_file):
    original = open(original_array_file, 'r')  # the original array array data, with read permissions only
    #new = open(new_array_file, 'w+')  # the file that will hold prefix sum data
    prefix_sum_array = []

    aggregate_sum = 0

    # By nature of the loop, "\n" + str(aggregate_sum) writes 'aggregate_sum' and '\n' the file the same number of times
    # This will cause the file to have an extra newline either at the beginning or the end
    # To avoid this we write the first 'aggregate_sum' to the file, and then write "\n" + str(aggregate_sum) in the loop

    # write the first 'aggregate_sum' value
    #first_value = original.readline()
    #aggregate_sum += int(first_value)
    #new.write(str(aggregate_sum))

    for num in original:
        aggregate_sum += int(num)
        prefix_sum_array.append(aggregate_sum)
        #new.write("\n" + str(aggregate_sum))

    original.close()
    print(prefix_sum_array)
    return prefix_sum_array
    #new.close()
