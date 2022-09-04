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

stops.update(["–","…","*", " ", "", "highnesses\ndistinguished", "committee\nfellow"])

#FUNCTIONS

def takeSecond(elem):
    return elem[1]

def create_wordlist(file):

    vocab_list = []

    #iterate through each file
    #uses regex to check for more complicated issues in the data

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

            #check that the words are not stopwords
            #stopwords are the most common words in a language
            #in English it's "the", "and", "a", "then", "there", etc.
            #tldr; not relevant to the analysis

            if word not in stops:
                vocab_list.append(word)

        #use the Counter method to create key:value pairs

        most_frequent = col.Counter(vocab_list)
    
    most_frequent_words = []

    #iterate through the counter to form a list so it can be sorted by most frequent words

    for key in most_frequent:
        if most_frequent[key] > 2:
            most_frequent_words.append((key, most_frequent[key]))

    mfw = sorted(most_frequent_words, reverse= True, key = takeSecond)
    
    return mfw


#MAIN

def main(file):

    #ask the user how many words they would like to see

    num = int(input("How many words would you like to see?: "))

    words = create_wordlist(files)

    print(words[0:num-1])

main(files)


