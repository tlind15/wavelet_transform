from math import floor, log


# After decomposing the original array data into a total average and detail coefficients
# we then selected some of those coefficients
# Here we use those selected coefficients to reconstruct an approximation to the original prefix-sum array
# this array will allow for faster querying than the original prefix-sum array
def wavelet_recomposition(total_average, detail_coefficient_array):
    new_data_recomposition = [total_average]  # will hold the data that will generate the approximation

    # newly calculated data will be based off other data in the array
    # this index will help us track the other data that we need
    data_index = 0

    # This process is essentially like constructing a binary tree
    # We have a value, we add the coefficient to produce a "left child" and subtract to produce a "right child"
    # we essentially perform a level order traversal and repeat the above process
    for coefficient in detail_coefficient_array:
        new_data_recomposition.append(new_data_recomposition[data_index] + coefficient)
        new_data_recomposition.append(new_data_recomposition[data_index] - coefficient)
        data_index += 1

    # Many of the values in 'new_data_recomposition' are intermediate values that we use to calculate other values
    # if we imagine our list as a full binary tree, the pertinent values would be those at the bottom level (the leaves)
    return get_final_array(new_data_recomposition)


# computes the first index where we expect the pertinent values to reside
def get_final_array(recomposition_data):
    first_number_index = 2**(floor(log(len(recomposition_data), 2))) - 1
    return recomposition_data[first_number_index:]
