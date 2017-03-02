import cmath
from math import log10
import numpy as np
import matplotlib.pyplot as plt

def julia(z, c, max_iters):
	count = 0
	eps = 1e-8
	while count < max_iters:
		z = z*z + c
		if abs(z) > 2:
			return log10( float(count)/max_iters + eps)
		count += 1
	return 0

def makeGraph(width, height, xmin, xmax, ymin, ymax, c, max_iters):
	graph = np.zeros( (height,width) )
	for row in xrange(width):
		for col in xrange(height):
			zreal = float(row)/width * (xmax - xmin) + xmin
			zimag = float(col)/height * (ymax - ymin) + ymin
			z = zreal + zimag*1j
			graph[col][row] = julia(z, c, max_iters)
	return graph

def showGraph(graph, xmin, xmax, ymin, ymax): 
	plt.imshow(graph, cmap='hot', extent=[xmin,xmax,ymin,ymax])
	plt.show()
if __name__ == '__main__':
	xmin = -2
	xmax = 2
	ymin = -2
	ymax = 2
	max_iters = 256
	c = 0
	
	width = 1920
	height =  1080

	graph = makeGraph(width, height, xmin, xmax, ymin, ymax, c, max_iters)
	showGraph(graph, xmin, xmax, ymin, ymax)
