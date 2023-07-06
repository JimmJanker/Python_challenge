import os
import csv
#Read in csv
budget_csv = os.path.join(r"C:\Users\slbow\Documents\Analysis Projects\pyrep\Python_challenge\PyPoll\resources\election_data.csv")
#create counting variables
candidatec=0
candidateb=0
candidatea=0
count=0
#Read in 
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#vote counting
    for row in csv_reader:
        count = count + 1
        if str(row[2]) == "Charles Casper Stockham":
            candidatec = candidatec+1
        elif  str(row[2]) == "Diana DeGette":
            candidateb = candidateb+1
        elif str(row[2]) == "Raymon Anthony Doane":
            candidatea = candidatea + 1
    #total votes and total voters
    print(str(candidatea))
    print(str(candidateb))
    print(str(candidatec))
    print(count)
    #make into percentages
    stock_perc = str((candidatec/count)*100 )+ '%'
    deg_perc = str((candidateb/count)*100) +'%'
    doa_perc = str((candidatea/count)*100) + '%'
    print(stock_perc)
    print(deg_perc)
    print(doa_perc)
    #decide a winner
    if stock_perc > deg_perc:
        if stock_perc>doa_perc:
            winner = "Charles Casper Stockham"
            
    if deg_perc > stock_perc:
        if deg_perc>doa_perc:
            winner = "Diana DeGette"
    if doa_perc > stock_perc:
        if doa_perc >deg_perc:
            winner= "Raymon Anthony Doane"
    print(winner)
    #winner ^^^ yay!!!
#Creating text file from list
texts = ["Voters:", count, "Charles Casper Stockham", stock_perc, "Diana DeGette",deg_perc, "Raymon Anthony Doane", doa_perc,"The Winner is:", winner]
output_file = os.path.join(r"C:\Users\slbow\Documents\Analysis Projects\pyrep\Python_challenge\PyPoll\analysis\results.txt")
with open(output_file, "w") as t:
    for text in texts:
        t.write(str(text))
        t.write('\n')
            

