import glob
import csv
import re

########### MAIN ###########

for filename in glob.glob("./*.csv"):

	output_filename = './' + filename.split('/')[-1].split('.')[0] + '-clean.csv'
	output_file = open(output_filename, 'a')
	output_writer = csv.writer(output_file)

	with open(filename, 'rU') as infile:
		for input_row in csv.reader(infile):
			all_blank = True
			# clean the individual cells
			for input_pos in range(len(input_row)):
				if input_row[input_pos].strip() != '':
					all_blank = False
				# replace quoted newlines with spaces
				input_row[input_pos] = re.sub(r'\n', ' ', input_row[input_pos].strip())
				# strip and get rid of multiple spaces
				input_row[input_pos] = re.sub(' +', ' ', input_row[input_pos].strip())
				# remove spaces before commas
				input_row[input_pos] = re.sub(' ,', ',', input_row[input_pos])
				# remove spaces before semicolons
				input_row[input_pos] = re.sub(' ;', ';', input_row[input_pos])

			if not all_blank:
				output_writer.writerow(input_row)

	# done writing, close the file
	output_file.close()
