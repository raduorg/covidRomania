import csv
import numpy as np

# initialize empty lists to store data
rows = []
weekly_stringency = []
time = []

# open the CSV file and read in the rows
with open('WeeklyGovStringencyRomania.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    # only keep rows wherv e the first entry is 'Romania'
    if row[0] == "Romania": #and row[3]!='':
      rows.append(row)
  #print(rows)

##compute the weekly death totals
#for i in range(0, len(rows), 7):
  #for row in rows[i:i+7]:
    # if row[3] == '':
      # print('aici')
    # print(row[3])
#  weekly_deaths.append(np.sum([int(row[3]) for row in rows[i:i+7]]))

#compute the weekly stringency average
for i in range(0, len(rows), 7):
  #for row in rows[i:i+7]:
    # if row[3] == '':
      # print('aici')
    # print(row[3])
  weekly_stringency.append(np.average([float(row[3]) for row in rows[i:i+7]]))

# compute the time values
week_num = 9
year = 2020
for i in range(len(weekly_stringency)):
  time.append(f"W{week_num:02d}, {year}")
  week_num += 1
  if week_num > 52:
    week_num = 1
    year += 1

# add the weekly deaths and time columns to the rows
for i in range(len(weekly_stringency)):
  rows[i].append(weekly_stringency[i])
  rows[i].append(time[i])

#write the modified rows to a new CSV file
with open('WeeklyGovStringencyRo.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(rows)
# print('ceva')