from nltk.translate.ribes_score import corpus_ribes
import sys
import csv

def calculate_ribes(csv_file):
	# Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Define file name of output file
    out_file_name = csv_file.split("/")[-1];

    # Define list of reference, hypothesis
    reference = []
    hypothesis = []
    rows = []

    in_csv = open (csv_file, 'r')
    reader = csv.reader (in_csv)
    for row in reader:
        space_separated_reference = row[1].split(" ");
        space_separated_hypothesis = row[2].split(" ");
        reference.append (space_separated_reference)
        hypothesis.append (space_separated_hypothesis)
        rows.append (row)

    in_csv.close ()

    # Write to csv_file with the results
    out_csv = open ("./data/ribes/"+out_file_name, 'w')
    writer = csv.writer (out_csv)
    writer.writerow (rows[0])

    # Calculate RIBES score.
    for i in range (1, len(rows)):
        try:
            input_re = [[reference[i]]]
            input_hy = [hypothesis[i]]
            #print (input_re, input_hy)
            rows[i][3] = round(corpus_ribes(input_re, input_hy), 4)
            writer.writerow (rows[i])
        except ZeroDivisionError:
            rows[i][3] = 0
            writer.writerow (rows[i])

    print ("Success on calculating RIBES!!")
    out_csv.close()
    # [END calculate_ribes]

if __name__ == '__main__':
    calculate_ribes(sys.argv[1])
