import csv

#   constant arrays that are full of the keys and commands corresponding to their array pos
KEYS        = []
ACTION    = []

#   opens the csv and puts its data into a temporary list called tList
tList = []
with open('./root-keybinds/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tList.append(row)

#   checks that i is past the first line (dummy text in the csv)
for i in range(len(tList)):
    if i > 0:
        KEYS.append(tList[i][0])
        ACTION.append(tList[i][1])

#   turn into markdown text to go into the other file for future me to shift over
#
#   |Keys|Action|
#   |:-|:-|
#   |C w|close tab|
#   |C W|close all tabs|
#   |M q|quit window|   
#

#   tReturn is the val passed into return later...
tReturn = ""

tReturn += f"|{tList[0][0]}|{tList[0][1]}|\n|:-|:-|\n"
for characters_in_list in range(len(KEYS)):
    tReturn += f"|{KEYS[characters_in_list]}|{ACTION[characters_in_list]}|\n"

#   tReturn is the markdown formated list
print(tReturn)