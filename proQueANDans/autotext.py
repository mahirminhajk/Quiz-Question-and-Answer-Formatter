from __future__ import annotations
from asyncore import read
from cgi import print_arguments
from dataclasses import replace
import readline
from tkinter import N
from typing import Tuple
import warnings as W

# main section
totalQuestion = 16
# END main section

# array
getIntoLines = []
questions = []  # all quesiton here
allAnswers = []
answer = []  # all correct answer here
result = []  # the final result here
# ene array

# open
with open("I:\\PYthonProjects\\automatic a txt file\\proQueANDans\\paper.txt", "r") as sourceFile:
    for line in sourceFile.readlines():
        getIntoLines.append(line)
# end open

# solving area
# question and answer separate and save into different list


def quAsSeparater(questions, allAnswers, line):
    indexQFinsher = line.find("(")
    ques = line[:indexQFinsher]
    questions.append(ques)

    indexAnsStarter = len(line) - indexQFinsher
    ans = line[-indexAnsStarter:]
    allAnswers.append(ans)


for line in getIntoLines:
    quAsSeparater(questions, allAnswers, line)

# answering

   # parent function


def optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd):
    while True:
        indexOFOpLet = anss.find(optionLetter, searchStarter, searchEnd)
        if anss[indexOFOpLet + 1] == ")":
            # we got answer
            correct_option_picker(answer, anss, searchEnd, indexOFOpLet)

            break
        searchStarter = indexOFOpLet + 1

    # child function


def correct_option_picker(answer, anss, searchEnd, indexOFOpLet):
    allOptions = anss[indexOFOpLet:searchEnd]
    if allOptions[0] != "d":
        splits = allOptions.split("  ", 1)
        answer.append(splits[0])
    else:
        answer.append(allOptions[0:(len(allOptions)-1)])


for anss in allAnswers:
    indexOfAns = 10
    optionLetter = anss[indexOfAns].lower()
    searchStarter = 12
    searchEnd = len(anss)
    if optionLetter == "a":
        optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd)
    elif optionLetter == "b":
        optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd)
    elif optionLetter == "c":
        optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd)
    elif optionLetter == "d":
        optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd)
    else:
        W.warn("The option not find")


for i in range(totalQuestion):
    result.append(questions[i] + " " + answer[i])


# end solving area


# saving
with open("I:\\PYthonProjects\\automatic a txt file\\proQueANDans\\result.txt", "w") as resultfile:  # "w" will overwrite id
    for i in result:
        resultfile.write(i)
        resultfile.write("\n")
# end saving

# test print
print("Program exited")
# end test print
