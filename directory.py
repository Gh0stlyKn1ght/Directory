#Juan Nevarez
#CIS245
#assignment 8.1
#9/28/2020

import os

path = "C:/Users/NEO/PycharmProjects/pythonProject5/"


def main():
    directory = input("lordnikon@linux:~$ directory? ")
    filename = input("lordnikon@linux:~$ filename?")
    name = input("lordnikon@linux:~$ name?")
    address = input("lordnikon@linux:~$ address?")
    phone_number = input("lordnikon@linux:~$ phone# number?")
    if os.path.isdir(directory):
        writefile = open(os.path.join(directory, filename), 'w')
        writefile.write(name + ',' + address + ',' + phone_number + '\n')
        writefile.close()

        print("lordnikon@linux:~$ File contents:")
        readfile = open(os.path.join(directory, filename), 'r')
        for line in readfile:
            print(line)
        readfile.close()
    else:
        print("Incorrect directory, try again.")


main()
