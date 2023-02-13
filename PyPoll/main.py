# Module 3 - PyPoll
# import os module to create file paths across operating systems
import os

# import module for reading csv files
import csv

# set path for file
election_data = os.path.join(os.getcwd(), 'PyPoll', 'Resources', 'election_data.csv')

# create empty lists and set variables
totalVotes = 0
candidateList = []
candidateVotes = []
candidatePercent = []
count = 0
winner = ""

# improved reading using csv module (open csv file)
with open(election_data) as csvfile:

    # store contents of csv file in variable csvreader
    data = csv.reader(csvfile, delimiter=',')

    # skip the header and then iterate (loop) through values
    header = next(data)

    # loop through data
    for row in data:
        
        # calculate the total number of votes cast
        totalVotes += 1
    
        # output a complete list of candidates who received votes
        candidate = row[2]

        if candidate not in candidateList:
            candidateList.append(candidate)
            candidateVotes.append(1)
            candidatePercent.append(0) 

        else: 
            candidateVotes[candidateList.index(candidate)] += 1

        # calculate the percentage of votes each candidate won
        votes = candidateVotes[candidateList.index(candidate)] 
        candidatePercent[candidateList.index(candidate)] = votes/totalVotes

        # identify winner 
        if votes > count:
          count = votes
          winner = candidate 

# output file
output_path = os.path.join(os.getcwd(), 'PyPoll','Resources', 'PyPollAnalysis.txt')

# write changes to csv using write command
with open(output_path, 'w') as file:

  # print statements
  print(f"Election Results")
  file.write(f"Election Results\n")
  print(f"----------------------")
  file.write(f"----------------------\n")
  print(f"Total Votes: {totalVotes}")
  file.write(f"Total Votes: {totalVotes}\n")
  print(f"----------------------")
  file.write(f"----------------------\n")

  # loop for candidate output
  i=0
  for candidate in candidateList:
    percent = candidatePercent[i] * 100
    votes = candidateVotes[i]
    print(f"{candidate}: {percent: .3f} % ({votes})")
    file.write(f"{candidate}: {percent: .3f} % ({votes})\n")
    i += 1
  print(f"----------------------")
  file.write(f"----------------------\n")
  print(f"Winner: {winner}")
  file.write(f"Winner: {winner}\n")
        
