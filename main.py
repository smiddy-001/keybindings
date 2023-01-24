# import os
import csv
import pyperclip

#   constant arrays that are full of the keys and commands corresponding to their array pos
KEYS                    = []
MODE                    = []
ACTION                  = []
README_BACKUP           = './src/readme.md'
LOGS                    = './src/logs.txt'
README                  = './README.md'

DEFAULT_KEYBIND_LIST    = '<div id="big-list-of-keybindings"></div>'

DATA_LOCATION           = './src/data.csv'

#   opens the csv and puts its data into a temporary list called tList
tList = []
with open(DATA_LOCATION, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tList.append(row)

#   checks that i is past the first line (dummy text in the csv)
for i in range(len(tList)):
    if i > 0:
        KEYS.append(tList[i][0])
        MODE.append(tList[i][1])
        ACTION.append(tList[i][2])


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

tReturn += f"|{tList[0][0]}|{tList[0][1]}|{tList[0][2]}|\n|:-|:-|:-|\n"
for characters_in_list in range(len(KEYS)):
    tReturn += f"|{KEYS[characters_in_list]}|{MODE[characters_in_list]}|{ACTION[characters_in_list]}|\n"

#   logs text output...
logs = open(LOGS, 'w')
logs.write(tReturn)
logs.close()

#   tReturn is the markdown formated list
print(f'{tReturn} \nwhat do you want done with the output:\n\n1.  copy to clipboard\n2.  append to README.md\n')
if input("Type 1 or 2: ") == '1':
    print('copied to clipboard')
    pyperclip.copy(tReturn)
else:
    print('appending to readme.md')