#read in data set computed in C
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
xres = 1920
yres = 1080
img = np.zeros( (yres,xres)) 
rowcount = 0
with open('julia.txt', 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		colcount = 0
		for col in row[:-1]:
			img[rowcount][colcount] = float(col)
			colcount += 1
		rowcount += 1
plt.imsave( 'julia-hot.png', img, cmap='hot')
plt.imsave( 'julia-ncar.png', img, cmap='gist_ncar')
plt.imsave( 'julia-jet.png', img, cmap='jet')
plt.imsave( 'julia-summer.png', img, cmap='summer')
