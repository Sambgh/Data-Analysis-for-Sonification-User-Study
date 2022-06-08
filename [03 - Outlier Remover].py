import numpy
from pandas import *
import pandas as pd
import csv

# reading CSV file
data = read_csv("05 - Method 5 - Granular Audio + Visual (blanks removed).csv")

# name of csv file that we want to write into
filenameToWrite = "05 - Method 5 - Granular Audio + Visual (removed outliers).csv"

# converting column data to list
col1 = data['Completion Time'].tolist()
col2 = data['Distance Error'].tolist()
col3 = data['Angle Error'].tolist()

elements1 = numpy.array(col1)
elements2 = numpy.array(col2)
elements3 = numpy.array(col3)

mean1 = numpy.mean(elements1, axis=0)
sd1 = numpy.std(elements1, axis=0)
mean2 = numpy.mean(elements2, axis=0)
sd2 = numpy.std(elements2, axis=0)
mean3 = numpy.mean(elements3, axis=0)
sd3 = numpy.std(elements3, axis=0)

final_list1 = [x for x in col1 if (x > mean1 - 3 * sd1)]
final_list1 = [x for x in final_list1 if (x < mean1 + 3 * sd1)]
final_list1.insert(0, "Completion Time:")
print('Completion Time:', col1)     # print original
print('Corrected Time :', final_list1)                  # print after removing outliers

final_list2 = [x for x in col2 if (x > mean2 - 3 * sd2)]
final_list2 = [x for x in final_list2 if (x < mean2 + 3 * sd2)]
final_list2.insert(0, "Distance Error:")
print('Distance Error:', col2)      # print original
print('Corrected Err :', final_list2)                  # print after removing outliers

final_list3 = [x for x in col3 if (x > mean3 - 3 * sd3)]
final_list3 = [x for x in final_list3 if (x < mean3 + 3 * sd3)]
final_list3.insert(0, "Angle Error:")
print('Angle Error:', col3)         # print original
print('Corrected  :', final_list3)                  # print after removing outliers

#  r1 = zip(final_list1, final_list2, final_list3)
#  r2 = zip(final_list2)
#  r3 = zip(final_list3)

# writing to csv file
# with open(filenameToWrite, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
#
#     # writing the fields
#     fieldsToWrite = ['Completion Time', 'Distance Error', 'Angle Error']
#     csvwriter.writerow(fieldsToWrite)

with open(filenameToWrite, "a") as csvfile:
    w = csv.writer(csvfile)
    w.writerow(final_list1)
    w.writerow(final_list2)
    w.writerow(final_list3)

