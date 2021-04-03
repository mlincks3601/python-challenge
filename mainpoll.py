import os
import csv
#set our path for the computer to find our csv file
pypoll_csv = os.path.join("Resources", "election_data.csv") 

candidate = []
vote_count = []
correy_votes = 0
li_votes= 0
khan_votes = 0
OTooley = 0
percentage = {}
winner = []

total_votes = 0


with open (pypoll_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
#going to manually put in our counter for our data
    for row in csvreader:
        total_votes += 1
        row_candidate = row[2]
        if row_candidate == "Khan":
            khan_votes += 1
        elif row_candidate == "Li":
            li_votes += 1
        elif row_candidate == "O'Tooley":
            OTooley += 1
        elif row_candidate == "Correy":
            correy_votes += 1
#going to compare between votes to help us declare our winner and to find our averages later on
    if (khan_votes > li_votes) and (khan_votes > OTooley) and (khan_votes > correy_votes):
        winner = "Khan"
    elif (li_votes > OTooley) and (li_votes > correy_votes):
        winner = "li"
    elif (OTooley > correy_votes) and (OTooley > li_votes) and (OTooley > li_votes):
        winner = "OTooley"
    else : 
        winner = "Correy"

print('Election Results')
print('----------------------')
print(f'Total Votes: {total_votes}\n')
print('----------------------')
 
#average = khan_votes + li_votes + OTooley + correy_votes / 2
average_khan = (khan_votes/total_votes) *100
print("Khan's % in votes:")
print(average_khan)
average_li = (li_votes/total_votes) *100
print("Li's % in votes:")
print(average_li)
average_otooley = (OTooley/total_votes) *100
print("O'Tooley's % in votes:")
print(average_otooley)
average_correy = (correy_votes/total_votes) *100
print("Li's % in votes:")
print("Correy's % in votes:")
print(average_correy)
print('----------------------')
print('winner: {Khan}')


#all of these below were commented out on purpose/ full of trials and errors to figure this thing out
#row[2] in candidate and row[2] not in "Candidate":
#else will create a new spot in the list for the candidate
#if 
#else:
#candidate.append(row[2])
#vote_count[row[2]] = 1

#for key, value in vote_count.items():
#percentage[key] = str(round((value/total_votes)*100,3)) + "% ("+str(value)+ ")"

#inner = max(vote_count.keys())
"""
#ouput our results as a textfile and make it organized
with open('output_election.txt','w',newline='') as textfile:
    print('Election Results')#, file = textfile)
    print('----------------------------------', file = textfile)


    print(f'Total Votes: {candidate[0]}\n')#, file = textfile)
   
    print(f'percentage: {percentage}', file = textfile)
    print('----------------------------------', file = textfile)


    print(f'Winner: {winner[0]}', file = textfile)
   
with open('output_election.txt',newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row)

"""




