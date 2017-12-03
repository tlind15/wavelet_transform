from wavelet_op import *

data = input("Enter the path of your data file: ")
result = input("Enter the destination path for the transformed data: ")

print("You must now choose the number of coefficients that you would like to use for the transformation. " +
      "Choosing more coefficients will generate more accurate data but that data will take longer to generate.")
coefficient_number = int(input("Enter the number of coefficients that you would like to use: "))

#data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/another_test.txt"
#result = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/another_test_result.txt"
write_transformed_array(wavelet_transformation(data ,coefficient_number), result)