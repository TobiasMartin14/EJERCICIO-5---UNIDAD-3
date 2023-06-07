import unittest

from menu import Menu
from manejadorEmpleados import ManejadorEmpleados

def test():
    ME = ManejadorEmpleados()
    ME.cargarEmpleados()
    print("\nLa lista fue cargada con éxito. \n")
    ME.mostrarLista()
    menu = Menu()
    menu.opciones(ME)


if __name__ == "__main__":
    test()