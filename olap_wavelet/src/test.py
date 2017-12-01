def read_append_test(file):
    read = open(file, "r")
    append = open(file, "a")

    for x in range(10):
        append.write(str(x) + "\n")
        for num in read:
            print(num)



    read.close()
    append.close()


x = [1,3]

del x[1:]

print(x)

