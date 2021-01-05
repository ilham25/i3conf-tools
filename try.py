#!/usr/bin/python

# text_file = open("sample.txt", "a")
# n = text_file.write("LINE \n")
# text_file.close()

# read input file
fin = open("sample.txt", "rt")
# read file contents to string
data = fin.read()
# replace all occurrences of the required string
data = data.replace('ini adalah say', 'ini adalah kamu')
data = data.replace("kita berada disini", 'kita berada disitu')


# close the input file
fin.close()
# open the input file in write mode
fin = open("sample.txt", "wt")
# overrite the input file with the resulting data
fin.write(data)
# close the file
fin.close()
