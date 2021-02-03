import csv
import argparse
import sys

from helpers import get_new_csv_structure

parser = argparse.ArgumentParser('csv')
parser.add_argument('csv', help='A csv file which will be processed by the script')
args = parser.parse_args()


if len(sys.argv) == 2:

    if not args.csv.endswith('.csv'):
        sys.exit('Please provide a CSV file')

    with open(args.csv) as csvFile:
        overall_list = []

        reader = csv.reader(csvFile, delimiter=',')
        for line in reader:
            overall_list.append(line)

    new_csv_structure = get_new_csv_structure(overall_list=overall_list)

    new_file_path = args.csv[:-4]  # This removes the .csv from the input file path

    with open(new_file_path+'_output.csv', 'w') as outputCsvFile:
        writer = csv.writer(outputCsvFile, delimiter=',')
        for line in new_csv_structure:
            writer.writerow(line)

else:
    sys.exit('Please only provide two arguments on command line the script interpolation.py and the input CSV file')











