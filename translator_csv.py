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



"""def run_translator(csv_file):
    # Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Define file name of output file
    out_file_name = csv_file.split("/")[-1];

    # Bunch of corpuses to be translated
    corpuses = []
    rows = []

    in_csv = open(csv_file, 'r')
    reader = csv.reader(in_csv)
    for row in reader:
        corpuses.append(row[0])
        rows.append(row)

    del corpuses[0]
    in_csv.close ()

    # Instantiates a client
    translate_client = translate.Client()

    # The target language
    target = 'es'

    # Write to csv_file with the results
    out_csv = open ("./data/output/"+out_file_name, 'w')
    writer = csv.writer (out_csv)
    writer.writerow (rows[0])
    i = 1

    # Translates some corpuses into Spanish
    for corpus in corpuses:
        translation = translate_client.translate(
            corpus,
            target_language=target)
        #print(u'Text: {}'.format(corpus))
        #print(u'Translation: {}'.format(translation['translatedText']))
        rows[i][2] = translation['translatedText']
        writer.writerow (rows[i])
        i += 1

    print ("Success on translating coupuses!!")
    out_csv.close()
    # [END translator_csv]"""


if __name__ == '__main__':
    run_translator(sys.argv[1])
