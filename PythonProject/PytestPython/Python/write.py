# read the file and store all the lines in list
# reverse the list
#write the list back to file


# this will open and close file , both actions in one go
with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


