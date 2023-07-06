import os
import csv
#function for average
def average(list):
    all = sum(list)
    dist=len(list)
    av= all/dist
    return av
#read in
budget_csv = os.path.join(r"C:\Users\slbow\Documents\Analysis Projects\pyrep\Python_challenge\PyBank\resources\budget_data.csv")
#lists
dates = []
profits = []
changes = []
#read in, do work
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    #Create lists
    for row in csv_reader:
            dates.append(row[0]) 
            profits.append(row[1])
    #length of sample
    months = (len(dates))
    #destring profits list
    profits = [int(i) for i in profits]
    #populate list 3
    for x in range(len(profits)):
        if x > 0:
            diff = profits[x] - profits[x-1]
            changes.append(diff)
    #Find totals and some formatting
    total = sum(profits)
    dollars = "$" + str(total)
    print(dollars)
    #Total and average changes
    rang_chang = len(changes)
    total_change= changes[rang_chang-1]-changes[0]
    print(total_change)

    avg_change = average(changes)
    print(avg_change)
    #Minimum and maximum
    maximum = changes.index(max(changes))
    minimum = changes.index(min(changes))
    most =max(changes)
    print(most)
    least =min(changes)
    print(least)
    bigmonth =dates[maximum + 1]
    smallmonth = dates[minimum + 1]
    print(bigmonth)
    print(smallmonth)
#Write text files with a list
texts = ["Months:", months, "Total Profits:", dollars,"Total Changes:", total_change, "Average Change:",avg_change, "Greatest Increase Month:", bigmonth,"Increase:", most, "Greatest Decrease Month:", smallmonth, "Decrease:", least]
output_file = os.path.join(r"C:\Users\slbow\Documents\Analysis Projects\pyrep\Python_challenge\PyBank\analysis\results.txt")
with open(output_file, "w") as t:
    for text in texts:
        t.write(str(text))
        t.write('\n')
    
    