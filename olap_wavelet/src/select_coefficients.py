import statistics


# we assume 'array' is an array of detail coefficients
# we want to keep the specified number of detail coefficients and make the rest equal to zero
# if we know the kth largest magnitude coefficient, we can simply set all other smaller magnitude ones equal to zero
# This will eventually allow an approximate array to be created from which faster querying will be possible
def select_coefficients(array, nums_of_coefficients):

    if nums_of_coefficients < 1:
        return None

    if nums_of_coefficients >= len(array):
        return array

    original_array = deep_copy(array)
    cutoff_coefficient_value = kth_smallest_element(array, nums_of_coefficients)
    if cutoff_coefficient_value is None:
        return None

    for x in range(len(original_array)):
        if original_array[x] > cutoff_coefficient_value:
            original_array[x] = 0

    return original_array


# in signal processing we know that the largest coefficients are a better indicator of the characteristics of a data set
# we know that detail coefficients will have negative values
# In this case, the "largest" coefficients are the most negative values (or ones with greatest magnitude)
# We want to find the kth smallest coefficient value (or kth largest magnitude). See above for more.
# We use the Quicksort partitioning algorithm to find the kth smallest element
def kth_smallest_element(array, k):

    if k < 1 or len(array) == 0:
        return None

    if len(array) == 1:
        return array[0]

    tally = k
    left_marker_stop = False
    right_marker_stop = False

    while True:
        size = len(array)
        left_marker = 0
        right_marker = size-2

        # using median of 3 method for determining the pivot
        temp_arr = [array[0], array[size // 2], array[size - 1]]
        pivot = statistics.median(temp_arr)

        index_of_pivot = None
        if temp_arr.index(pivot) == 0:
            index_of_pivot = 0
        elif temp_arr.index(pivot) == 1:
            index_of_pivot = size // 2
        elif temp_arr.index(pivot) == 2:
            index_of_pivot = size - 1

        array[index_of_pivot], array[size - 1] = array[size - 1], array[index_of_pivot]  # swap pivot with last element

        # begin list partitioning
        while left_marker <= right_marker:
            if array[left_marker] <= pivot and left_marker <= right_marker:
                left_marker += 1
            else:
                left_marker_stop = True

            if array[right_marker] >= pivot and right_marker >= left_marker:
                right_marker -= 1
            else:
                right_marker_stop = True

            if left_marker_stop and right_marker_stop:

                if left_marker < size-1:
                    array[left_marker], array[right_marker] = array[right_marker], array[left_marker]
                    left_marker += 1
                if right_marker > 0:
                    right_marker -= 1
                left_marker_stop = False
                right_marker_stop = False


        #swap left marker with pivot
        array[left_marker], array[size-1] = array[size-1], array[left_marker]

        # in each of the following, the 'left_marker' represents the number of elements less than the pivot value

        # we know the pivot is larger than all values to the left of it
        # thus if tally (or k) is the number of elements to the left of the pivot plus 1
        # the pivot is the number we are looking for
        if tally == left_marker+1:
            return array[left_marker]

        # if the number of elements smaller than the pivot is more than 'tally'
        # we know that the element of interest must be to the left of the pivot
        # thus we can delete all elements to the right of the pivot and the pivot itself
        elif left_marker >= tally:
            del array[left_marker:]

        # if the number of elements smaller than the pivot is less than 'tally'
        # then the element of interest must be to the right of the pivot
        # thus we can delete all elements to the left of the pivot and the pivot itself
        else:
            del array[:left_marker+1]
            tally -= left_marker+1

# a helper function for 'select_coefficients' that makes a deep copy of a list
def deep_copy(array):
    deep_copy = []
    for num in array:
        deep_copy.append(num)

    return deep_copy
