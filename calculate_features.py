import csv
import sys

def calculate_features(input_filename):
    if input_filename.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    results = []

    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            result = row
            result['number_of_words'] = feature_1(row['english'])
            result['number_of_alphabets'] = feature_2(row['english'])
            #result['feature3'] = feature_3(row['english'])

            results.append(result)

    filename = input_filename.split('/')[-1].split('.')[0]

    output_filename = 'result/' + filename +  '.csv'
    with open(output_filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish', 'translated_spanish', 'ribes_score', 'number_of_words', 'number_of_alphabets']
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for corpus in results:
            writer.writerow(corpus)




"""
Description: This is calculating number of words.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""
def feature_1(s):
    return len(s.split(" "))

"""
Description: This is calculating whole length of sentence.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""
def feature_2(s):
    return len(s)

"""
Description: This is calculating average length of words.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""



if __name__ == '__main__':
    calculate_features(sys.argv[1])
