import sys
from translator_csv import run_translator
from calculate_ribes import calculate_ribes
from calculate_features import calculate_features

def main(csv_file):
	# Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    #run_translator("data/es-en.csv")
    #calculate_ribes("result/es-en.csv")
    calculate_features("result/es-en.csv")

    print("Success on executing main!!")

if __name__ == '__main__':
    main(sys.argv[1])
