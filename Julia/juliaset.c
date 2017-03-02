#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

double julia(complex double z, complex double c, int max_iters);
double** makeGraph(int width, int height, double xmin, double xmax, double ymin, double ymax, complex double c, int max_iters);
void writeGraph(char* fname, double** graph, int width, int height);
complex double juliaFunc(complex double z);

int main() {
	int width = 1920;
	int height = 1080;
	double xmin = -1.5;
	double xmax = 1.5;
	double ymin = -1;
	double ymax = 1.0;
	complex double c = -0.621 + 0.128*I;
	int max_iters = 1000;
	double	**graph = makeGraph(width, height, xmin, xmax, ymin, ymax, c, max_iters);
	writeGraph("julia.txt", graph, width, height);
	free(graph);
	return 0;
}

complex double juliaFunc(complex double z) {
	return cexp(z*z*z);
}

double julia(complex double z, complex double c, int max_iters) {
	double i = 0;
	double eps = 0.00000001;
	complex double z0 = z;
	while (i < max_iters) {
		z = juliaFunc(z) + c;
		if ( creal(z)*creal(z) + cimag(z)*cimag(z) > 100000)
			return  log10(i/max_iters + eps);
		i++;	
	}
	return 0; 
}

double** makeGraph(int width, int height, double xmin, double xmax, double ymin, double ymax, complex double c, int max_iters) {
	double** graph = malloc(height*sizeof(double*));
	for (size_t y = 0; y < height; ++y) 
		graph[y] =  malloc( width*sizeof(double));
	double juliaVal;
	double zreal, zimag;
	complex double z;
	for (int y = 0; y < height; ++y) {
		for (int x = 0; x < width; ++x) {
			zreal = ((float)x)/width * (xmax - xmin) + xmin;
			zimag = ((float)y)/height * (ymax - ymin) + ymin;
			z = zreal + I*zimag;
			graph[y][x] = julia(z,c,max_iters);
		}
	}
	return graph;
}

void writeGraph(char* fname, double** graph, int width, int height) {
	FILE* fp;
	fp = fopen(fname, "w");

	for (int y = 0; y < height; ++y) {
		for (int x = 0; x < width; ++x)
			fprintf(fp, "%f\t", graph[y][x]);
		fprintf(fp, "\n");
	}
	fclose(fp);
}
