#define SIZE 10
#define TRUE 1
#define FALSE 0

void main(void) {

  static int lista[SIZE];
  int houveTroca, i, aux, j;

  // read
  for(j=0; j < SIZE; j++) {
    print_string("\n Introduza um numero: ");
    lista[j] = read_int();
  }

  // ordenacao
  do {

    houveTroca = FALSE;

      for(i=0; i < SIZE-1; i++) {
        if (lista[i] > lista[i+1]) {
          aux = lista[i];
          lista[i] = lista[i+1];
          lista[i+1] = aux;
          houveTroca = TRUE;
        }
      }
    } while(houveTroca == TRUE);

    // print
    for() {


    }

}
