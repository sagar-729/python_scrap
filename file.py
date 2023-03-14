file = open("demo.txt", 'r')                                                                                            # read only

line = file.readline()                                                                                                  # line is a String
while line:
    print("Line read- " + line)
    line = file.readline()                                                                                              # in a readline() , String concatenated with "\n". And file content First line is deleted.
# file is IOWrapper , so we need to convert it into String => file.read() to convert into String

# make sure to close the file
file.close()