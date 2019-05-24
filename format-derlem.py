import collections
import re
import os
from pathlib import Path

"""
Formats derlem.txt and writes formatted questions to test_questions.txt which can be used for evaluation
"""

questions = []
# Change the encoding of the input file to latin-1
file_content = ""
with open("soru_gruplari.txt", encoding="utf-16") as f:
    file_content = f.read()
# Read the file and append all of the lines
question_groups = file_content.split("\n\n")

for group in question_groups:
    lines = group.split("\n")
    for line in lines:
        ID = re.findall("(.*):", line)[0]
        sentence = re.findall(": (.*)", line)[0]
        if ID[0] == 'S':  # if the sentence is a question
            questions.append(sentence)

os.mkdir("test_data")

cwd = os.getcwd()
file_name = cwd + '/test_data/test_questions.txt'

with open(Path("test_data") / "test_questions.txt", 'w+', encoding='utf16') as f:
    f.write('\n'.join(questions))