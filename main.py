import sys
from translator_csv import run_translator
from calculate_ribes import calculate_ribes
from calculate_features import calculate_features

def main(csv_file):
	# Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Define file name of output file
    #out_file_name = csv_file.split("/")[-1];

    run_translator(csv_file)
    #calculate_ribes("data/output/"+out_file_name)
    #calculate_features("data/ribes/"+out_file_name)

    print("Success on executing main!!")

if __name__ == '__main__':
    main(sys.argv[1])
