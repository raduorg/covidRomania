import csv

# Open the CSV file
with open('data_complete.csv', 'r') as f:
  reader = csv.reader(f)
  
  # Read each row of the CSV file
  rows = []
  for row in reader:
    rows.append(row)
  
  # Iterate through each cell in the table
  for i, row in enumerate(rows):
    for j, cell in enumerate(row):
      # If the cell is blank and the cells above and below it are non-blank, delete the cell
      if cell == '' and rows[i-1][j] != '' and rows[i+1][j] != '':
        row[j] = None

# Open the CSV file for writing
with open('file.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  
  # Write each modified row to the CSV file
  for row in rows:
    writer.writerow(row)
