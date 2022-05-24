from clase import viajero

class manejadorviajeros:
    __lista = []
    def __init__(self):
        self.__lista=[]
    def agregar(self,viajero):
        self.__lista.append(viajero)
    def buscar(self,n):
       for indice,viajero in enumerate(self.__lista):
           if viajero.getid() == n:
               return indice
