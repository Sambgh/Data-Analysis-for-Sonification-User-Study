import csv
in_fnam = "05 - Method 5 - Granular Audio + Visual.csv"
out_fnam = "05 - Method 5 - Granular Audio + Visual (blanks removed).csv"

with open(in_fnam, newline='') as in_file:
    with open(out_fnam, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)