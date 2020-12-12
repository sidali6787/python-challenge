# 1st Step is to import the required modules
import os
import csv
# Getting the CVS data file 
csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')
output_path= os.path.join("PyPoll","analysis","Final_Analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    data = []
    
    for row in csvreader:
        data.append(row)
    print("Election Results")
    print("----------------------------")
#   * The total number of votes cast
    print(f'Total Voters Cast: {len(data)}')
    print("----------------------------")
# * A complete list of candidates who received votes. 
#   Creating 4 variables to count each candidiates votes.
    khan=0
    correy=0
    li=0
    tooley=0
    for b in data: 
        if b[2]=="Khan":
            khan=khan+1
        elif b[2]=="Correy":
            correy=correy+1
        elif b[2]=="Li":
            li=li+1
        elif b[2]=="O'Tooley":
            tooley=tooley+1
    print(f'Khan: {(khan/len(data)*100):.3f}% ({khan})')
    print(f'Correy: {(correy/len(data)*100):.3f}% ({correy})')
    print(f'Li: {(li/len(data)*100):.3f}% ({li})')
    print(f"O'Tooley: {(tooley/len(data)*100):.3f}% ({tooley})") 
    print("----------------------------")
#   Comparing the votes of each candidiates with the winner_votes and printing the winner. 
    winner= ""
    winner_votes=0
    if winner_votes<khan: 
        winner_votes=khan
        winner="Khan"
    if winner_votes<correy: 
        winner_votes=correy
        winner="Correy"
    if winner_votes<li: 
        winner_votes=li
        winner="Li"
    if winner_votes<tooley: 
        winner_votes=tooley
        winner="O'Tooley"
    print(f'Winner: {winner}')
    print("----------------------------")
#   Getting the output file to store our analysis.
with open(output_path,"w") as writer:
    writer.write("Election Results\n")
    writer.write("----------------------------\n")
    writer.write(f'Total Voters Cast: {len(data)}\n')
    writer.write("----------------------------\n")
    writer.write(f'Khan: {(khan/len(data)*100):.3f}% ({khan})\n')
    writer.write(f'Correy: {(correy/len(data)*100):.3f}% ({correy})\n')
    writer.write(f'Li: {(li/len(data)*100):.3f}% ({li})\n')
    writer.write(f"O'Tooley: {(tooley/len(data)*100):.3f}% ({tooley})\n") 
    writer.write("----------------------------\n")
    writer.write(f'Winner: {winner}\n')
    writer.write("----------------------------\n")




