'''
Visualizes the Mandlebrot set for static number of iterations
Matt Ambacher
July 12 2016
'''
import cmath
import matplotlib.pyplot as plt

def inMandel(c, max_iters):	
	z = 0
	for i in xrange(max_iters):
		z = z*z + c
		if abs(z) > 2:
			return  1.0 - 0.5*float(i)/max_iters
	return 0.5

def make_graph(xmin, xmax, ymin, ymax, xresolution, yresolution, max_iters):
	graph = [[1 for x in range(xresolution + 1)] for y in range(yresolution + 1)]
	for x in xrange(xresolution + 1):
		zreal = float(x)/xresolution * (xmax - xmin) + xmin
		for y in xrange(yresolution+ 1):
		#have to flip imag(z) because python increases downwards and complex plane increases			upwards
			zimag = float(y)/yresolution * (ymax - ymin) + ymin 
			c = zreal + 1j*zimag
			graph[y][x] = inMandel(c, max_iters)
	return graph

def show_graph(graph, xmin , xmax, ymin, ymax):
	
	plt.imshow(graph, extent=[xmin,xmax,ymin,ymax], cmap='hot')
	plt.colorbar()
	plt.show()
	return

if __name__ == '__main__':
	#set max/min of grid to 2 since any z such that |z| > 2 diverges	
	xmin = -0.388
	xmax = -0.375 
	ymin = 0.587
	ymax = 0.595
	xresolution = 1920-1
	yresolution = 1080-1
	max_iters = 1000
	graph = make_graph(xmin, xmax, ymin, ymax, xresolution, yresolution, max_iters)
	show_graph(graph, xmin, xmax, ymin, ymax)
