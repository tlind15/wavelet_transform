from pad_zeros import pad_zeros
from prefix_sum import prefix_sum
from wavelet_decomposition import wavelet_decomposition
from select_coefficients import select_coefficients
from wavelet_recomposition import wavelet_recomposition


data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/another_test.txt"
#new_data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/another_test_prefix_sum.txt"

pad_zeros(data)

decomposition = wavelet_decomposition(prefix_sum(data))
total_average = decomposition[0]

detail_coefficients = select_coefficients(decomposition[1:],2)
approximate_array = wavelet_recomposition(total_average, detail_coefficients)


#("The total average for that data is ", total_average)
print("The chosen detail coefficients are ", detail_coefficients)
print("The final array is ", approximate_array)
