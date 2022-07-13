# Proyecto-2-PrograAvan-2022
Este proyecto es la continuacion del proyecto contenido en este link
(https://github.com/Tryton22/Proyecto-1-U3).
Al igual que en la primera parte, el profesor a cargo (Fabio Durán) segurió algunas ideas que
nos ayudo para
desarrollar esta segunda parte.

# Autores
- Claudio La Rosa.
- Denise Valdés.
- Matías Fonseca.

# Ciudadano.py
Como cambios en esta clase se agregaron algunos atributos y métodos. Los atributos agregados
permiten saber
la edad del ciudadano (self._edad), que enfermedad base presenta (self._enfermedad_base),
que afeccion presenta (self._afeccion), si esta vacunado o no (self._vacuna) todos estos
atributos son inicializados
con un None, ya que mas adelante se les otorgara algun valor. Otros atributos agregados nos
ayuda a confirmar si efectivamente
el ciudadano se vacuno (self._vacunado), si tiene alguna afeccion (self._afectado), si tiene
alguna enfermedad base 
(self._enfermo_base), si el ciudadano se encuentra grave o no (self._grave) y si el ciudadano
esta muerto o no (self._muerto) 
todos estos son inicializados en None menos el self._muerto (por que el ciudadano estaria
muerto por default)
y se iran cambiando segun el codigo avance y se confirme lo que le pasa al ciudadano.

Como nuevos metodos, aparte de los @setter y los @property de los nuevos atributos, tenemos
unas funciones que nos retornan
y verifican la infomracion o getters de que si el ciudadano se vacuno (self vacunado_getter), 
si tiene una enfermedad base (self enfermobase_getter), si tiene una afeccion
(self afectado_getter) 
o si esta muerto (self muerto_getter) 

# Enfermedad.py
El único cambio que se le hizo a esta clase fue el cambio de nombre que sufrió tanto el
@property como el @setter
de un atributo, el cambio en cuestión fue que paso
del nombre def prob_morir a def probabilidad_de_morir.
A nivel de escritura son exactamente iguales, solo cambia el nombre.

# Comunidad.py
El primer cambio que se observa en esta clase es que al inicio del codigo, antes de la clase,
se agregaron 2 listas,
una lista con las enfermedades bases que pueden contraer los ciudadanos y otras con las
afecciones.
Luego, ya dentro de la clase, se agregaron unos atributos que nos indican la cantidad de
enfermos graves
(self._graves), la cantidad de inoculados (self._inoculados) y la cantidad de muertos
(self._muertos).

En los metodos, se agrega def edad, el cual tiene 2 if, el primero da lugar si
familia == 1 (la edad puede variar entre 20 y 80 años) y el segundo da lugar si 
familia >= 2 (la edad puede variar entre 1 y 80 años).
Y tambien a def crear_ciudadanos se le agrego una probabilidad que hace que los
ciudadanos tengan una enfermedad base (0.25) o que tengan una afeccion (0.65).
Tambien se le agrego una variable (enfermedad_o_afeccion) que toma aleatoriamente un valor 
entre el 0 y el 2, luego de esta variable aparecen varios if que relacionan la poblacion 
con enfermedad base o afeccion con el valor que toma la variable explicada anteriormente y
se le define la edad a nuestro ciudadano.

# Simulador.py
Tal como en Comunidad(), en esta clase los primeros cambios se notan antes, se importa
la clase Ciudadano() y se agrega otra variable (prob_gravedad).
Los cambios de la clase se producen en los metodos, ya que no se agrega ningun atributo 
nuevo, se agrega la funcion (def calculo_probabilidad_gravedad) la cual ve si el ciudadano
tiene alguna enfermedad y le multiplica un valor a prob_gravedad para sacar la probabilidad
real de que paciente este grave. Se le cambia el nombre a la funcion
(def comprobar_recuperacion_o_muerte) a (def comprobrar_recuperacion_o_gravedad), tambien 
se le hacen algunos cambios internos, una condicion extra al (if dias_enfermo > 7) lo que hace
esta condicion es ver si el ciudadano esta grave, si el ciudadano esta grave despues de 7 días
sale de la lista de graves automaticamente. En esta misma funcion se crean 2 else, uno
comprueba que el ciudadano no este grave y le calcula una probablidad real de gravedad
la cual es -1 si el ciudadano se encuentra vacunado, esta probabilidad la compara con un
numero aleatorio de 0 a 100, si la probabilidad es mayor o igual al numero el ciudadano
pasa a estar grave automaticamente, el otro comprueba que el ciudadano esta grave de verdad
y le calcula sus proabilidades de morir de una manera similar a las probabilidades de estar
grave, solo que el numero aleatorio va de 0 a 1000. 
Y lo ultimo que sufre cambios es la
funcion (def pandemia), ya que todo lo otro se mantiene igual que en la parte anterior, 
empezando con que se agregan variables (edades = 0, enfermos_base_o afectados = 0, 
cantidad_vacunas = 0 y vacunas_maximas = int(self._comunidad.num_ciudadanos * 0.5) y
la variable (dias_de_simulacion) pasa de (= self._dias) a (= 0), se crear un for en el que 
se agrega la edad a todos los ciudadanos y se confirma si poseen enfermedad base o afeccion,
se crea una variable de promedio de edades, la cual se muestra en pantalla, se hace un print
con el total de poblacion, el total con enfermedad base o afeccion, el promedio de edad y 
las vacunas disponibles. Se crea un while (dias_de_simulacion < self.dias) en el cual tenemos
un if doble que calcula la proporcion de vacunas que existen tomando como condiciones que las
vacunas_maximas no pueden ser menores que la cantidad_vacunas y que los dias_de_simulacion
tiene que ser un multiplo de 7 por que esos son los dias en los que el ciudadano puede 
recuperarse o morir, luego de este if doble viene un for que inocula a los ciudadanos que
no estan enfermos y a los ciudadanos que estan enfermos los pone a realizar contactos con 
ciudadanos sanos, luego se muestra en pantalla la cantidad de infectados, sanos, graves y 
recuperados y termina agregando un dia mas a la simulacion. Agregando las cosas finales 
tenemos que la variable edad y la variable enfermos_base_o_afectados es igual a 0, se agrega
otro for que confirma que el ciudadano no este muerto y le agregra una edad, tambien confirma 
si tiene alguna enfermedad base o afeccion y los suma a los enfermos_base_o_afectados. Llegando 
al final se agregan 2 variables, la primera poblacion_viva que suma los ciudadanos 
recuperados y susceptibles a la enfermedad y resta los ciudadanos muertos, la segunda
promedio_edades nos saca el promedio de edades que tiene la poblacion que queda viva.
Luego de todos estos cambios se vera en pantalla el numero total de poblacion, el total de 
poblacion con enfermedad base y/o afeccion, la cantidad de infectados, los recuperados, los 
fallecidos y el promedio de edad de la poblacion.

Los cambios relatados anteriormente son todo lo nuevo que se hizo en este proyecto, lo que no 
aparece aca se mantuvo igual en ambos codigos.







