import re

# Set Directory
DIR = '/Users/rmadhok/Documents/MOOC/Coursera/Using Python to Access Web Data/data/'
FILE = 'regex_sum_213640.txt'

# Open File
file = open(DIR + FILE)

# Create empty array
list = list()

# Loop through file and append numbers to num
for line in file:
	line = line.rstrip()
	list = list+re.findall('[0-9]+', line)
	
# Set Total
total = 0

for i in list:
	total+=int(i)

print 'The sum of the numbers in the file is ' + str(total)


