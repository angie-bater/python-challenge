import os
import csv
csvpath = os.path.join("./","**PyBank**","budget_data.csv")
# open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    total_months = 0
        
    for row in csvreader:
        total_months= total_months+1
    total_months = total_months-1
print(total_months)
 # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
 for row in csvreader:
        print(row)
        total_months = 0


   