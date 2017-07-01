def ord_seleccion(lista):                   #De menor a mayor
    n = len(lista) - 1

    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n -= 1

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#________________________________________________________________________________________________

def ord_insercion(lista):                   #De menor a mayor
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        
def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

#_______________________________________________________________________________________________

def ord_insercion2(lista):                  #De mayor a menor
    lista_nueva = lista[:]
    for i in range(len(lista_nueva) - 1):
        if lista[i + 1] > lista[i]:
            reubicar2(lista_nueva, i + 1)
    return lista_nueva
        
def reubicar2(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v > lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

#_______________________________________________________________________________________________
    
def merge_sort(lista):
    if len(lista) < 2:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado
#_______________________________________________________________________________________________
    
def merge_sort_3(lista):
    if len(lista) < 2:
        return lista
    sep1 = len(lista) // 3
    sep2 = (len(lista) // 3) * 2
    seccion1 = merge_sort(lista[:sep1])
    seccion2 = merge_sort(lista[sep1:sep2])
    seccion3 = merge_sort(lista[sep2:])
    return merge_3(seccion1, seccion2, seccion3)

def merge_3(lista1, lista2, lista3):
    aux = merge(lista1, lista2)
    resultado = merge(aux, lista3)
    return resultado

#_______________________________________________________________________________________________

def quick_sort(lista):
    if len(lista) < 2:
        return lista
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)

def _partition(lista):
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores

#_______________________________________________________________________________________________

def quick_sort_mejorado(lista): #Opera sobre la misma lista, no gasta tanta memoria
    _quick_sort(lista, 0, len(lista) - 1)

def _quick_sort(lista, inicio, fin):
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)

def _partition(lista, inicio, fin):
    pivote = lista[inicio]
    menores = inicio
    for i in range(inicio + 1, fin + 1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                _swap(lista, i, menores)
    if inicio != menores:
        _swap(lista, inicio, menores)
    return menores

def _swap(lista, i, j):
    lista[j], lista[i] = lista[i], lista[j]
#_______________________________________________________________________________________________


    
"""__________________________________________Selección en C________________________________________________

    
#include <stdio.h>
#define LEN 7
void imprimir_lista(int *lista, int len){
    int i;
    for(i=0 ; i<len ; i++)
     printf("%i,",lista[i]);
    
    printf("\n");
}  

int main() {
    int lista[] = {5,7,4,2,1,6,3};
    int aux,mayor;
    int i,j;
    
    imprimir_lista(lista, LEN);
    
    
   for(j = LEN-1; j>= 0; j--){
   mayor = j;
     for(i=j ; i >= 0 ;i--){
       if (lista[i] > lista[mayor])
         mayor=i;
     }
     
     aux= lista[j];
     lista[j] = lista[mayor];
     lista[mayor] = aux;
     
   }
     
     
     imprimir_lista(lista, LEN);
     printf("%i", mayor);
    
    getchar();
    return 0;
}
"""

l = [6, 7, -1, 0, 5, 2, 3, 8]
