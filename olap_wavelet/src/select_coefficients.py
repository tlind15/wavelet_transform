import statistics


# we assume 'array' is an array of detail coefficients
def select_coefficients(array, nums_of_coefficients):
    if nums_of_coefficients >= len(array):
        return array

    original_array = deep_copy(array)
    cutoff_coefficient_value = kth_smallest_element(array, nums_of_coefficients)
    for x in range(len(original_array)):
        if original_array[x] > cutoff_coefficient_value:
            original_array[x] = 0

    return original_array


def kth_smallest_element(array, k):
    tally = k
    left_marker = None
    right_marker = None

    left_marker_stop = False
    left_marker_stop = False
    right_marker_stop = False

    while True:
        size = len(array)
        temp_arr = [array[0], array[size//2], array[size-1]]
        pivot = statistics.median(temp_arr)
        left_marker = 0
        right_marker = size-2

        index_of_pivot = None
        if temp_arr.index(pivot) == 0:
            index_of_pivot = 0
        elif temp_arr.index(pivot) == 1:
            index_of_pivot = size // 2
        elif temp_arr.index(pivot) == 2:
            index_of_pivot = size - 1

        array[index_of_pivot], array[size - 1] = array[size - 1], array[index_of_pivot]  # swap pivot with last element

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

        if tally == left_marker+1:
            return array[left_marker]

        elif left_marker >= tally:
            del array[left_marker:]

        else:
            del array[:left_marker+1]
            tally -= left_marker+1

def deep_copy(array):
    deep_copy = []
    for num in array:
        deep_copy.append(num)

    return deep_copy
