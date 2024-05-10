# imports
import menu,os,time,Functions

while True: # bucle principal
    menu.menu()
    try:
        option = menu.eleccion()
        # USUARIO
        if option == 1:
                while True:
                    os.system("clear")
                    menu.menuUser() # menu usuario
                    option = menu.eleccion()
                    os.system("clear")
                    if option == 1:
                        while True: # Mostrar catalogo de servicios
                            Functions.MostrarCatalogo("ServiciosDataBase.json")
                            print("----------")
                            print("[1] VOLVER")
                            print("----------")
                            option = menu.eleccion()
                            if option == 1: # Mostrar catalogo de productos
                                os.system("clear")
                                break # catalogo de servicios
                    elif option == 2: # Mostrar catalogo de productos
                        while True:
                            Functions.MostrarCatalogo("ProductosDataBase.json")
                            print("----------")
                            print("[1] VOLVER")
                            print("----------")            
                            option = menu.eleccion()
                            if option == 1:
                                os.system("clear")
                                break
                    elif option == 3:
                        while True:  # servicio al cliente
                            datos = Functions.CargarDatos("ConsultasDataBase.json")
                            menu.menuServicioAlCliente()
                            option = menu.eleccion()
                            if option == 1:
                                consulta = str(input("INGRESA LA CONSULTA QUE DESEAS\n>> "))
                                for dato in datos.values():
                                    datos = dato.append(consulta)
                                    
                            elif option == 2:
                                None
                            elif option == 3:
                                break                                    
                    elif option == 4:
                        None # reclamos
                    elif option == 5:
                        None # sugerencias
                    elif option == 6:
                        break # Volver al menu principal
                    else:
                        while True:
                            print("---------------")
                            print("OPCION INVALIDA")
                            print("---------------")
                            time.sleep(1)
                            os.system("clear")
                            break
            
        
        # ADMINISTRADOR 
        elif option == 2:
            os.system("clear")
            menu.menuAdmin() # mostrar menu admin
            option = menu.eleccion()
            while True: # Bucle menuAdmin
                if option == 1:
                     None # mostrar usuarios
                elif option == 2:
                    None # mostrar servicios
                elif option == 3:
                    break # volver al menu
                else:
                    os.system("clear")
                    print("------------------")
                    print("OPCION INVALIDA!!!")
                    print("------------------")
                    time.sleep(1)
                    os.system("clear")
                    break
        elif option == 3: # salir del programa
            os.system("clear")
            break
        else:
            os.system("clear")
            print("------------------")
            print("OPCION INVALIDA!!!")
            print("------------------")
            time.sleep(1)
            os.system("clear")
    except ValueError:
            os.system("clear")
            print("----------------")
            print("VALOR INVAlIDO!!")
            print("----------------")
            time.sleep(1)
            os.system("clear")
