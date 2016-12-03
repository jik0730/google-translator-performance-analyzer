import sys
from translator_csv import run_translator
from calculate_ribes import calculate_ribes
from calculate_features import calculate_features
from calculate_grammatical_complexity import calculate_grammatical_complexity

def main(csv_file):
	# Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Define file name of output file
    #out_file_name = csv_file.split("/")[-1];

    #run_translator("data/es-en.csv")
    calculate_ribes("result/es-en.csv")
    calculate_features("result/es-en.csv")
    calculate_grammatical_complexity("result/es-en.csv")

    #calculate_ribes("data/output/"+out_file_name)
    #calculate_features("data/ribes/"+out_file_name)

    print("Success on executing main!!")

if __name__ == '__main__':
    main(sys.argv[1])
