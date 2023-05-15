def menu():
    print("\n\t ------------------------------")
    print("\t|             Menú             |")
    print("\t|------------------------------|")
    print("\t| 1. Crear cliente.            |")
    print("\t| 2. Consultar cliente.        |")
    print("\t| 3. Modificar cliente.        |")
    print("\t| 4. Eliminar cliente.         |")
    print("\t| 5. Crear factura.            |")
    print("\t| 6. Consultar facturas.       |") 
    print("\t| 7. Salir.                    |")
    print("\t ------------------------------")

def opcion():
    print('\n')
    opcionMenu = int(input("\tIngrese una opción: "))
    return opcionMenu

def opcionIncorrecta():
    print("\n\tLa opción ingresada no esta disponible, ingrese otra opción\n")

def ingresarCedula():
    cedula = input("\tIngrese el número de cédula: ")
    return cedula

def ingresarNombreCliente():
    nombre_cliente = input("\tIngrese el nombre del cliente: ")
    return nombre_cliente

def ingresarNuevoNombreCliente():
    nombre_cliente = input("\tIngrese el nuevo nombre: ")
    return nombre_cliente

def espacio():
    print("\n")

def clienteInexistente():
    print("\n\tEste cliente no se encuentra registrado.\n")

def noHayFacturas():
    print("\n\tNo se encuentraron facturas registradas.\n")

def clienteCreado():
    print("\n\tEl cliente se ha creado exitosamente")

def preguntaSiHayCliente():
    eleccion = int(input("\n\tEscriba 1 si hay un cliente existente para asociar la factura\n\tEscriba 2 si desea crear un cliente\n\tCualquier otra cosa se tomará como una petición cancelada.\n\topcion: "))
    return eleccion

def ingresarFechaFactura():
    fecha = input("\tIngrese la fecha de la factura: ")
    return fecha

def cantidadProductos():
    cantidad = int(input("\tCuantos productos desea agregar? (escriba un numero): "))
    return cantidad

def elegirProducto():
    producto = 0
    while (producto != 1 and producto != 2 and producto != 3):
        producto = int(input("\tEscriba 1 si desea agregar un control plagas\n\tEscriba 2 si desea agregar fertilizante\n\tEscriba 3 si desea Agregar un antibiotoco: "))
    return producto

def ingresarRegistroICA():
    registro = input("\tIngrese el registro ICA del producto: ")
    return registro

def ingresarNombreProducto():
    nombre_producto = input("\tIngrese el nombre del producto: ").lower()
    return nombre_producto

def ingresarfrecuenciaProducto():
    frecuencia_producto = input("\tIngrese la frecuencia de aplicación del producto: ")
    return frecuencia_producto

def ingresarPeriodoCarencia():
    periodo = input("\tIngrese el periodo de carencia del producto: ")
    return periodo

def ingresarFechaUltimaAplicacion():
    fecha = input("\tIngrese la fecha de ultima aplicacion del producto: ")
    return fecha

def ingresarDosis():
    dosis = int(input("\tIngrese la dosis del producto en kg: "))
    return dosis

def ingresarTipoAnimal():
    tipo_animal = 'animal'
    while (tipo_animal != "bovino" and tipo_animal != "caprino" and tipo_animal != "porcino" and tipo_animal != "bovinos" and tipo_animal != "caprinos" and tipo_animal != "porcinos"):
        tipo_animal = input("\tIngrese el tipo de animal (Bovino(s), Caprino(s) o Porcino(s)): ").lower()
    return tipo_animal

# def tipoAnimalErroneo():
#     print("\n\tEste tipo de animal erróneo.\n")

def ingreseValorProducto():
    valor = int(input("\tIngrese el precio del producto: "))
    return valor