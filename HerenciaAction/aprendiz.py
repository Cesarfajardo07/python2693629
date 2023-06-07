from persona import *
#Se importan las clases persona  y curso
from curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha): #Se crea el constructor de la clase aprendiz
        Persona.__init__(self,nombre,documento) #Se llama elconstructor de la clase persona
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[]
    
    def agregarCurso(self,curso): #Se crea un metodo para agregar cursos
        self.__cursos.append(curso)
    
    def componerCurso(self): #Secrea un metodo para que permita ingresa el curso que desea agregar
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)
    
    def verCursos(self): #Se crea en metodo que permit ver los nombres de los cursos agregados
        return self.__cursos