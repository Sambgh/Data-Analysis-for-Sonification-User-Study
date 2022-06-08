# import necessary libraries
import pandas as pd
import os
import glob
import csv
from Tools.scripts.dutree import display

# use glob to get all the csv files in the folder

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

# name of csv file that we want to write into
filenameToWrite = "05 - Method 5 - Granular Audio + Visual.csv"

# writing to csv file
with open(filenameToWrite, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    fieldsToWrite = ['File Name', 'Completion Time', 'Distance Error', 'Angle Error']
    csvwriter.writerow(fieldsToWrite)


# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f)
    fields = []
    rows = []
    RowsToWrite = []

    # reading csv file
    filename = os.path.basename(f)
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % csvreader.line_num)

        lastSec = rows[-1][11]
        firstSec = fields[11]
        CompletionTime = float(lastSec) - float(firstSec)
        CompletionTimeStr = str(CompletionTime)
        DistanceError = rows[-1][1]
        AngleError = rows[-1][4]
        fileNameStr = f.split("\\")[-1]
        currentRow = [fileNameStr, CompletionTimeStr, DistanceError, AngleError]
        RowsToWrite.append(currentRow)
        print("File Name: " + fileNameStr + ", Completion Time: " + CompletionTimeStr + ", " + "Distance Error: " + DistanceError + ", Angle Error: " + AngleError)

        # writing to csv file
        with open(filenameToWrite, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the data rows
            csvwriter.writerows(RowsToWrite)






    # printing the field names
    # print('Field names are:' + ', '.join(field for field in fields))

    #  printing first 5 rows
    # print('\nFirst 5 rows are:\n')
    # for row in rows[:5]:
    #     # parsing each column of a row
    #     for col in row:
    #         print("%10s" % col, end=" "),
    #     print('\n')

    # print the location and filename
    # print('Location:', f)
    # print('File Name:', f.split("\\")[-1])

