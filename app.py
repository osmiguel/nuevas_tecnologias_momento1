def opcion_default():
    print("Opción no válida digite nuevamente")
    print("--------------------")
    print(" ")

def mostrar_menu():
    print("Bienvenido a TuBiciApp que quieres hacer??:")
    print("Menú:")
    print("1. Registrarme en la plataforma")
    print("2. Prestar una bici")
    print("3. Buscar prestamos")
    print("4. Buscar Usuario")
    print("Para Salir del sistema presione X")
    opcion = input("escribir opción: ")
    return opcion

# definir lista de usuarios
usuarios = {}
prestamos = {}

opcion = mostrar_menu()

while opcion != "X":
    if opcion == "1":
        
        idTarjeta = input("Ingrese id de tarjeta primera letra de nombre y cuatro ulimos digitos del doc: ")
        usuarios[idTarjeta] = []
        
        nombre = input("Ingrese su nombre: ")
        usuarios[idTarjeta].append(nombre)

        apellido = input("Ingrese su apellido: ")
        usuarios[idTarjeta].append(apellido)

        correo = input("Ingrese su correo: ")
        usuarios[idTarjeta].append(correo)
        
        print ("Usuario agregado correctamente")
        print ("-----------------------")
        print (" ")
    
    elif opcion == "2":
        print ("-----------------------")
        print ("----- Presa tu Bici --------")
        print (" ")
        
        idTarjetaBuscada = input("Ingrese el id para hacer el prestamo: ")

        if idTarjetaBuscada in usuarios:
            datosUsuario = usuarios[idTarjetaBuscada]
            print("Buenvenid@:", datosUsuario[1])
            
            idBicicleta = input("Ingrese id de la bicicleta: ")
            prestamos[idBicicleta] = []
            
            idTarjeta = idTarjeta
            prestamos[idBicicleta].append(idTarjeta)
            
            nomUsuario = datosUsuario[0]
            prestamos[idBicicleta].append(nomUsuario)
            
            nomUsuario = datosUsuario[1]
            prestamos[idBicicleta].append(nomUsuario)
            
            origen = input("Ingrese su origen: ")
            prestamos[idBicicleta].append(origen)
            
            destino = input("Ingrese su destino: ")
            prestamos[idBicicleta].append(destino)
            
            print ("Bicicleta asignada")
            
            print ("-----------------------")
            
            # Agregamos la información del usuario al prestamo
            prestamos[idBicicleta].append(datosUsuario)
            
        else:
            print("El id de tarjeta no se encuentra registrado")
            print ("-----------------------")
            print (" ")
    
    elif opcion == "3":
        idBiciBuscada = input("Ingrese el id de bicicleta que desea buscar: ")

        if idBiciBuscada in prestamos:
            datosPrestamo = prestamos[idBiciBuscada]
            print("ID Tarjeta:", datosPrestamo[0])
            print("Nombre:", datosPrestamo[1])
            print("Origen:", datosPrestamo[3])
            print("Destino:", datosPrestamo[4])
            print ("-----------------------")
            print (" ")
           
        else:
            print("El id de bicicleta no se encuentra registrado")
            print ("-----------------------")
            print (" ")
            
    elif opcion == "4":
        idUsuarioBuscado = input("Ingrese el id de tarjeta que desea buscar: ")

        if idUsuarioBuscado in usuarios:
            datosUsuario = usuarios[idUsuarioBuscado]
            print(idUsuarioBuscado)
            print("Nombre:", datosUsuario[0])
            print("apellido:", datosUsuario[1])
            print("correo:", datosUsuario[2])
            print ("-----------------------")
            print (" ")
           
        else:
            print("El id de usuario no se encuentra registrado")
            print ("-----------------------")
            print (" ")
    else:
        opcion_default()
        
    opcion = mostrar_menu()
