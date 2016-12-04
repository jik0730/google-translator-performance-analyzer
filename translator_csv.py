import csv
import sys
# Imports the Google Cloud client library
from google.cloud import translate

target = 'es'

def run_translator(input_filename):
    translate_client = translate.Client()

    results = []

    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            source_sentence = row['english']
            if not detect_sentence(source_sentence):
                continue
            translation = translate_client.translate(
                source_sentence,
                target_language=target)
            translated_text = translation['translatedText']
            result = row
            result['translated_spanish'] = translated_text
            results.append(result)

    filename = input_filename.split('/')[-1].split('.')[0]
    output_filename = 'result/' + filename +  '.csv'
    with open(output_filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish', 'translated_spanish']
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer = csv.writer(sys.stdout, delimiter="|", quoting=csv.QUOTE_NONE, quotechar='')
        writer.writeheader()
        for corpus in results:
            writer.writerow(corpus)


"""
Description: Detecting whether the sentence is not one sentence.
Input (str): A sentence.
Output (str): T/F
"""
def detect_sentence(sentence):
    tokens = sentence.split(" ");
    length = len(tokens)
    for i in range(0, length):
        if tokens[i][-1] == "." and i != length - 1:
            return False

    return True


if __name__ == '__main__':
    run_translator(sys.argv[1])
