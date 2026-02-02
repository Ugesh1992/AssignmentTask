#Task 1: Read a File and Handle Errors

import os
# with : read a file with automatically close the file
filename= "Sample.txt"
if os.path.exists(filename):
    print('file exists')
    with open(filename, 'rt') as fh:
        content = fh.read()
    print(content)
else:
    print('file not exists')


#Task 2: Write and Append Data to a File

str = input("Enter text to be write in a file : ")
with open("Output.txt", 'wt') as fh:
    fh.write(str)
    print(f"Data successfully written to Output.txt")
appendstr = input("Enter additional text to append : ")
with open("Output.txt", 'at') as fh1:
    fh1.write("\n" + appendstr)
    print(f"Data successfully appended")

print("Final Content: ")
with open("Output.txt", 'rt') as fh2:
    content = fh2.read()
print(content)




