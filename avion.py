from silla import Silla

class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []

        self.definicionSillaEjecutivas()
        self.definicionSillaEconomicas()

    def definicionSillaEjecutivas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.ventana)
            else:
                self.sillasEjecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.pasillo)
 
    def definicionSillaEconomicas(self):
        for i in range(self.SILLAS_ECONOMICAS):
            
