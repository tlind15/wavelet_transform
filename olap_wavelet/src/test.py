def read_append_test(file):
    read = open(file, "r")
    append = open(file, "a")

    for x in range(10):
        append.write(str(x) + "\n")
        for num in read:
            print(num)



    read.close()
    append.close()


print(7//2)
