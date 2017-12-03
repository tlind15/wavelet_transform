from pad_zeros import pad_zeros
from prefix_sum import prefix_sum
from wavelet_decomposition import wavelet_decomposition
from select_coefficients import select_coefficients
from wavelet_recomposition import wavelet_recomposition


def wavelet_transformation(data_file, coefficient_number):
    pad_zeros(data_file)

    decomposition = wavelet_decomposition(prefix_sum(data_file))

    total_average = decomposition[0]
    detail_coefficients = select_coefficients(decomposition[1:],2)

    approximate_array = wavelet_recomposition(total_average, detail_coefficients)

    print("The total average for that data is ", total_average)
    print("The chosen detail coefficients are ", detail_coefficients)
    print("The final array is ", approximate_array)

    return approximate_array


def write_transformed_array(array, destination_file):
    destination = open(destination_file,"w+")

    destination.write(str(array[0]))

    for i in range(1,len(array)):
        destination.write("\n" + str(array[i]))

    destination.close()
