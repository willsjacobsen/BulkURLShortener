#tk

import csv

from pyshorteners import Shortener

inputfile= 'input.csv'
outputfile= 'output.csv'
def readFile(inputfile):
    your_list = []
    with open( inputfile, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        for url in f:
            your_list.append(url)
    return your_list

def readFile(inputfile):
    your_list = []
    with open( inputfile, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

def write_file(outputfile,shortenList):
    listFile = open(outputfile, 'w+')
    writer = csv.writer(listFile)

    for item in shortenList:
        word = ''.join(item)
        writer.writerow([word])


def tinyURLShortner(inputlist):
    short = Shortener('Tinyurl', timeout=9000)
    outputlist=[]
    for url in inputlist :
        shortenURL=short.short(''.join(url))
        outputlist.append(shortenURL)
    return outputlist


def main():
    # print readFile(inputfile)
    inputlist = readFile(inputfile)
    outputlist = tinyURLShortner(inputlist)
    print(outputlist)
    write_file(outputfile,outputlist)


if __name__ == '__main__':
    main()
