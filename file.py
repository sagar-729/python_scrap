file = open("demo.txt", 'w')                                                                                            # we have to specify in which mode we have to open the file
file.write("This is the content for the file. ")
file.close()

file = open("demo.txt", 'r')                                                                                            #opening file in Read Mode
content = file.read()
print(content)
file.close()

file = open("demo.txt", 'a')
file.write("This is the new content.")                                                                                  #It donot interfere with the last saved content.
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()