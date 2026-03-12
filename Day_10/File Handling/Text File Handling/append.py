file=open('jecrc.txt', 'a+')

# file.write('JECRC is a very good university!\n')
# file.write('JECRC is also very popular for placements!') ##will not over ride any data. It will write after that

file.writelines([
    '\nHere food is good!',
    '\nEcosystem is also very good!',
    '\nFaculties are very supportive!\n'
])
file.seek(0)
print(file.read()) ##all the data will be printed

file.close()