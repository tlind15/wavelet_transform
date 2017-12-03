import math


# decompose the original data array into a single average and a list of detail coefficients
def wavelet_decomposition(array):

    # h and g are two vectors developed by Alfred Haar form the Haar wavelet basis
    # This method will transform the data using this basis
    h = [0.5, 0.5]  # this vector essentially produces the average of two numbers
    g = [0.5, -0.5]  # this vector essentially produces the difference of two numbers from their average

    # each iteration of the transformation will produce half as many values for the h transform array
    iteration_count = math.log(len(array),2)

    h_transform_array = []  # this will hold all values generated from the h vector
    g_transform_array = []  # this will hold all values generated from the g vector

    # we iterate through the passed in array, transforming the data with the h and g vectors
    # the '2' in the loop definition is the loop step size
    for y in range(0,len(array) - 1,2):

        # take the current element and the proceeding element in the list
        # peform the h & g transformations on the given pair of numbers
        # place the obtained values in the appropriate lists
        element_i = array[y]
        element_i_plus_1 = array[y+1]

        # each of these the first number in the pair is transformed by h[0] or g[0], and the second by h[1] or g[1]
        average = h[0] * element_i + h[1] * element_i_plus_1
        detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

        h_transform_array.append(average)
        g_transform_array.append(detail_coefficient)

    del array[:]  # we are done with the array and we can remove it from memory

    # Once we finish with 'array', we can perform the remaining operations all on the h_transform and g_transform lists
    for x in range(1, int(iteration_count)):  # start from 1 because we just did the first iteration above
        marker = 0  # this represents the current position in the h_transform_array
        size = len(h_transform_array)
        temp_g = []  # this aids with the proper ordering of the detail coefficients in the g_transform_array

        while marker < size:

            # the concept the same as above
            element_i = h_transform_array[marker]
            element_i_plus_1 = h_transform_array[marker + 1]

            average = h[0] * element_i + h[1] * element_i_plus_1
            detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

            h_transform_array.append(average)
            temp_g.append(detail_coefficient)

            marker += 2

        g_transform_array = temp_g + g_transform_array  # insert coefficients in proper position
        del h_transform_array[:size]  # save memory space and remove elements that are no longer needed

    return h_transform_array + g_transform_array
