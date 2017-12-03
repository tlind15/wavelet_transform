import math


def wavelet_decomposition(array):
    h = [0.5, 0.5]
    g = [0.5, -0.5]

    iteration_count = math.log(len(array),2)
    h_transform_array = []
    g_transform_array = []

    for y in range(0,len(array) - 1,2):
        element_i = array[y]
        element_i_plus_1 = array[y+1]

        average = h[0] * element_i + h[1] * element_i_plus_1
        detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

        h_transform_array.append(average)
        g_transform_array.append(detail_coefficient)

    print(h_transform_array)

    for x in range(1, int(iteration_count)):
        marker = 0
        size = len(h_transform_array)
        temp_g = []
        while marker < size:

            element_i = h_transform_array[marker]
            element_i_plus_1 = h_transform_array[marker + 1]

            average = h[0] * element_i + h[1] * element_i_plus_1
            detail_coefficient = g[0] * element_i + g[1] * element_i_plus_1

            h_transform_array.append(average)
            temp_g.append(detail_coefficient)

            marker += 2
        g_transform_array = temp_g + g_transform_array
        del h_transform_array[:size]
    return h_transform_array + g_transform_array
