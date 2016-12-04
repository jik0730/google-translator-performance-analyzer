from nltk.translate.ribes_score import corpus_ribes
import sys
import csv

def calculate_ribes(input_filename):
    if input_filename.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    results = []

    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            reference_sentence = row['spanish'].split(" ")
            hypothesis = row['translated_spanish'].split(" ")

            try:
                score = round(corpus_ribes([[reference_sentence]], [hypothesis]), 4)
            except ZeroDivisionError:
                score = 0

            result = row
            result['ribes_score'] = score
            results.append(result)

    filename = input_filename.split('/')[-1].split('.')[0]

    output_filename = 'result/' + filename +  '.csv'
    with open(output_filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish', 'translated_spanish', 'ribes_score']
        
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for corpus in results:
            writer.writerow(corpus)

    print("Success on calculating RIBES scores!!")
            

if __name__ == '__main__':
    calculate_ribes(sys.argv[1])
