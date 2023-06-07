class persona:
    def __init__ (self,nombre,documento,):
        #print ('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        self.__cursos=['Ingles']

    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setDocumento(self, documento):
        self.__documento=documento

    def cursos(self):
        self.__cursos=input(f'agrega un curso {self.__cursos.append}')
        return self.__cursos
    
    def getDocumento(self):
        return self.__documento
    
    def setCursos(self,cursos):
        self.__cursos=cursos

    def getCursos(self):
        return self.__cursos