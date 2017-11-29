import math


def get_data_count(file):
    data = open(file, "r")
    count = 0
    for count, line in enumerate(data):
        pass
    data.close()
    return count+1  # it enumerates from zero so you add 1 to get true count


def nearest_power_of_two(count):
    exact_pow = math.log(count,2)
    nearest_pow = math.ceil(exact_pow)
    return pow(2,nearest_pow)


def num_zeroes_for_padding(count):
    return nearest_power_of_two(count) - count


def pad_zeros(file):
    data = open(file, "a")
    count = get_data_count(file)
    num_zeros_to_pad = num_zeroes_for_padding(count)

    for x in range(num_zeros_to_pad):
        data.write("\n" + str(0))  # you need the \n before the string to prevent having an extra newline at the end
    data.close()


f = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/test_big_text.txt"
pad_zeros(f)
