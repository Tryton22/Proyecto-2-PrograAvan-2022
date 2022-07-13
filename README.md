# Proyecto-2-PrograAvan-2022
Este proyecto es la continuacion del proyecto contenido en este link (https://github.com/Tryton22/Proyecto-1-U3).
Al igual que en la primera parte, el profesor a cargo (Fabio Durán) segurió algunas ideas que nos ayudo para
desarrollar esta segunda parte.

# Autores
- Claudio La Rosa.
- Denise Valdés.
- Matías Fonseca.

# Ciudadano.py
Como cambios en esta clase se agregaron algunos atributos y métodos. Los atributos agregados permiten saber
la edad del ciudadano (self._edad), que enfermedad base presenta (self._enfermedad_base),
que afeccion presenta (self._afeccion), si esta vacunado o no (self._vacuna) todos estos atributos son inicializados
con un None, ya que mas adelante se les otorgara algun valor. Otros atributos agregados nos ayuda a confirmar si efectivamente
el ciudadano se vacuno (self._vacunado), si tiene alguna afeccion (self._afectado), si tiene alguna enfermedad base 
(self._enfermo_base), si el ciudadano se encuentra grave o no (self._grave) y si el ciudadano esta muerto o no (self._muerto) 
todos estos son inicializados en None menos el self._muerto (por que el ciudadano estaria muerto por default)
y se iran cambiando segun el codigo avance y se confirme lo que le pasa al ciudadano.

Como nuevos metodos, aparte de los @setter y los @property de los nuevos atributos, tenemos unas funciones que nos retornan
y verifican la infomracion o getters de que si el ciudadano se vacuno (self.vacunado_getter), 
si tiene una enfermedad base (self.enfermobase_getter), si tiene una afeccion (self.afectado_getter) 
o si esta muerto (self.muerto_getter) 

# Enfermedad.py
El único cambio que se le hizo a esta clase fue el cambio de nombre que sufrió tanto el @property como el @setter
de un atributo, el cambio en cuestión fue que paso
del nombre def.prob_morir a def.probabilidad_de_morir.
A nivel de escritura son exactamente iguales, solo cambia el nombre.

# Comunidad.py
El primer cambio que se observa en esta clase es que al inicio del codigo, antes de la clase, se agregaron 2 listas,
una lista con las enfermedades bases que pueden contraer los ciudadanos y otras con las afecciones.
Luego, ya dentro de la clase, se agregaron unos atributos que nos indican la cantidad de enfermos graves
(self._graves), la cantidad de inoculados (self._inoculados) y la cantidad de muertos (self._muertos).

En los metodos, se agrega def.edad, el cual tiene 2 if, el primero da lugar si
familia == 1 (la edad puede variar entre 20 y 80 años) y el segundo da lugar si 
familia >= 2 (la edad puede variar entre 1 y 80 años).
Y tambien a def.crear_ciudadanos se le agrego una probabilidad que hace que los
ciudadanos tengan una enfermedad base (0.25) o que tengan una afeccion (0.65).
Tambien se le agrego una variable (enfermedad_o_afeccion) que toma aleatoriamente un valor 
entre el 0 y el 2, luego de esta variable aparecen varios if que relacionan la poblacion 
con enfermedad base o afeccion con el valor que toma la variable explicada anteriormente y
se le define la edad a nuestro ciudadano.

# Simulador.py


