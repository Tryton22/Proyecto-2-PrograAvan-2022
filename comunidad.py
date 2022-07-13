from enfermedad import Enfermedad
from ciudadano import Ciudadano
import random
Enfermedades_Base = ['Asma', 'Enfermedad cerebrovascular', 'Fibrosis quistica', 'Hipertension', 'Presion arterial alta']
Afecciones = ['Obesidad', 'Desnutricion']

class Comunidad():
    def __init__(self):
        self._comunidad = None
        self._promedio_conexion_fisica = None
        self._num_ciudadanos = None
        self._enfermedad = None

        self._susceptibles = 0
        self._infectados = 0
        self._graves = 0
        self._recuperados = 0
        self._inoculados = 0
        self._muertos = 0
        self._ciudadanos = []
        
    
    
    @property
    def comunidad(self):
        return self._comunidad

    @comunidad.setter
    def comunidad(self, comunidad):
        if isinstance(comunidad, str):
            self._comunidad = comunidad
        else:
            print("El tipo de dato en comunidad no corresponde")

    @property
    def promedio_conexion_fisica(self):
        return self._conexion_fisica

    @promedio_conexion_fisica.setter
    def promedio_conexion_fisica(self, conexion):
        if isinstance(conexion, int):
            self._conexion_fisica = conexion
        else:
            print("El tipo de dato en conexion fisica no corresponde")


    @property
    def num_ciudadanos(self):
        return self._num_ciudadanos

    @num_ciudadanos.setter
    def num_ciudadanos(self, num_ciudadanos):
        if isinstance(num_ciudadanos, int):
            self._num_ciudadanos = num_ciudadanos
        else:
            print("El tipo de dato en num_ciudadanos no corresponde")

    @property
    def enfermedad(self):
        return self._enfermedad
               
    @enfermedad.setter
    def enfermedad(self, enfermedad):
        if isinstance(enfermedad, Enfermedad):
            self._enfermedad = enfermedad
        else:
            print("El tipo de dato en enfermedad no corresponde")

    def crear_edad(self, familia):
        if familia == 1:
            edad = random.randint(20,80)
            return edad
        elif familia >= 2:
            edad = random.randint(1,80)
            return edad

    def crear_ciudadanos(self):
        id = 1
        id_familia = 1
        familia = 1
        cantidad_ciudadanos = self.num_ciudadanos
        poblacion_con_enfermedad_base = int(cantidad_ciudadanos * 0.25)
        poblacion_con_afeccion = int(cantidad_ciudadanos * 0.65)
        
        while cantidad_ciudadanos > 0:
        
            #Se identifica si el ciudadano tendra familia o no
            posibilidad_familia = random.randint(0,100)

            if posibilidad_familia == 0 or posibilidad_familia == 10:
                familia = 1
            elif posibilidad_familia >= 20 and posibilidad_familia <= 50:
                familia = 2
            elif posibilidad_familia >= 60 and posibilidad_familia <= 80:
                familia = 3
            elif posibilidad_familia == 90 or posibilidad_familia == 100:
                familia = 4
            
            while familia > 0:
                ciudadano = Ciudadano()
                ciudadano.id = id
                ciudadano.id_familia = id_familia
                ciudadano.comunidad = self.comunidad

                enfermedad_o_afeccion = random.randint(0,2)
                if poblacion_con_enfermedad_base == 0:
                    enfermedad_o_afeccion = random.randint(1,2)
                if poblacion_con_afeccion == 0:
                    enfermedad_o_afeccion = random.choice(0,2)
            

                if poblacion_con_enfermedad_base != 0 and enfermedad_o_afeccion == 0:
                    enfermedad_base = Enfermedades_Base[random.randint(0,4)]
                    ciudadano.enfermedad_base = enfermedad_base

                    poblacion_con_enfermedad_base -= 1

                elif poblacion_con_afeccion != 0 and enfermedad_o_afeccion == 1:
                    afeccion = Afecciones[random.randint(0,1)]
                    ciudadano.afeccion = afeccion

                    poblacion_con_afeccion -= 1 

                edad = self.crear_edad(familia)
                ciudadano.edad = edad

                self._ciudadanos.append(ciudadano)
                
                familia -= -1
                cantidad_ciudadanos = cantidad_ciudadanos - 1
                id = id + 1
                self._susceptibles += 1

                if cantidad_ciudadanos == 0:
                    familia = 0
            id_familia = id_familia + 1
                
    def inicio(self):
    
        paciente_cero = random.randint(1,len(self._ciudadanos))

        for i in self._ciudadanos:

            id_paciente_cero = i.id
            
            if id_paciente_cero == paciente_cero:
                self._susceptibles -= 1
                self._infectados += 1
                i.enfermo = 0               
                







