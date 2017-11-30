def read_append_test(file):
    read = open(file, "r")
    append = open(file, "a")

    for x in range(10):
        append.write(str(x) + "\n")
        for num in read:
            print(num)



    read.close()
    append.close()


data = "C:/Users/tlindblom/Google Drive/CECS Classes/521 Database Architecture/read_append.txt"
read_append_test(data)

