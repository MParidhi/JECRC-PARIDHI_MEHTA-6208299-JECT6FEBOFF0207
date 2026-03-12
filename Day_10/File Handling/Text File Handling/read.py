# only read
file = open('temp.txt', 'r')

# print(file.read())


# print(file.readline()) ##will only print 'first line'
# ## for all three line repeat it
# print(file.readline())
# print(file.readline())
# print(file.readline()) ##now it will print space
# print(file.readline())

print(file.readlines()) ##['first line\n', 'second line\n', 'third line']

file.close()
## if we want to implement all three functions of read use seek(0) after all individual function