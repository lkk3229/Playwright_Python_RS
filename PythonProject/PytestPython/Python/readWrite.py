file = open('test.txt')

# Read all the content of file
#print(file.read())
# read n number of characters by parsing parameter
#print(file.read(5))

#Read one single line at a time
#print(file.readline())
#print(file.readline())


# print each line of file using readline method
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

# read each line and keep it list form
#print(file.readlines())
for line in file.readlines():
    print(line)



file.close()