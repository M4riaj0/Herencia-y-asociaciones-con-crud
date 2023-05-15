import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import cliente

class CRUDClientes:
    def __init__(self):
        self.clientes = []

    def crear_cliente(self, nombre, cedula):
        nuevo_cliente = cliente.Cliente(nombre, cedula)
        self.clientes.append(nuevo_cliente)
        print("\tEl cliente se ha creado exitosamente")
        return nuevo_cliente
    
    def agregar_factura(self, cliente, factura):
        cliente.facturas.append(factura)
        print("\tFactura agregada exitosamente")

    def obtener_facturas_cliente(self, cliente):
        return cliente.facturas

    def consultar_cliente(self, cedula):
        for c in self.clientes:
            if c.cedulaCliente == cedula:
                print("\n\tCliente: ")
                print("\n\tCédula: ", cedula)
                print("\tNombre: ", c.nombreCliente)
                return c
        return None

    def modificar_cliente(self, cedula, nuevo_nombre):
        if self.clientes != []:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    c.nombreCliente = nuevo_nombre
                    print("\n\tCliente actualizado exitosamente")
                    return 
        return 1

    def eliminar_cliente(self, cedula):
        if self.clientes != []:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    self.clientes.remove(c)
                    print("\n\tCliente eliminado exitosamente")
                    return
        return 1
