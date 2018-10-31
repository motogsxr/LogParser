#!/usr/bin/env python

finalFile = open("result.txt", "a+")
FileToBeParsed = input('Input filename: ')

for line in open (FileToBeParsed):
    if "test" in line:
        finalFile.write(line)
finalFile.write('\n')
finalFile.close()