# BULK FILES RENAMER
# Renames all the files in a folder as the user specifies the name and format
import os

print('Welcome to your Bulk Files Renamer!\n')

def main():
    i = 0

    print('Path example: C:/Users/user/folder/')
    path = input('Please enter the directory path (as the example above) of the folder where the files to be renamed are:\n')
    name = input('New name of the files: ')
    format = input('Format of the files(Ex:.jpg): ')

    for filename in os.listdir(path):
        my_dest = name + str(i) + format
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__' :
    main()

print('Task done! Hope to see you again :)')    