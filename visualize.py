#read in mandel data computed in C
import csv
import matplotlib.pyplot as plt
import numpy as np

xres = 1920
yres = 1080
img = np.zeros( (yres,xres)) 
rowcount = 0
with open('mandelbrot.txt', 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		colcount = 0
		for col in row[:-1]:
			img[rowcount][colcount] = float(col)
			colcount += 1
		rowcount += 1

plt.imsave( 'mandel-hot.png', img, cmap='hot')
plt.imsave( 'mandel-ncar.png', img, cmap='gist_ncar')
plt.imsave( 'mandel-brbg.png', img, cmap='BrBG')
plt.imsave( 'mandel-jet.png', img, cmap='jet')
plt.imsave( 'mandel-prism.png', img, cmap='prism')
