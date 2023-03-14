file = open("demo.txt", 'r')                                                                                            # read only

content = file.readline()
print(content)

# make sure to close the file
file.close()