class viajero:
    __numviajero= ''
    __dni= ''
    __nombre=''
    __apellido = ''
    __millasacum = 0
    def __init__(self,numviajero,dni,nombre,apellido,millas):
        self.__numviajero=numviajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasacum=int(millas)
    def getid(self):
        return(self.__numviajero)
    def cantidadtotal(self):
        return self.__millasacum
    def acumularmillas(self,n):
        self.__millasacum=slef.__millasacum+n
        return (self.__millasacum)
    def canjearmillas(self,m):
        if(m > self.__millasacum):
            return(print('La cantidad de millas a canjear no supera la cantidad de millas acumuladas'))
        else:
            self.__millasacum= self.__millasacum - m
            return(self.__millasacum)
    def __gt__(self, other):
        if self.__millasacum >= other.cantidadtotal:
            return self.__millasacum
        else:
            return  other.cantidadtotal
    def __radd__(self, n):
        return(viajero(self.__numviajero,self.__dni,self.__nombre,self.__nombre,self.__apellido,self.__millasacum+n))
    def __rsub__(self, n):
        return(viajero(self.__numviajero,self.__dni,self.__nombre,self.__nombre,self.__apellido,self.__millasacum-n))
    def __eq__(self, n):
        if(self.__millasacum == n):
            return True
        else:
            return False
    def __add__(self, n):
        k=self.__millasacum+n
        return k
    def __radd__(self, n):
        k=self.__millasacum+n
        return k
    def __sub__(self, n):
        k=self.__millasacum-n
        return k
    def __rsub__(self, n):
        k=self.__millasacum-n
        return k
