class Curso: #Se crea la clase curso
    def __init__(self,nombre,tipo): #Se crea el constructor de la clase
        self.__nombre=nombre
        self.__tipo=tipo

    def getNombre(self): #Se crea el getter para ver el nombre del curso
        return self.__nombre