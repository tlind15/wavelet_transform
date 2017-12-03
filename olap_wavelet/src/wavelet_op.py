from pad_zeros import pad_zeros
from prefix_sum import prefix_sum
from wavelet_decomposition import wavelet_decomposition
from select_coefficients import select_coefficients
from wavelet_recomposition import wavelet_recomposition


# perform the wavelet transform on a 1-D data set
def wavelet_transformation(data_file, coefficient_number):

    # make sure size of data is a power of 2. See pad_zeros.py for more details
    pad_zeros(data_file)

    # decompose array data into a single average and a list of detail coefficients
    decomposition = wavelet_decomposition(prefix_sum(data_file))

    # grab the total average
    total_average = decomposition[0]

    # remove some detail coefficients and keep only the specified number. More details in select_coefficients.py
    detail_coefficients = select_coefficients(decomposition[1:],coefficient_number)

    # Recompose the approximate array based off the choosen number of detail coefficients
    approximate_array = wavelet_recomposition(total_average, detail_coefficients)

    # print some values of interest to the user
    print("The total average for that data is ", total_average)
    print("The chosen detail coefficients are ", detail_coefficients)
    print("The final array is ", approximate_array)

    return approximate_array


# write the obtained array from the wavelet transformation to a specified file
def write_transformed_array(array, destination_file):

    # "w+" will create the specified file if it does not already exist
    destination = open(destination_file,"w+")

    # we do not want the file to have an extra newline at the beginning or the end of the file
    # Since the loop write a "\n" and a "value" during each iteration, we need to have one extra write operation
    # This ensures that the first and last operations on the file are the writing of a "value"
    destination.write(str(array[0]))

    for i in range(1,len(array)):
        destination.write("\n" + str(array[i]))

    destination.close()
