# import os
import csv
# import pyperclip  #UNCOMMENT WHEN CLIPBOARD MANAGEMENT IS BACK ON THE ROLL

#   constant arrays that are full of the keys and commands corresponding to their array pos
KEYS = []
ACTION = []

#   misc file locations
README_BACKUP = './src/readme.md'
LOGS = './src/logs.txt'
README = './README.md'

DEFAULT_KEYBIND_LIST = '<div id="big-list-of-keybindings"></div>'

#   file location of keybinds
DEFAULT_KEYBIND_LOCATION = './src/keybinds/default.csv'

#   opens the csv and puts its data into a temporary list called tList
tList = []
with open(DEFAULT_KEYBIND_LOCATION, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tList.append(row)

#   checks that i is past the first line (dummy text in the csv)
for i in range(len(tList)):
    if i > 0:
        KEYS.append(tList[i][0])
        ACTION.append(tList[i][1])

#   turn into markdown text to go into the o id ther file for future me to shift over
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

#   logs text output...
logs = open(LOGS, 'w')
logs.write(tReturn)
logs.close()

#   tReturn is the markdown formated list
# print(f'{tReturn} \nwhat do you want done with the output:\n\n1.  copy to clipboard\n2.  append to README.md\n')

tNum = []

my_file = open(README_BACKUP, "r")

# reading the file
data = my_file.read()

data_into_list = data.split("\n")

# printing the data
# print(data_into_list)
for i in range(len(data_into_list)):
    if data_into_list[i] == DEFAULT_KEYBIND_LIST:
        # print(f'\n\nwe got one on line {i}')
        tNum.append(i)
    # print(i)
# print(tReturn)
tReturn = tReturn.split("\n")

tReturn

tReturn.reverse()
for i in range(len(tNum)):
    for v in range(len(tReturn)):
        data_into_list.insert(tNum[i], tReturn[v])
my_file.close()
# print(data_into_list)
read = open(README, "w")
read.write('\n'.join(data_into_list))
read.close()

# print(f'{rmb.read()}\n{tReturn}')

# rmb.close()
# rm.close()


#   UNCOMMENT IF YOU MIGHT WANT TO CLIPBOARD IT...
#
# if input("Type 1 or 2: ") == '1':
#     print('copied to clipboard')
#     pyperclip.copy(tReturn)
# else:
#     tNum = []

#     my_file = open(README_BACKUP, "r")

#     # reading the file
#     data = my_file.read()

#     data_into_list = data.split("\n")

#     # printing the data
#     print(data_into_list)
#     for i in range(len(data_into_list)):
#         if data_into_list[i] == DEFAULT_KEYBIND_LIST:
#             print(f'\n\nwe got one on line {i}')

#             tNum.append(i)
#         # print(i)
#     # print(tReturn)
#     tReturn = tReturn.split("\n")

#     tReturn

#     tReturn.reverse()
#     for i in range(len(tNum)):
#         for v in range(len(tReturn)):
#             data_into_list.insert(tNum[i], tReturn[v])
#     my_file.close()
#     print(data_into_list)
#     read = open(README, "w")
#     read.write('\n'.join(data_into_list))
#     read.close()

#     # print(f'{rmb.read()}\n{tReturn}')

#     # rmb.close()
#     # rm.close()
