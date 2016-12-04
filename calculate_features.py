import csv
import sys
from calculate_grammatical_complexity import calculate_gc

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

            # Feature_3, 4, 5, 6, 7, 8
            gc = calculate_gc(row['english'])
            result['noun'] = gc['noun']
            result['adj'] = gc['adj']
            result['verb'] = gc['verb']
            result['adp'] = gc['adp']
            result['conj'] = gc['conj']
            result['height_of_parse_tree'] = gc['height']

            results.append(result)

    filename = input_filename.split('/')[-1].split('.')[0]

    output_filename = 'result/' + filename +  '.csv'
    with open(output_filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish', 'translated_spanish', 'ribes_score', 'number_of_words', 'number_of_alphabets', 'noun', "adj", "verb", "adp", "conj", "height_of_parse_tree"]
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for corpus in results:
            writer.writerow(corpus)


"""
Description: This is calculating number of words.
Input (list(str)): A sentence separated by ' '(Space) as a list.
Output (int): A value on a sentence.
"""
def feature_1(s):
    return len(s.split(" "))

"""
Description: This is calculating whole length of sentence.
Input (list(str)): A sentence separated by ' '(Space) as a list.
Output (int): A value on a sentence.
"""
def feature_2(s):
    return len(s)


if __name__ == '__main__':
    calculate_features(sys.argv[1])
