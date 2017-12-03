from math import floor, log


def wavelet_recomposition(total_average, detail_coefficient_array):
    size = len(detail_coefficient_array)
    new_data_recomposition = [total_average]
    data_index = 0

    for coefficient in detail_coefficient_array:
        new_data_recomposition.append(new_data_recomposition[data_index] + coefficient)
        new_data_recomposition.append(new_data_recomposition[data_index] - coefficient)
        data_index += 1

    #print(new_data_recomposition)
    return get_final_array(new_data_recomposition)


def get_final_array(recomposition_data):
    first_number_index = 2**(floor(log(len(recomposition_data), 2))) - 1
    return recomposition_data[first_number_index:]
