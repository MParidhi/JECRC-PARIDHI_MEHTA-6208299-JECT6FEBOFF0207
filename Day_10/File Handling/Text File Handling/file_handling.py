'''
File Handling
--File is a type of container in which we contain or store some data
--By using extension name, we can identify what tyoe of data is there inside of it
    EX: .py, .mp4, .html, .mp3, .png, .jpg/.jpeg, etc.

Before handling any file, taking permission is very much important. It is done using open function
open(): 
    open('filename.ext'/'absolute_path', mode)
    
to close the file, we use reference of file stored in variable:
close():
    var_name.close()
    
--We have 3 diff modes:
    1. write(w),
    2. read(r),
    3. append(a)
    
write mode:
    1. only write(w),
    2. write + read(w+), #first write then read
    3. write binary(wb),
    4. write & read binary(wb+)
    
read mode:
    1. only red(r),
    2. read + write(r+), #first read then write
    3. read binary(rb),
    4. read & write binary(rb+)
    
append mode:
    1. only append(a),
    2. append + read(a+)
    3. append binary(ab),
    4. append & read binary(ab+)
'''

'''
For write operation, we have two functions
    1. write(str_data): Single line of data
        --In this, if the file is not present, it will create one then perform write operation
        --If the file is already present, then it will override the prev data with the new one
    2. writelines([line1, line2, ..., linen]): For multiple line of data
'''
'''
For read operation, we have three functions
    1. read(): Display the file contents as it is
    2. readline(): It will read the data line by line i.e. single line of data at a time
    3. readlines()
'''
'''
For append operation, we have two functions(same to write)
    1. write(str_data): Single line of data
        --In this, if the file is not present, it will create one then perform write operation
        --If the file is already present, then it will override the prev data with the new one
    2. writelines([line1, line2, ..., linen]): For multiple line of data
'''

