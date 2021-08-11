#!/usr/bin/env python3
import cv2
import os
import sys
import numpy as np
import csv

from numbers_to_image import number_to_color, int_rgb_color, make_image

DIR = "images"

os.makedirs(DIR, exist_ok = True)

file = sys.argv[1]
column_start = int(sys.argv[2])
column_end = int(sys.argv[3])
number_max = int(sys.argv[4])

# Load data
def data_load(file):
	results = []
	# Read CSV file into array
	with open (file, newline = "") as csvfile:
		reader = csv.reader(csvfile, delimiter = ';')
		for row in reader:
			results.append(row)
	print(len(results))

	# Remove first n'line with array
	del results[0:1]
	data = []
	for row in results:
		numbers = row[column_start : column_end]
		line_data = []
		for num in numbers:
			line_data.append(int(num))
		data.append(line_data)
		print(line_data)
		for idx, x in enumerate(line_data):
			number_color = number_to_color(x, number_max)
			print(idx, number_color)
			number_rgb_color = int_rgb_color(number_color)
			image = make_image(number_rgb_color[2], 0, number_rgb_color[1], 0, number_rgb_color[0], 0, 8)
			if idx > 0:
				image_prev = np.concatenate((image_prev, image), axis=1)
			else:
				image_prev = image

		image_name = '_'.join(str(x) for x in line_data) + ".png"
		print(">>>", os.path.join(DIR, image_name))
		cv2.imwrite(os.path.join(DIR, image_name), image_prev)

data_load(file)
