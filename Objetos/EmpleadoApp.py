from Empleado import *
empl1=Empleado ('pepe','contador',1160000)
print(type(empl1))
print(empl1.getNombre())
empl1.setNombre('Pepito')
print(empl1.getNombre())
print(empl1.getCargo())
empl1.setCargo('Administrador')
print(empl1.getCargo())
print(empl1.getSalario())
empl1.setSalario(122323)
print(empl1.getSalario())