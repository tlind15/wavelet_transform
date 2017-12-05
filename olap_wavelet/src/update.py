#  Update: During day 4 of month 11, the server was down and did not receive any website hits that day.

from query import read_file_into_array, minutes_per_month
from wavelet_op import wavelet_transformation, write_array_to_file


def update_original(data_file):
    data = read_file_into_array(data_file)

    start_index_month11_day4 = minutes_per_month(11) + minutes_per_day(3)
    end_index_month11_day4 = minutes_per_month(11) + minutes_per_day(4)

    update_cost = 0  # we add one for every value changed
    for x in range(start_index_month11_day4, end_index_month11_day4):
        data[x] = 0
        update_cost += 1

    return {"update cost": update_cost}


def update_wavelet(original_wavelet_file, original_data_file, coefficient_number):

    data = read_file_into_array(original_data_file)

    start_index_month11_day4 = minutes_per_month(11) + minutes_per_day(3)
    end_index_month11_day4 = minutes_per_month(11) + minutes_per_day(4)

    for x in range(start_index_month11_day4, end_index_month11_day4):
        data[x] = 0

    write_array_to_file(data, original_data_file)

    return wavelet_update_cost(original_wavelet_file, original_data_file, coefficient_number)


def wavelet_update_cost(original_wavelet_file, original_data_file, coefficient_number):
    original_wavelet_array = read_file_into_array(original_wavelet_file)
    updated_wavelet_array = wavelet_transformation(original_data_file, coefficient_number)

    # number values in 'original_wavelet_array' that changed in 'updated_wavelet_array' as a result of the update
    update_cost = 0
    for i in range(len(original_wavelet_array)):
        if original_wavelet_array[i] != updated_wavelet_array[i]:
            update_cost += 1

    return {"update cost": update_cost}


def minutes_per_day(num_days):
    minutes_per_hour = 60
    hours_per_day = 24
    return minutes_per_hour*hours_per_day*num_days
