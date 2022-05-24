import csv
from manejador import manejadorviajeros
from clase import viajero


def menu():
    n=input('ingrese el numero de viajero a realizar acciones \n')
    indice= mv.buscar(n)
    if indice == None:
        print('no se encontró el viajero')
    else:
        print('....MENU....')
        m=int(input(' 1..Consultar millas \n 2..Acumular millas \n 3..Canjear millas \n 0.. para finalizar\n'))
        while m!=0:
            if m==1:
                print(mv.cantidadtotal(indice))
            elif m==2:
                n=int(input('ingrese las millas a acumular'))
                mv.acumularmillas(indice,n)
            elif m==3:
                x=int(input('ingrese las millas a canjear'))
                mv.canjearmillas(indice,x)
            m=input(' 1..Consultar millas \n 2..Acumular millas \n 3..Canjear millas \n 0.. para finalizar')

if __name__ == '__main__':
    mv=manejadorviajeros()
    archivo=open('viajeros.csv')
    reader=csv.reader(archivo)
    for row in reader:
        p=viajero(row[0],row[1],row[2],row[3],int(row[4]))
        mv.agregar(p)
    menu()
