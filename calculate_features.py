import csv
import sys

def calculate_features(csv_file):
    # Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Define file name of output file
    out_file_name = csv_file.split("/")[-1];

    # Define input sentences for input of feature functions
    input_sentences = []
    rows = []

    in_csv = open (csv_file, 'r')
    reader = csv.reader (in_csv)
    for row in reader:
        space_separated_sentence = row[0].split(" ");
        input_sentences.append(space_separated_sentence)
        rows.append (row)

    in_csv.close ()

    # Calculate feature values on input sentences
    out_feature_1 = feature_1(input_sentences)
    out_feature_2 = feature_2(input_sentences)
    out_feature_3 = feature_3(input_sentences)
    # Add more feature functions here...

    # Write to csv_file with the results
    out_csv = open ("./data/features/"+out_file_name, 'w')
    writer = csv.writer (out_csv)
    writer.writerow (rows[0])

    # Calculate RIBES score.
    for i in range (1, len(rows)):
        rows[i][4] = out_feature_1[i]
        rows[i][5] = out_feature_2[i]
        rows[i][6] = out_feature_3[i]
        # Add more feature functions here...
        writer.writerow (rows[i])

    print ("Success on calculating feature values!!")
    out_csv.close()


"""
Description: This is calculating number of words.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""
def feature_1(s_list):
    toReturn = []
    for s in s_list:
        toReturn.append(len(s))
    return toReturn

"""
Description: This is calculating whole length of sentence.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""
def feature_2(s_list):
    toReturn = []
    for s in s_list:
        count = 0;
        for c in s:
            count += len(c) + 1
        count -= 1;
        toReturn.append(count)
    return toReturn

"""
Description: This is calculating average length of words.
Input (list(list(str))): list of sentences separated by ' '(Space).
Output (list(int)): list of values on each sentence.
"""
def feature_3(s_list):
    toReturn = []
    for s in s_list:
        count = 0;
        total_words_length = 0;
        for c in s:
            count += 1
            total_words_length += len(c)
        toReturn.append(round(total_words_length/count, 4))
    return toReturn


if __name__ == '__main__':
    calculate_features(sys.argv[1])
