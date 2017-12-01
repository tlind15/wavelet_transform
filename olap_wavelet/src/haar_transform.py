from pad_zeros import get_data_count
from detail_coefficient_partition import select_coefficients
import math

def haar_transform(array_file):
    h = [0.5, 0.5]
    g = [0.5, -0.5]

    iteration_count = math.log(get_data_count(array_file),2)
    array = open(array_file, "r")
    h_transform_array = []
    g_transform_array = []

    element_i = None
    element_i_plus_1 = None
    average = None
    detail_coefficient = None

    for num in array:
        element_i = int(num)
        element_i_plus_1 = int((array.readline()))

        average = h[0] * element_i + h[1] * element_i_plus_1
        detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

        h_transform_array.append(average)
        g_transform_array.append(detail_coefficient)

    array.close()

    for x in range(1, int(iteration_count)):
        marker = 0
        size = len(h_transform_array)
        while marker < size:

            element_i = h_transform_array[marker]
            element_i_plus_1 = h_transform_array[marker + 1]

            average = h[0] * element_i + h[1] * element_i_plus_1
            detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

            h_transform_array.append(average)
            g_transform_array.append(detail_coefficient)

            marker += 2
        del h_transform_array[:size]

    return h_transform_array + g_transform_array


data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/test_prefix_sum.txt"
array_data = haar_transform(data)
print(array_data)
temp_arr = select_coefficients(array_data[1:], 1)
print(temp_arr)

