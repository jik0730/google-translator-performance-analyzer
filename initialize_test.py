# English Raw Data
# https://www.dropbox.com/s/zuqd6yxzs3id5l7/europarl-v7.es-en.en?dl=1
# Spanish Raw data
# https://www.dropbox.com/s/emzffiti8gmml98/europarl-v7.es-en.es?dl=1


import urllib.request
from pathlib import Path
import sys, csv

def download_raw_file(language):
    if language == "english":
        url_english = "https://www.dropbox.com/s/zuqd6yxzs3id5l7/europarl-v7.es-en.en?dl=1"
        filename_english = "data/europarl-v7.es-en.en"
        urllib.request.urlretrieve(url_english, filename_english)
    elif language == "spanish":
        url_spanish = "https://www.dropbox.com/s/emzffiti8gmml98/europarl-v7.es-en.es?dl=1"
        filename_spanish = "data/europarl-v7.es-en.es"
        urllib.request.urlretrieve(url_spanish, filename_spanish)
    else:
        print("error")

def combine_raw_files_to_csv(filename, number_of_lines):
    #from itertools import izip
    parallel_corpus = []

    with open("data/europarl-v7.es-en.en") as textfile1, open("data/europarl-v7.es-en.es") as textfile2:
        i = 0
        for x, y in zip(textfile1, textfile2):
            x = x.strip()
            y = y.strip()
            line = {
                "english": x,
                "spanish": y
            }
            parallel_corpus.append(line)

            i = i + 1
            if i > number_of_lines:
                break

    with open(filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish']
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONE)
        writer.writeheader()
        for corpus in parallel_corpus:
            writer.writerow(corpus)

file_english = Path("data/europarl-v7.es-en.en")
if not file_english.is_file():
    download_raw_file("english")

file_spanish = Path("data/europarl-v7.es-en.es")
if not file_spanish.is_file():
    download_raw_file("spanish")

if len(sys.argv) is not 3:
    print("2 arguments filename, number of lines to extract are needed")
else:
    filename = sys.argv[1]
    number_of_lines = int(sys.argv[2])

    combine_raw_files_to_csv(filename, number_of_lines)
