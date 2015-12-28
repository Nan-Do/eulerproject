#include <stdio.h>
#include <math.h>

double gen_next(double n){
	double a;
	a = n - floor(n);
	return 1 / a;
}



int main(){
	int i;
	double r = pow(23, 0.5);
	for (i=0; i<100; i++){
		printf("%f\n", floor(r));
		r = gen_next(r);
	}
}
