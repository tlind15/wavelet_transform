import math


# determine number of data elements in the file
def get_data_count(file):
    data = open(file, "r")
    count = 0
    for count, line in enumerate(data):
        pass
    data.close()
    return count+1  # it enumerates from zero so you add 1 to get true count


# the wavelet transform works much nicer when the array size is a power of 2
# we can make our array size optimal by padding our current array with zeros

# we want to find the closest number that is a power of 2 to our array size
def nearest_power_of_two(count):
    exact_pow = math.log(count, 2)
    nearest_pow = math.ceil(exact_pow)
    return pow(2,nearest_pow)


# determine how many zeros we need to pad to our current array
def num_zeroes_for_padding(count):
    return nearest_power_of_two(count) - count


# pad zeros to the array by appending the array data file
def pad_zeros(file):
    data = open(file, "a")
    count = get_data_count(file)
    num_zeros_to_pad = num_zeroes_for_padding(count)

    for x in range(num_zeros_to_pad):
        data.write("\n" + str(0))  # you need the \n before the string to prevent having an extra newline at the end
    data.close()
