#IMPORTS

import os
import nltk
import re
import collections as col
from nltk.corpus import stopwords
from pathlib import Path

#GLOBALS

#define the path where the speech files are found
path = Path.cwd()/ "nobelspeeches"

nobel_speeches = os.listdir(path)

#join the path with the files to find the appropriate file when looking for it
files = sorted([os.path.join(path, file) for file in nobel_speeches if file.endswith('.txt')])

stops = set(stopwords.words('english'))

stops.update(["–","…","*", " ", ""])

#FUNCTIONS

def create_wordlist(file):

    vocab_list = []

    for file in files:

        file1 = open(file, encoding = "utf8")
        file2 = file1.read()
        file3 = re.sub("\b\W?(\w*)\W?\b", r"/1", file2)
        file4 = re.sub(r"[\b?\(\n*)](\w*)[\(\n*)\b?]", r" \1", file3)
        file4 = re.sub(r"\\n*", " ", file3)
        file5 = re.sub(r"(,|;|:|\.|)?(\w*)(,|;|:|\.|)?", r"\2", file4)
        file5.replace("\n", " ")
        lst = file5.lower().split(" ")

        for word in lst:
            if word.startswith("\'"):
                pass
            elif word not in stops:
                vocab_list.append(word)\

        most_frequent_words = col.Counter(vocab_list)

    print(most_frequent_words)

#MAIN

def main(file):

    create_wordlist(files)

main(files)



