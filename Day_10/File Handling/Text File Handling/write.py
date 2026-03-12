## only_write
# file=open('temp.txt', 'w')
# # file.write('I am the first line!\n')
# # file.write('I am the new line!')
# file.writelines([
#     'first line\n',
#     'second line\n',
#     'third line'
# ])


# file.close()

## write+read
file=open('temp.txt', 'w+')
#if the file is not present inside the folder, then we cannot read it. It will raise FileNotFound error

file.writelines([
    'first line\n',
    'second line\n',
    'third line'
])

# print(file.read()) ##will not print anything
## so we will use one function--seek-->To make python interpreter to point at a specific index, we use this function(mostly index=0)
file.seek(0)
print(file.read())
file.close()