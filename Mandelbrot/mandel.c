#include <stdlib.h>
#include <math.h>
#include <png.h>
#include <stdio.h>
#include <complex.h>


double mandel(double complex c, int max_iterations);
double** makeGraph(double xmin, double xmax, double ymin, double ymax, int xres, int yres, int max_iterations);
void writeGraph(char* fname, double **graph, int width, int height);

int main() {
	
	double xmin = -0.3875;
	double xmax = -0.386;
	double ymin = 0.5937;
	double ymax = 0.595;
	int xres = 1920;
	int yres = 1080;
	int max_iterations = 10000;
	double **graph = makeGraph(xmin, xmax, ymin, ymax,  xres,  yres,  max_iterations);
	writeGraph("mandelbrot.txt", graph, xres, yres);
	free(graph);
	return 0;
}

double mandel(double complex c, int max_iterations) {
	double i = 0;
	double eps = 0.0000001;
	double complex z = c;
	while (i < max_iterations) {
		z = z*z + c;
		if (creal(z)*creal(z) + cimag(z)*cimag(z) > 4)
			return  log10(i/max_iterations + eps);
		i++;
	}
	return 0;
}

double** makeGraph(double xmin, double xmax, double ymin, double ymax, int xres, int yres, int max_iterations) {
	double** graph = malloc(yres * sizeof (double*));
	for (size_t size = 0; size < yres; size++)
		graph[size] = malloc(xres * sizeof(double));
	double val = 0;
	double complex c = 0;
        #pragma omp parallel
	{
	#pragma omp for collapse(2)
	for (int x = 0; x < xres; x++) {
		for (int y = 0; y < yres; y++) {
			double zreal = ((float)x)/xres * (xmax - xmin) + xmin;
			double zimag = ((float)y)/yres * (ymax - ymin) + ymin;
			c = zreal + I*zimag;
			graph[y][x] = mandel(c, max_iterations);
		}
	}	
	}
	return graph;
}

void writeGraph(char* fname, double** graph, int width, int height) {
	FILE* fp;
	fp = fopen(fname, "w");

	for (int y=0; y < height; ++y) {
		for (int x = 0; x < width; ++x)
			fprintf(fp, "%f\t", graph[y][x]);
		fprintf(fp, "\n");
	}
	fclose(fp);
}
