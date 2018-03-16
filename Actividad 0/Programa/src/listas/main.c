// Libreria de input y output (para leer y escribir archivos o leer y escribir en consola)
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Importo los archivos .h de las listas
#include "arraylist/arraylist.h"
#include "linkedlist/linkedlist.h"

// Recibe como input los parametros del programa en un arreglo de strings y un numero que indica cuantos argumentos son
int main(int argc, char *argv[])
{
  LinkedList* list = linkedlist_init();
  ArrayList* list2 = arraylist_init();
  clock_t begin = clock();
  for (int i = 0; i < 100000; i++) {
    linkedlist_append(list, i);
  }
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent);

  clock_t begin2 = clock();
  for (int i = 0; i < 100000; i++) {
    arraylist_append(list2, i);
  }


  clock_t end2 = clock();
  double time_spent2 = (double)(end2 - begin2) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent2);





  clock_t begin3 = clock();
  for (int i = 0; i < 5000; i++){
    linkedlist_insert(list, 5, 0);
    linkedlist_insert(list, 4, list->count);
    linkedlist_insert(list, 3, list->count/2);
  }
  clock_t end3 = clock();
  double time_spent3 = (double)(end3 - begin3) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent3);

  clock_t begin4 = clock();
  for (int i = 0; i < 5000; i++){
    arraylist_insert(list2, 5, 0);
    arraylist_insert(list2, 4, list2->count);
    arraylist_insert(list2, 3, list2->count/2);
  }
  clock_t end4 = clock();
  double time_spent4 = (double)(end4 - begin4) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent4);

  clock_t begin5 = clock();
  for (int i = 0; i < 4000; i++){
    linkedlist_delete(list, 3);
  }
  clock_t end5 = clock();
  double time_spent5 = (double)(end5 - begin5) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent5);

  clock_t begin6 = clock();
  for (int i = 0; i < 4000; i++){
    arraylist_delete(list2, 3);
  }
  clock_t end6 = clock();
  double time_spent6 = (double)(end6 - begin6) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent6);

  LinkedList* list3 = linkedlist_init();
  ArrayList* list4 = arraylist_init();

  for (int i = 0; i < 100000; i++) {
    linkedlist_append(list3, i);
  }

  for (int i = 0; i < 100000; i++) {
    arraylist_append(list4, i);
  }

  clock_t begin7 = clock();
  linkedlist_concatenate(list, list3);
  clock_t end7 = clock();
  double time_spent7 = (double)(end7 - begin7) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent7);

  clock_t begin8 = clock();
  arraylist_concatenate(list2, list4);
  clock_t end8 = clock();
  double time_spent8 = (double)(end8 - begin8) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent8);

  clock_t begin9 = clock();
  for (int i = 0; i < 500000; i++) {
    linkedlist_get(list, 5);
  }
  clock_t end9 = clock();
  double time_spent9 = (double)(end9 - begin9) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent9);

  clock_t begin10 = clock();
  for (int i = 0; i < 500000; i++) {
    arraylist_get(list2, 5);
  }
  clock_t end10 = clock();
  double time_spent10 = (double)(end10 - begin10) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent10);

  clock_t begin11 = clock();
  linkedlist_destroy(list);
  clock_t end11 = clock();
  double time_spent11 = (double)(end11 - begin11) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent11);

  clock_t begin12 = clock();
  arraylist_destroy(list2);
  clock_t end12 = clock();
  double time_spent12 = (double)(end12 - begin12) / CLOCKS_PER_SEC;
  printf("Tiempo gastado: %f\n", time_spent12);





  /*int* valor = lista->array;
  for (int i = 0; i < lista->count; i++){
    printf("%d\n",valor[i]);
  }*/
  /*Node* valor = list->head;
  for (int i = 0; i < list->count; i++){
    printf("%d\n",valor->value);
    valor = valor->next;
  }*/
  return 0;
}
