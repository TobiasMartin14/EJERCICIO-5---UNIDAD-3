from claseEmpleado import Empleado

class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, ME):
        indice = True
        while indice:
            print("\n") 
            print ("Opcion 1: Insertar un empleado.")
            print ("Opcion 2: Mostrar un empleado. ")
            print ("Opcion 3: Mostrar todos los empleados.")
            print ("Opcion 4: Salir.")
            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                pos = int(input("Ingrese una posicion para insertar un empleado: "))
                dni = str(input("Ingrese el dni del empleado: "))
                nombre = str(input("Ingrese el nombre del empleado: "))
                direccion = str(input("Ingrese la direccion del empleado: "))
                telefono = str(input("Ingrese el telefono del empleado: "))
                empleado = Empleado(dni, nombre, direccion, telefono)
                ME.insertarElemento(empleado, pos)
            elif (self.__opcion == 2):
                pos = int(input("Ingrese una posicion para mostrar un empleado: "))
                print(ME.mostrarElemento(pos))
            elif (self.__opcion == 3):
                ME.mostrarLista()
            elif (self.__opcion == 4):
                indice = False
            else:
                print("La opcion ingresada no es valida.")