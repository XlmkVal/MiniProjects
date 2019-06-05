import os
import re
import csv



def scrub(fileName):
    with open (fileName) as csvFile:
        raw_temp = csv.reader(csvFile)
        print(tuple(raw_temp)[0])

for a,b,c in os.walk(os.getcwd()):
    currentFiles = c
csvList = [csv for csv in currentFiles if re.match('[0-9]*.csv', csv)]

for items in csvList:
    scrub(items)
