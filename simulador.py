from ciudadano import Ciudadano
from comunidad import Comunidad
from enfermedad import Enfermedad
import random
prob_inf = 15
prob_gravedad = 7
prob_mor = 23
con_fis = 5
poblacion = 1000
pasos = 50

class Simulador():
    def __init__(self):
        self._comunidad = None
        self._dias = 0

    @property
    def comunidad(self):
        return self._comunidad

    @comunidad.setter
    def comunidad(self, comunidad):
        if isinstance(comunidad, Comunidad):
            self._comunidad = comunidad
        else:
            print("El tipo de dato en comunidad no corresponde")

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self,dias):
        if isinstance(dias, int):
            self._dias = dias
        else:
            print('El tipo de dato en dias no corresponde ')

    def calculo_probabilidad_gravedad(self, enfermedad):
        
        if enfermedad == 'Asma':
            final = prob_gravedad * 5
            return final
        elif enfermedad == 'Enfermedad cerebrovascular':
            final = prob_gravedad * 3
            return final
        elif enfermedad == 'Fibrosis quistica':
            final = int(prob_gravedad * 6.5)
            return final
        elif enfermedad == 'Hipertension':
            final = prob_gravedad * 2       
            return final
        elif enfermedad == 'Presion arterial alta':
            final = int(prob_gravedad *  2.5)
            return final      
        elif enfermedad == 'Obesidad':
            final = int(prob_gravedad * 4.5)
            return final
        elif enfermedad == 'Desnutricion':
            final = int(prob_gravedad * 2.5)
            return final

    def comprobar_recuperacion_o_gravedad(self, i):
        dias_enfermo = i.aumento_dias_enfermo()
        if dias_enfermo > 7:
            i.enfermo = 1
            self.comunidad._recuperados += 1
            self.comunidad._infectados -= 1
            if i.grave == True:
                self.comunidad._graves -= 1
            return 0

        else:
            if i.grave == False:            
                if i.enfermobase_getter() == True:
                    prob_gravedad_real = self.calculo_probabilidad_gravedad(i.enfermedad_base)
                elif i.afectado_getter() == True:
                    prob_gravedad_real = self.calculo_probabilidad_gravedad(i.afeccion)
                
                else:
                    prob_gravedad_real = int(prob_gravedad * 0.60)
                
                if i.vacunado_getter() == True:
                    if i.vacuna == 1:
                        prob_gravedad_real = int(prob_gravedad_real * 0.25)
                    elif i.vacuna == 2:
                        prob_gravedad_real = -1
                    elif i.vacuna == 3:
                        i.enfermo = 1
                        self.comunidad._recuperados += 1
                        self.comunidad._infectados -= 1
                        return 0
                    else: 
                        pass

                prob_estar_grave = random.randint(0,100)
                if prob_estar_grave <= prob_gravedad_real:
                    i.grave = 1
                    self.comunidad._graves += 1
                    return 1
            
        if i.grave == True:
            probabilidad_de_morir = self.comunidad.enfermedad.probabilidad_de_morir
            probabilidad_muerte = random.randint(0,1000)
            if probabilidad_muerte <= probabilidad_de_morir:
                i.enfermo = 2
                self.comunidad._muertos += 1
                self.comunidad._recuperados += 1
                self.comunidad._infectados -= 1
                return 0
            else:
                return 1
                            
    def contagio(self, j, factor):
        probabilidad_de_infeccion = self.comunidad.enfermedad.probabilidad_de_infectarse * factor
        probabilidad_de_infectarse = random.randint(0,100)
        if probabilidad_de_infectarse <= probabilidad_de_infeccion:
            j.enfermo = 0
            self.comunidad._susceptibles -= 1
            self.comunidad._infectados += 1

    def realizar_contactos(self, i):
        contactos_fisicos = random.randint(1, self.comunidad.promedio_conexion_fisica)
        while contactos_fisicos > 0:
            contacto_aleatorio = random.randint(1,len(self._comunidad._ciudadanos))
            for j in self.comunidad._ciudadanos:    
                id_contacto_aleatorio = j.id
                if id_contacto_aleatorio == contacto_aleatorio:
                    if j.enfermo == False and j.id_familia == i.id_familia:
                        self.contagio(j, 2)                                       
                    elif j.enfermo == False and j.id_familia != i.id_familia:
                        self.contagio(j, 1)
            
            contactos_fisicos -= 1

    def pandemia(self):
        dias_de_simulacion = 0
        edades = 0
        enfermos_base_o_afectados = 0
        cantidad_vacunas = 0
        vacunas_maximas = int(self.comunidad.num_ciudadanos * 0.5)

        for i in self.comunidad._ciudadanos:
            edades += i.edad
            if i.enfermobase_getter() == True:
                enfermos_base_o_afectados += 1
            if i.afectado_getter() == True:
                enfermos_base_o_afectados += 1

        promedio_edades = int(edades/ self.comunidad.num_ciudadanos)

        print("TOTAL DE POBLACION =",self.comunidad.num_ciudadanos,
              "TOTAL DE POBLACION CON ENFERMEDAD BASE Y/O AFECCION", enfermos_base_o_afectados,
              "PROMEDIO DE EDAD DE LA COMUNIDAD", promedio_edades,
              "VACUNAS DISPONIBLES", cantidad_vacunas)

        while dias_de_simulacion < self.dias:
            if dias_de_simulacion % 7 == 0:
                if cantidad_vacunas < vacunas_maximas:
                    cantidad_vacunas_nuevas = int(vacunas_maximas * 0.1)
                    cantidad_vacunas_uno = int(cantidad_vacunas_nuevas * 0.5)
                    cantidad_vacunas_dos = int(cantidad_vacunas_nuevas * 0.32)
                    cantidad_vacunas_tres = int(cantidad_vacunas_nuevas * 0.16)
                    cantidad_vacunas += cantidad_vacunas_nuevas

            for i in self._comunidad._ciudadanos:
                vacunacion = random.randint(0,3)
                if vacunacion == 1 and cantidad_vacunas_uno != 0:
                    i.vacuna = 1
                    cantidad_vacunas_uno -= 1
                    self.comunidad._inoculados += 1

                elif vacunacion == 2 and cantidad_vacunas_dos != 0:
                    i.vacuna = 2
                    cantidad_vacunas_dos -= 1
                    self.comunidad._inoculados += 1
                elif vacunacion == 3 and cantidad_vacunas_tres != 0:
                    i.vacuna = 3
                    cantidad_vacunas_tres -= 1
                    self.comunidad._inoculados += 1
            
                if i.enfermo == True and i.recuperado_getter() == False:
                    estado = self.comprobar_recuperacion_o_gravedad(i)
                    if estado != 0:
                        if i.grave == False:
                            self.realizar_contactos(i)                                                                                                                                                               
            print("INFECTADOS = ", self.comunidad._infectados, 
                  "SANOS =", self.comunidad._susceptibles,
                  "GRAVES =", self.comunidad._graves, 
                  "RECUPERADOS =", self.comunidad._recuperados)                    
            dias_de_simulacion += 1

        edades = 0
        enfermos_base_o_afectados = 0
        for i in self.comunidad._ciudadanos:
            if i.muerto_getter() == False:
                edades += i.edad
                if i.enfermobase_getter() == True:
                    enfermos_base_o_afectados += 1
                if i.afectado_getter() == True:
                    enfermos_base_o_afectados += 1

        poblacion_viva = self.comunidad._susceptibles + self.comunidad._recuperados - self.comunidad._muertos
        promedio_edades = int(edades/ poblacion_viva)

        print("TOTAL DE POBLACION =",poblacion_viva,
              "TOTAL DE POBLACION CON ENFERMEDAD BASE Y/O AFECCION", enfermos_base_o_afectados,
              "INFECTADOS = ", self.comunidad._infectados,
              "INOCULADOS", self.comunidad._inoculados,
              "RECUPERADOS =", self.comunidad._recuperados,
              "FALLECIDOS =", self.comunidad._muertos,
              "PROMEDIO DE EDAD DE LA COMUNIDAD", promedio_edades)     

def main():
    covid = Enfermedad()
    covid.nombre = 'Covid-19'
    covid.probabilidad_de_infectarse = prob_inf
    covid.probabilidad_de_morir = prob_mor

    talca = Comunidad()
    talca.comunidad = 'Talca'
    talca.promedio_conexion_fisica = con_fis
    talca.num_ciudadanos = poblacion
    talca.enfermedad = covid
    talca.crear_ciudadanos()
    talca.inicio()

    simulacion = Simulador()
    simulacion.comunidad = talca
    simulacion.dias = pasos
    simulacion.pandemia()

if __name__ == "__main__":
    main()