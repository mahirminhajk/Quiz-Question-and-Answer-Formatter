from __future__ import annotations
from asyncore import read
from cgi import print_arguments
from dataclasses import replace
import readline
from tkinter import N
from typing import Tuple
import warnings as W

# class


class Question:
    # __init__ is a constructor, self var is used to assecc other var in the class
    def __init__(self, id, ques,  answer):
        self.id = id
        self.ques = ques
        self.answer = answer
# end class

# function area


def idCollector(line):  # please delete this
    strId = ""
    if line[:2] == " ":
        strId = line[:1]
    elif line[:2] != " ":
        strId = line[:2]
    else:
        strId = line[:3]
    return strId
# end function area


# array
getIntoLines = []
teResult = []
questions = []
allAnswers = []
answer = []
# ene array

# open
with open("I:\\PYthonProjects\\automatic a txt file\\text1.txt", "r") as sourceFile:
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


def next_option(optionLetter):
    if optionLetter == "a":
        return "b"
    elif optionLetter == "b":
        return "c"
    elif optionLetter == "c":
        return "d"
    elif optionLetter == "d":
        return "d"


def optionSearcher(answer, anss, optionLetter, searchStarter, searchEnd):
    while True:
        indexOFOpLet = anss.find(optionLetter, searchStarter, searchEnd)
        if anss[indexOFOpLet + 1] == ")":
            # we got answer
            nextOption = next_option(optionLetter)
            while True:
                indexOfNOP = anss.find(nextOption, searchStarter, searchEnd)
                if anss[indexOfNOP + 1] == ")":
                    answer.append(anss[searchStarter:indexOfNOP])
                    break

            break
        searchStarter = indexOFOpLet + 1


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


# end solving area


# saving
with open("I:\\PYthonProjects\\automatic a txt file\\result.txt", "w") as resultfile:  # "w" will overwrite id
    for i in allAnswers:
        resultfile.write(i)
        resultfile.write("\n")
# end saving

# test print
print("Program exited")
# end test print
