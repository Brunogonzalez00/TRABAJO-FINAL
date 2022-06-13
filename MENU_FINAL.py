import os
import time
from base_de_datos import *

op = ""
op2 = ""
op3 = ""
op4 = ""
op5 = ""
op6 = ""
op7 = ""
op8 = ""
op9 = ""

while op != "0":
    print("///MENU PRINCIPAL\\\\\\")
    print("====================")
    print("1. Entrenador")
    print("2. Nutricionista")
    print("3. Cliente")
    print("0. Salir")
    op = input("Ingrese una opcion: ")
    if op == "1":
        while op2 != "4":
            os.system("cls")
            print("///ENTRENADOR\\\\\\")
            print("================")
            print("1. Registrarse")
            print("2. Iniciar sesion")
            print("3. Crear Rutinas")
            print("4. Volver")
            op2 = input("Ingrese una opcion: ")
            if op2 == "1":
                os.system("cls")
                usuario = input("Nickname: ")
                nombre = input("Nombre: ")
                contrasenia=input("Contraseña: ")
                edad = input("Edad: ")
                genero = input("Genero: ")
                email=input("email: ")
                especialidad = input("Especialidad: ")
                años_experiencia = input("Años de experiencia: ")
                contacto = input("Numero de contacto: ")
                entrenador=Entrenador(usuario, nombre, edad,contrasenia,email, genero, especialidad, años_experiencia, contacto)
                entrenador_clases.append(entrenador)
                os.system("cls")
                print("Creando usuario...")
                time.sleep(5)
                print("El entrenador se ha creado con exito!")
                time.sleep(3)
            elif op2 == "2":
                registro = input("Ingrese su Nickname: ")
                registro_contrasenia=input("Ingrese su Contraseña: ")
                for i in entrenador_clases:
                    if i.usuario == registro and i.contrasenia == registro_contrasenia:
                        print(f"Bienvenido {i.nombre} ")
                        time.sleep(3)
                    else:
                        print("Ocurrio un error al ingresar el usuario y/o la contraseña")

            elif op2 == "3":
                rutina=entrenador.crearRutina()
                lista_rutinas.append(rutina)
                time.sleep(4)
                print("La rutina se ha creado con exito!")
                time.sleep(3)

    elif op == "2":
        while op8 != "4":
            os.system("cls")
            print("///NUTRICIONISTA\\\\\\")
            print("================")
            print("1. Registrarse")
            print("2. Iniciar sesion")
            print("3. Crear Dieta")
            print("4. Volver")
            op8 = input("Ingrese una opcion: ")
            if op8 == "1":
                os.system("cls")
                usuario = input("Nickname: ")
                nombre = input("Nombre: ")
                contrasenia=input("Contraseña: ")
                edad = input("Edad: ")
                genero = input("Genero: ")
                email=input("email: ")
                especialidad = input("Especialidad: ")
                años_experiencia = input("Años de experiencia: ")
                contacto = input("Numero de contacto: ")
                nutricionista = Nutricionista(usuario, nombre, edad,contrasenia,email, genero, especialidad, años_experiencia, contacto)
                nutricionista_clases.append(nutricionista)
                os.system("cls")
                print("Creando usuario...")
                time.sleep(5)
                print("El nutricionista se ha creado con exito!")
                time.sleep(2)
            elif op8 == "2":
                registro = input("Ingrese su Nickname: ")
                registro_contrasenia=input("Ingrese su Contraseña: ")
                for i in nutricionista_clases:
                    if i.usuario == registro and i.contrasenia == registro_contrasenia:
                        print(f"Bienvenido {i.nombre} ")
                        time.sleep(3)
                    else:
                        print("Ocurrio un error al ingresar el usuario y/o la contraseña")

            elif op8 == "3":
                dieta = nutricionista.crearDieta()
                lista_dietas.append(dieta)
                time.sleep(5)
                print("La dieta se ha creado con exito!")
                time.sleep(2)

    elif op == "3":
        while op3 != "3":
            os.system("cls")
            print("///CLIENTE\\\\\\")
            print("=============")
            print("1. Registrarse")
            print("2. Iniciar sesion")
            print("3. Volver")
            op3 = input("Ingrese una opcion: ")
            if op3 == "1":
                os.system("cls")
                usuario = input("Nickname: ")
                nombre = input("Nombre: ")
                contrasenia=input("Contraseña: ")
                email=input("Email: ")
                edad = input("Edad: ")
                genero = input("Genero: ")
                peso = int(input("Peso: "))
                estatura = int(input("Estatura: "))
                alergias = input("Alergias: ")
                nivelActividad = input("NivelActividad: ")

                time.sleep(2)
                print("///Seleccione un plan\\\\\\")
                print("=============")
                print("1. ADELGAZAMIENTO")
                print("2. GANANCIA_MUSCULAR")
                print("3. PREPARACION_FISICA")

                op7 = input("Ingrese una opcion: ")
                if(op7 == "1"):
                    planbiofit=PlanBiofit.ADELGAZAMIENTO
                elif(op7 == "2"):
                    planbiofit=PlanBiofit.GANANCIA_MUSCULAR
                else:
                    planbiofit=PlanBiofit.PREPARACION_FISICA
                cliente=Cliente(usuario, nombre, edad,contrasenia, email,genero, peso, estatura, alergias,nivelActividad,planbiofit)
                clientes_clases.append(cliente)
                os.system("cls")
                print("Creando usuario...")
                time.sleep(5)
                print("El usuario se ha creado con exito!")
                time.sleep(2)

            elif op3 == "2":
                registro = input("Ingrese su Nickname: ")
                registro_contrasenia=input("Ingrese su Contraseña: ")
                for i in clientes_clases:
                    if i.usuario == registro and i.contrasenia == registro_contrasenia:
                        print(f"Bienvenido {i.nombre} ")
                        time.sleep(3)
                        os.system("cls")

                        print("///QUE SERVICIO ESTAS BUSCANDO? \\\\\\")
                        print("1. Dietas")
                        print("2. Entrenamientos")
                        op5 = input("Seleccione una opcion: ")
                        time.sleep(3)
                        if op5 == "1":
                            while op4 != "2":
                                print("///ACCIONES\\\\\\")
                                print("==============")
                                print("1. Ver Dietas")
                                print("2. Salir")
                                op4=input("Seleccione una opcion: ")
                                if op4 == "1":
                                    for d in lista_dietas:
                                        print(d.paciente)
                                        if(d.paciente == cliente.nombre):
                                            print("--------------")
                                            print("\nDieta: "+ d.nombre + "\nTipoDieta:" + d.tipoDieta)

                                            for menu in d.menus:
                                                print("--------------")
                                                print("dia" + menu.dia)
                                                print("--------------")
                                                print("desayuno: " + menu.desayuno)
                                                print("comida: " + menu.comida)
                                                print("merienda: " + menu.merienda)
                                                print("cena: " + menu.cena)
                                            print("--------------")
                                        else:
                                            print("Aun no tiene dieta asignada")

                        if op5 == "2":
                            while op6 != "2":
                                print("///ACCIONES\\\\\\")
                                print("==============")
                                print("1. Ver Rutinas")
                                print("2. Salir")

                                op6 = input("Seleccione una opcion: ")
                                if op6 == "1":
                                    for r in lista_rutinas:
                                        print(r)
                                        print("--------------")
                                        print("\nRutina: " + r.nombre + "\nDificultad:" + r.dificultad)
                                        print("\nEjercicios:")
                                        for ej in r.ejercicios:

                                            print("ejercicio: "+ ej.nombre)

                                        print("--------------")


