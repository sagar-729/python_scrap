file = open("demo.txt", 'r')                                                                                            # read only

content = file.read()
print(content)

# make sure to close the file
file.close()