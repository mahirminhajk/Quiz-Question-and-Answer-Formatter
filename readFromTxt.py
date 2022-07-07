from dataclasses import replace
import readline


import readline

listOfMacs = []
# open the file
# "r" -read, "w" - write "a" - append
with open("I:\\PYthonProjects\\automatic a txt file\\text.txt", "r") as reader:
    for line in reader.readlines():  # foreach loop
        listOfMacs.append(line)


RemoveDash = []
RemoveLine = []
NewMacs = []

for mac in listOfMacs:
    whatWeNeed = mac.replace(":", "-")
    RemoveDash.append(whatWeNeed)

for mac in RemoveDash:
    whatWeNeed = mac.replace("\n", "")
    RemoveLine.append(whatWeNeed)

for mac in RemoveLine:
    whatWeNeed = mac.upper()
    NewMacs.append(whatWeNeed)

with open("I:\\PYthonProjects\\automatic a txt file\\textready.txt", "w") as newfile:
    for i in NewMacs:
        newfile.write(i)
        newfile.write("\n")
