class alumno:
    #Cuando creas un alumno de proc
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad
a1 = alumno("Maria, 20")
a2 = alumno("Juan, 21")
a3 = alumno("Ana, 19")

edad_mayor = 0
edad_menor = 99
if a1.getedad() > edad_mayor:
    edad_mayor = a1.getedad()
    alumno_mayor = a2.getedad()
if a2.getedad() > edad_mayor:
    edad_mayor = a2.getedad()
    alumno_mayor = a2.getedad()
if a3.getedad() > edad_mayor:
    edad_mayor = a3.getedad()
    alumno_mayor = a3.getedad()

print (f'El alumno mayor es {alumno_mayor} y tiene {edad_mayor} años de edad")
       
alumnos = {a1, a2, a3}:

for alum in alumnos:
     if alum.getedad() < edad_menor:
        edad_menor = alum.getEdad()
        alumno_menor = alum.getNombre()
     nombres += alum.getNombre() +""
     suma +=alum.get 
