file = open("demo.txt", 'w')
file.write("this is content for the file")                                                                              # this overwrite the text over last text.
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)

