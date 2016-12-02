# English Raw Data
# https://www.dropbox.com/s/zuqd6yxzs3id5l7/europarl-v7.es-en.en?dl=1
# Spanish Raw data
# https://www.dropbox.com/s/emzffiti8gmml98/europarl-v7.es-en.es?dl=1


import urllib.request
from pathlib import Path

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

file_english = Path("data/europarl-v7.es-en.en")
if not file_english.is_file():
    download_raw_file("english")

file_spanish = Path("data/europarl-v7.es-en.es")
if not file_spanish.is_file():
    download_raw_file("spanish")
