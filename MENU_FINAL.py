import os
import time
from base_de_datos import *

op = ""
op2 = ""
op3 = ""
op4 = ""
op5 = ""
op6 = ""


while op != "0":
    print("///MENU PRINCIPAL\\\\\\")
    print("====================")
    print("1. Entrenador")
    print("2. Cliente")
    print("0. Salir")
    op = input("Ingrese una opcion: ")
    if op == "1":
        while op2 != "3":
            os.system("cls")
            print("///ENTRENADOR\\\\\\")
            print("================")
            print("1. Registrarse")
            print("2. Iniciar sesion")
            print("3. Volver")
            op2 = input("Ingrese una opcion: ")
            if op2 == "1":
                os.system("cls")
                usuario = input("Nickname: ")
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                genero = input("Genero: ")
                especialidad = input("Especialidad: ")
                años_experiencia = input("Años de experiencia: ")
                contacto = input("Numero de contacto: ")
                entrenador_clases.append(Entrenador(usuario, nombre, edad, genero, especialidad, años_experiencia, contacto))
                os.system("cls")
                print("Creando usuario...")
                time.sleep(5)
                print("El usuario se ha creado con exito!")
                time.sleep(3)
            elif op2 == "2":
                registro = input("Ingrese su Nickname: ")
                for i in entrenador_clases:
                    if i.usuario == registro:
                        print(f"Bienvenido {i.nombre} ")
                        time.sleep(3)
                        
    
    elif op == "2":
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
                edad = input("Edad: ")
                genero = input("Genero: ")
                peso = int(input("Peso: "))
                estatura = int(input("Estatura: "))
                cadera = int(input("Circunferencia de su cadera: "))
                objetivo = input("Objetivo a lograr: ")
                alergias = input("Alergias: ")
                clientes_clases.append(Cliente(usuario, nombre, edad, genero, peso, estatura, cadera, objetivo, alergias))
                os.system("cls")
                print("Creando usuario...")
                time.sleep(5)
                print("El usuario se ha creado con exito!")
                time.sleep(3)
                 
            elif op3 == "2":
                registro = input("Ingrese su Nickname: ")
                for i in clientes_clases:
                    if i.usuario == registro:
                        print(f"Bienvenido {i.nombre} ")
                        time.sleep(3)
                        while op4 != "3":
                            os.system("cls")
                            print("///ACCIONES\\\\\\")
                            print("==============")
                            print("1. Entrenamientos")
                            print("2. Calculadora de IMC e indice de grasa")
                            print("3. Salir")
                            op4 = input("Seleccione una opcion: ")
                            if op4 == "1":
                                while op5 != "0":
                                    print("ENTRENAMIENTOS")
                                    print("==============")
                                    print("1. Lunes, Miercoles y Viernes")
                                    print("2. Martes, Jueves y Sabado")
                                    print("3. Todos los dias")
                                    print("0. Salir")
                                    op5 = input("Seleccione una opcion: ")
                            elif op4 == "2":
                                while op6 != "3":
                                    print("CALCULADORA")
                                    print("1. IMC")
                                    print("2. Indice de Grasa")
                                    print("3. Salir")
                                    op6 = input("Ingrese una opcion: ")

                                    if op6 == 1:
                                        print(Cliente.self.imc)
                                    elif op6 == 2:
                                        print(Cliente.self.indice_grasa)