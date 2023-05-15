from ui import ui
from crud.crud_cliente import CRUDClientes
from crud.crud_facturas import CRUDFacturas

def main():
    crud_cliente = CRUDClientes()
    crud_factura = CRUDFacturas()
    opcion = 1

    while (opcion!=0 and opcion!=7):

        ui.menu()
        opcion = ui.opcion()

        if(opcion>0 and opcion<=7):
            if (opcion==1):
                ui.espacio()
                cedula = ui.ingresarCedula()
                nombre = ui.ingresarNombreCliente()
                c = crud_cliente.crear_cliente(nombre, cedula)
            elif (opcion==2):
                ui.espacio()
                cedula = ui.ingresarCedula()
                c = crud_cliente.consultar_cliente(cedula)
                if not c:
                    ui.clienteInexistente()
            elif (opcion==3):
                ui.espacio()
                cedula = ui.ingresarCedula()
                nuevo_nombre = ui.ingresarNuevoNombreCliente()
                c = crud_cliente.modificar_cliente(cedula, nuevo_nombre)
                if (c==1):
                    ui.clienteInexistente()
            elif (opcion==4):
                ui.espacio()
                cedula = ui.ingresarCedula()
                c = crud_cliente.eliminar_cliente(cedula)
                if (c==1):
                    ui.clienteInexistente()
            elif (opcion==5):
                ui.espacio()
                eleccion = ui.preguntaSiHayCliente()
                if (eleccion == 1 or eleccion == 2):
                    cedula = ui.ingresarCedula()
                    if(eleccion == 1):
                        c = crud_cliente.consultar_cliente(cedula)
                        if (c == None):
                            ui.clienteInexistente()
                    else:
                        nombre = ui.ingresarNombreCliente()
                        c = crud_cliente.crear_cliente(nombre, cedula)
                    if ( not None):
                        fecha = ui.ingresarFechaFactura()
                        factura = crud_factura.crear_factura(fecha)
                        cantidad_productos = ui.cantidadProductos()
                        for i in range(0, cantidad_productos):
                            ui.espacio()
                            producto = ui.elegirProducto()
                            ui.espacio()
                            nombre_producto = ui.ingresarNombreProducto()
                            precio = ui.ingreseValorProducto()
                            if (producto != 3):
                                registro_ICA = ui.ingresarRegistroICA()
                                frecuencia = ui.ingresarfrecuenciaProducto()
                                if (producto == 1):
                                    periodo = ui.ingresarPeriodoCarencia()
                                    factura = crud_factura.agregar_control_plagas(factura , registro_ICA , nombre_producto , frecuencia , precio, periodo)
                                else:
                                    fecha = ui.ingresarFechaUltimaAplicacion()
                                    factura = crud_factura.agregar_fertilizante(factura , registro_ICA , nombre_producto , frecuencia , precio, fecha)
                            else:
                                dosis = ui.ingresarDosis()
                                tipo_animal = ui.ingresarTipoAnimal()
                                factura = crud_factura.agregar_antibiotico(factura , nombre_producto , dosis , tipo_animal , precio)
                        crud_cliente.agregar_factura(c , factura)
            elif (opcion == 6):
                ui.espacio()
                cedula = ui.ingresarCedula()
                c = crud_cliente.consultar_cliente(cedula)
                if not c:
                    ui.clienteInexistente()
                else:
                    facturas = crud_cliente.obtener_facturas_cliente(c)
                    if facturas != [] : 
                        crud_factura.leer_facturas(facturas)
                    else:
                        ui.noHayFacturas()
            elif (opcion==7):
                ui.espacio()
                break
        elif opcion!=0:
            ui.opcionIncorrecta()
main()