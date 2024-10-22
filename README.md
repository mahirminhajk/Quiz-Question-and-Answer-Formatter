# Quiz Question and Answer Formatter

This Python project processes a text file containing quiz questions and answers, and formats the output with the correct answers. The project reads questions and their corresponding answers from a file, processes them to extract the correct options, and saves the formatted results to a new file.

## 📚 Project Overview

During my first semester of college, I encountered a bulk of questions for my study. Each question was accompanied by multiple-choice options, but it was a challenge to identify and format the correct answers amidst the confusion. To streamline this process, I developed a Python script to automatically extract and format the correct answers from a list of questions and options.

## 🎯 Objective

The objective of this project was to:
1. Parse a set of multiple-choice questions.
2. Extract the correct answer for each question.
3. Format the questions and correct answers into a clear, readable format.

## 🛠️ How It Works

The script takes a text file with multiple-choice questions and answers as input. It processes each line to separate questions and their corresponding answers. It then identifies the correct answer based on a designated option letter and formats the output.

## Features

- Reads quiz questions and answers from a text file.
- Extracts and formats correct answers.
- Saves formatted questions and answers to a new text file.

## Input

The input file (`paper.txt`) should contain quiz questions and answers in the following format:
```
1 World Environment Day (Answer : A) a) 5th June b) 5th July c) 5th August d) 5th September
2 The biggest award for environmental activities in India is given in the name of an individual. In whose name is it constituted? (Answer : C) a) Lal Bahadur Shasthri b) Morarji Desai c) Indira Gandhi d) Kamaraj
```
## Output

The output file (`result.txt`) will contain formatted questions with their correct answers:
```
1 World Environment Day a) 5th June
2 The biggest award for environmental activities in India is given in the name of an individual. In whose name is it constituted? c) Indira Gandhi
3 All forms of water that comes down on Earth, including rain, snow, hail etc. is known as _____________ c) Precipitation
```
## Notes

- Ensure that the file paths in the script are correctly set to match your environment.
- This project is no longer actively maintained.

