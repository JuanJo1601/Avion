class Pasajero:
    '''----------------
    ATRIBUTOS
    ----------------'''

    '''----------------
    CONSTRUCTOR
    ----------------'''
    
    def __init__(self, pCedula, pNombre):
        self.__cedula = self.pCedula
        self.__nombre = self.pNombre

    '''----------------
    METODOS
    ----------------'''

    def darCedula(self):
        return self.__cedula
    
    def darNombre(self):
        return self.__nombre
