from modulos.productos_control import ProductosControl
from modulos.control_plagas import ControlPlagas
from modulos.fertilizantes import Fertilizantes
from modulos.antibioticos import Antibioticos
from modulos.facturas import Facturas


class CRUDFacturas:

    def crear_factura(self, fecha_factura):
        nueva_factura = Facturas(fecha_factura)
        print("\tFactura creada exitosamente")
        return nueva_factura

    def agregar_control_plagas(self, factura, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia):
        control_plagas = ControlPlagas(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia)
        factura.ProductosControl.append(control_plagas)
        print("\tControl de plagas agregado a la factura\n")
        return factura

    def agregar_fertilizante(self, factura, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, fechaUltimaAplicacion):
        fertilizante = Fertilizantes(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, fechaUltimaAplicacion)
        factura.ProductosControl.append(fertilizante)
        print("\tFertilizante agregado a la factura\n")
        return factura

    def agregar_antibiotico(self, factura, nombreProducto, dosisKg, tipoAnimal, precio):
        antibiotico = Antibioticos(nombreProducto, dosisKg, tipoAnimal, precio)
        factura.pcantibioticos = antibiotico
        print("\tAntibiotico agregado a la factura\n")
        return factura

    def leer_facturas(self , facturas):
        count = 1
        for factura in facturas:
            print(f"\n\t -----------factura: {count} ---------------\n")
            print(f"\tFecha de factura: {factura.fechaFactura}\n")
            print("\tProductos de control:\n")
            for producto in factura.ProductosControl:
                print(f"\tNombre:  {producto.nombreProducto} - ${producto.valorProducto}")
            print("\n\tAntibióticos:\n")
            for antibiotico in factura.pcantibioticos:
                print(f"\tNombre: {antibiotico.nombreProducto} - ${antibiotico.precio}")
                print(f"\tTipo Animal: {antibiotico.tipoAnimal}")
            print(f"\tValor total: ${factura.valorTotal}")
            count = count + 1

    def actualizar_factura(self, fecha_factura, nueva_fecha , facturas):
        for factura in facturas:
            if factura.fechaFactura == fecha_factura:
                factura.fechaFactura = nueva_fecha
                print("\tFactura actualizada exitosamente")
                return
        print("\tNo se encontró ninguna factura con esa fecha")

    def eliminar_factura(self, fecha_factura , facturas):
        for factura in facturas:
            if factura.fechaFactura == fecha_factura:
                facturas.remove(factura)
                print("\tFactura eliminada exitosamente")
                return
        print("\tNo se encontró ninguna factura con esa fecha")
