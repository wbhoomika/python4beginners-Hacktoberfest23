"""
    An example program to showcase how we can read/write from/to files in python

    Objective:
        - We have an list of names. Write the names to names.txt file.
        - Read the names from names.txt file and now write it to marks.txt file(each person got some marks in exam)

    Steps: Read and Write operation
        - Open a file
        - Do some opertations(Read from it)
        - Write to another file
        - Close the files


    Contributor:    Anirban Chand
"""

from random import randint

# Open a file in write mode
in_file = open('names.txt', 'w')

# do something
names = ['Levi', 'Eren', 'Mikasa', 'Hange', 'Erwin', 'Armin', 'Grisha', 'Historia', 'Dina', 'Jean', 'Sasha', 'Hitch', 'Hannes', 'Marlo']
for name in names:
    in_file.write(name)
    in_file.write('\n')

in_file.close()


# Open a file 
in_file = open('names.txt', 'r')
out_file = open('marks.txt', 'w')

# Write the headings
out_file.write('Names')
out_file.write('\t\t  \t\t')
out_file.write('Marks\n')
out_file.write('_____')
out_file.write('\t\t  \t\t')
out_file.write('_____\n\n')

# Write names their marks in marks.txt file
for name in in_file:
    marks = randint(30, 100)
    name = name[:-1]
    out_file.write(name)
    out_file.write('\t\t-  \t\t')
    out_file.write(str(marks)+'\n')

in_file.close()
out_file.close()