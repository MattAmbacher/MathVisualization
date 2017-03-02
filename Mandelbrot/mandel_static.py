'''
Visualizes the Mandlebrot set for static number of iterations
Matt Ambacher
July 12 2016
'''
import cmath
import matplotlib.pyplot as plt

def inMandel(c, num_iters):	
	z = 0
	for i in xrange(num_iters):
		z = z*z + c
		if abs(z) > 2:
			return 0
	return 1

def make_graph(xmin, xmax, ymin, ymax, xresolution, yresolution, num_iters):
	graph = [[1 for x in range(xresolution + 1)] for y in range(yresolution + 1)]
	for x in xrange(xresolution + 1):
		zreal = xmin + 2*xmax*(float(x)/xresolution)
		for y in xrange(yresolution+ 1):
		#have to flip imag(z) because python increases downwards and complex plane increases			upwards
			zimag = ymax + 2*ymin*(float(y)/yresolution)
			c = zreal + 1j*zimag
			graph[y][x] = inMandel(c, num_iters)
	return graph

def show_graph(graph):
	plt.imshow(graph, cmap='hot')
	plt.show()
	return
if __name__ == '__main__':
	#set max/min of grid to 2 since any z such that |z| > 2 diverges	
	xmin = -4.0
	xmax = 4.0
	ymin = -3.0
	ymax = 3.0
	xresolution = 1920-1
	yresolution = 1080-1
	num_iters = 8
	graph = make_graph(xmin, xmax, ymin, ymax, xresolution, yresolution, num_iters)
	show_graph(graph)
