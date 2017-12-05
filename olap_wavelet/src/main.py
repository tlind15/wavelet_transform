from wavelet_op import *
from query import query_original, query_wavelet
from update import update_original, update_wavelet

'''This dataset represents the amount of hits Company X gets on their website every minute'''

#data = input("Enter the path of your data file: ")
#result = input("Enter the destination path for the transformed data: ")

#print("You must now choose the number of coefficients that you would like to use for the transformation. " +
 #     "Choosing more coefficients will generate more accurate data but that data will take longer to generate.")
coefficient_number = int(input("Enter the number of coefficients that you would like to use: "))

data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/error_checking.txt"
result = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/another_test_result_copy.txt"
write_array_to_file(wavelet_transformation(data, coefficient_number), result)

#print(query_original(data))
#print(query_wavelet(result))


#print(update_original(data))
#print(update_wavelet(result, data, coefficient_number))