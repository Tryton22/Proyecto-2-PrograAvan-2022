
class Ciudadano():
    def __init__(self):
        self._comunidad = None
        self._id = None
        self._edad = None
        self._id_familia = None
        self._enfermedad_base = None
        self._afeccion = None
        self._vacuna = None

        self._vacunado = False
        self._afectado = False
        self._enfermo_base = False
        self._enfermo = False
        self._grave = False
        self._recuperado = True
        self._muerto = False
        self._dias_enfermo = 0

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
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            print("El tipo de dato en id no corresponde")
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int):
            self._edad = edad
        else:
            print("El tipo de dato en edad no corresponde")

    @property
    def id_familia(self):
        return self._id_familia
    @id_familia.setter
    def id_familia(self, id_familia):
        if isinstance(id_familia, int):
            self._id_familia = id_familia
        else:
            print("El tipo de dato en id_familia no corresponde")

    @property
    def enfermo(self):
        return self._enfermo

    @enfermo.setter
    def enfermo(self, enfermo):
        if isinstance(enfermo, int):
            if enfermo == 0:
                #print('El ciudadano', self.id, 'se contagio')
                self._enfermo = True
                self._recuperado = False
            if enfermo == 1:
                #print('El ciudadano', self.id, 'se recupero')
                self._recuperado = True
            if enfermo == 2:
                self._recuperado = True
                self._muerto = True
        else:
            print("El tipo de dato en enfermo no corresponde")

    @property
    def grave(self):
        return self._grave

    @grave.setter
    def grave(self, grave):
        if isinstance (grave, int):
            if grave == 0:
                self._grave = False
            if grave == 1:
                self._grave = True
        else:
            print('El tipo de dato en grave no corresponde')
            
    @property
    def enfermedad_base(self):
        return self._enfermedad_base
    
    @enfermedad_base.setter
    def enfermedad_base(self, enfermedad_base):
        if isinstance(enfermedad_base, str):
            self._enfermedad_base = enfermedad_base
            self._enfermo_base = True
        else:
            print('El tipo de dato en enfermedad base no corresponde')

    @property
    def afeccion(self):
        return self._afeccion

    @afeccion.setter
    def afeccion(self, afeccion):
        if isinstance(afeccion, str):
            self._afeccion = afeccion
            self._afectado = True
        else:
            print('El tipo de dato en afeccion no corresponde')

    @property
    def vacuna(self):
        return self._vacuna
    
    @vacuna.setter
    def vacuna(self, vacuna):
        if isinstance(vacuna, int):
            self._vacuna = vacuna
            self._vacunado = True
        else:
            print('El tipo de dato en vacuna no corresponde')

    def vacunado_getter(self):
        return self._vacunado

    def enfermobase_getter(self):
        return self._enfermo_base

    def afectado_getter(self):
        return self._afectado

    def muerto_getter(self):
        return self._muerto

    def recuperado_getter(self):
        return self._recuperado

    def aumento_dias_enfermo(self):
        self._dias_enfermo += 1
        return self._dias_enfermo



        

    