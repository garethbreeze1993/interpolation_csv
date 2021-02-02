A simple python script which takes in a file Input in the form of a comma-separated file (CSV) in which rows are 
    separated by newline characters and the value of each column within a row 
    is separated by a comma. 

In the ouput the missing values from the input have been interpolated as the average of all 
non-diagonal neighbouring values. 

Output is in the same form as the input, and have the same number of rows 
    and columns, but contains no missing values.

To use this tool in the command line navigate to the directory which contains the python file interpolation.py.
Then simply run the command python interpolation.py path_to_csv_file

The result will be a CSV file named the original CSV file plus output.csv

e.g. data.csv will return data_output.csv

Also the output CSV file will be present in the same directory as the input CSV file

As long as the user has Python 3 installed on their computer they should be able to run this program as I have only used packages from Pythons standard library

Tests are run from the directory using the command python tests.py