
#include <stdlib.h>
#include <stdio.h>

int Count1=0;
int Count2=0;

int p(int num);
int din(int num);

int main(void){

	for(int i=0; i<=12; i++){
		int a1=p(i);
		int a2=din(i);
		fprintf(stdout, "Resultado recursivo = %d | Número de Operações = %3d\n", a1, Count1);
		fprintf(stdout, "Resultado dinâmico = %d | Número de Operações = %3d\n", a2, Count2);
		Count1=0;
		Count2=0;
	}


}

int p(int num){
	if(num<=1) return 0;

	Count1+=3;
	return num + p(num/3) + p((num+1)/3) + p((num+2)/3);
}

int din(int num){
	if(num<=1) return 0;

	int tmp=(num+2)/3;
	int array[tmp+1];

	array[0] = 0;
	array[1] = 0;

	for(int i=2; i<=tmp; i++){
		Count2+=3;
		array[i]= i + array[i/3] + array[(i+1)/3] + array[(i+2)/3];
	}

	Count2+=3;
	return num + array[num/3] + array[(num+1)/3] + array[tmp];
}
