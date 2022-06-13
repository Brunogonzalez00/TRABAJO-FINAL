from cmath import sqrt
from enum import Enum
import time
import os

class Usuario:
    def __init__(self, usuario, nombre,edad,contrasenia,email):
        self.nombre = nombre
        self.edad = edad
        self.email=email
        self.usuario=usuario
        self.contrasenia=contrasenia

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getUsuario(self):
        return self.usuario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getContrasenia(self):
        return self.contrasenia

    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email =email

    def registrar(self):
        try:
            base_usuario = open("base_usuario.txt", 'r')
        except FileNotFoundError:
            open("base_usuario.txt", 'w')
        with open("base_usuario.txt", 'a') as base_usuario:
            base_usuario.write(
                f"{self.usuario} {self.nombre} {self.contrasenia} ")



class Cliente(Usuario):
    def __init__(self, usuario, nombre, edad, contrasenia,email,genero, peso, estatura, alergias,nivel_actividad_fisica,planBioFit):
        super().__init__(usuario,nombre,edad,contrasenia,email)

        self.peso = peso
        self.estatura = estatura
        self.alergias = alergias
        self.genero=genero
        self.entrenadores = []
        self.rutinas = []
        self.dietas=None
        self.nivelActividadFisica=nivel_actividad_fisica
        self.imc = peso / (estatura ** 2)
        self.indice_masa_corporal = self.imc
        self.nutricionistas=[]
        self.servicio=None
        self.planBioFit=planBioFit

    def getPeso(self):
        return self.peso

    def setPeso(self,peso):
        self.peso=peso

    def getEstatura(self):
        return self.usuario

    def setEstatura(self, usuario):
        self.usuario = usuario

    def setAlergias(self):
        return self.alergias

    def getAlergias(self):
        return self.alergias

    def nivel_actividad_fisica(self):
        return self.nivelActividadFisica

    def getnivelActividadFisica(self):
        return self.nivelActividadFisica

    def registrar(self):
        try:
            base_cliente = open("base_cliente.txt", 'r')
        except FileNotFoundError:
            open("base_cliente.txt", 'w')
        with open("base_cliente.txt", 'a') as base_cliente:
            base_cliente.write(
                f"{self.usuario} {self.contrasenia} {self.nombre} {self.edad} {self.peso} {self.estatura} {self.alergias}")

    def addEntrenador(self,entrenador):
        self.entrenadores.append(entrenador)

    def removeEntrenador(self, entrenador_to_remove):
        for index, item in enumerate(self):
            if item == entrenador_to_remove:
                del self[index]
                return
        raise ValueError('list.remove(x): entrenador not in list')

    def addNutricionistas(self,nutricionista):
        self.nutricionistas.append(nutricionista)

    def removeNutricionista(self, nutricionista_to_remove ):
        for index, item in enumerate(self):
            if item == nutricionista_to_remove:
                del self[index]
                return
        raise ValueError('list.remove(x): entrenador not in list')

   # def suscribirseGimnasio(self,gimnasio):
   #def suscribirseEmpresaFit

class PlanBiofit(Enum):
        ADELGAZAMIENTO="ADELGAZAMIENTO"
        GANANCIA_MUSCULAR="GANANCIA_MUSCULAR"
        PREPARACION_FISICA="PREPARACION_FISICA"

class Entrenador(Usuario):
    def __init__(self, usuario, nombre, edad, contrasenia,email,genero,especialidad, anios_experiencia, contacto):
        super().__init__(usuario,nombre,edad,contrasenia,email)

        self.genero = genero
        self.especialidad = especialidad
        self.años_experiencia = anios_experiencia
        self.contacto = contacto
        #o tbn lista alumnos cm prefieran
        self.lista_clientes=[]
        self.calendarioCliente=None



    def getEspecialidad(self):
        return self.especialidad

    def setEspecialidad(self,especialidad):
        self.especialidad=especialidad

    def getAniosExperiencia(self):
        return self.años_experiencia

    def setAniosExperiencia(self, anios_experiencia):
        self.años_experiencia =anios_experiencia

    def getContacto(self):
        return self.contacto

    def setContacto(self,contacto):
        return self.contacto

    def registrar(self):
        try:
            base_entrenadores = open("base_entrenadores.txt", 'r')
        except FileNotFoundError:
            open("base_entrenadores.txt", 'w')
        with open("base_entrenadores.txt", 'a') as base_entrenadores:
            base_entrenadores.write(
                f"{self.usuario} {self.contrasenia} {self.nombre} {self.edad} {self.especialidad} {self.contacto} {self.aptitudes}")

    def getClientes(self):
        for cliente in self.lista_clientes:
            print(cliente)

    def crearRutinaCliente(self):
        print("Creando rutina............")

        nombre_rutina = input("Ingrese el nombre de la rutina: ")
        tiempo_total=input("Ingrese el tiempo de la rutina")
        tiempo_descanso= input("Ingrese una opcion: ")
        series_cantidad=input("Ingrese la cantidad de series")
        repeticion_nro=input("Ingrese la cantidad de repeticiones por"
                             " ejercicio")
        ejercicio=input("Ingrese los ejercicios para la rutina") #Agregar objetos o clases Ejercicio
        nivel=input("A que nivel pertenece la rutina?")
        cliente=input("Para que cliente diseña la rutina?")
        Rutina(nombre_rutina,tiempo_total,tiempo_total,tiempo_descanso,series_cantidad,
               repeticion_nro,ejercicio,nivel,cliente)


    def crearRutina(self):
        op=""
        print("Creando rutina............")
        time.sleep(5)
        nombre_rutina = input("Ingrese el nombre de la rutina: ")
        tiempo_total=input("Ingrese el tiempo total de la rutina: ")
        nivel = input("A que nivel pertenece la rutina? : ")
        time.sleep(2)
        while op != "2":
            os.system("cls")
            print("///EJERCICIOS DE LA RUTINA \\\\\\")
            print("1. Agregar ejercicio a rutina")
            print("2. Salir")
            op = input("Ingrese una opcion: ")
            if op == "1":
                nombre_ejercicio=input("Descripcion del ejercicio: ")
                musculos=input("Musculos trabajados: ")
                tiempo_descanso = input("Tiempo descanso: ")
                series_cantidad = input("Ingrese la cantidad de series: ")
                repeticion_nro = input("Ingrese la cantidad de repeticiones por"
                                       " ejercicio : ")
                dificultad_ejercicio=input("Dificultad del ejercicio: ")
                lista_ejercicios=[]
                lista_ejercicios.append(Ejercicio(nombre_ejercicio,musculos,tiempo_total,tiempo_descanso,series_cantidad,repeticion_nro,dificultad_ejercicio))


        rutina=Rutina(nombre_rutina,lista_ejercicios,nivel)
        return rutina


class Rutina:
    def __init__(self, nombre,ejercicios,dificultad):
        self.nombre=nombre
        self.ejercicios=ejercicios
        self.dificultad=dificultad

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDificultad(self):
        return self.dificultad

    def setDificultad(self, dificultad):
        self.dificultad = dificultad

class Ejercicio:
    def __init__(self,nombre,musculos,tiempo_total,tiempo_descanso,series,repeticion,dificultad):

        self.nombre=nombre
        self.musculos=musculos
        self.dificultad=dificultad
        self.tiempo_total = tiempo_total
        self.tiempo_descanso = tiempo_descanso
        self.series = series
        self.repeticion = repeticion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getMusculos(self):
        return self.musculos

    def setMusculos(self, musculos):
        self.musculos = musculos


    def getTiempoTotal(self):
        return self.tiempo_total

    def setTiempoTotal(self, tiempoTotal):
        self.tiempo_total = tiempoTotal

    def getSeries(self):
        return self.series

    def setSeries(self, series):
        self.series = series

    def getRepeticion(self):
        return self.repeticion

    def setRepeticion(self, repeticion):
        self.repeticion = repeticion

    def getEjercicio(self):
        return self.ejercicio

    def setEjercicio(self, ejercicio):
        self.ejercicio = ejercicio

    def setDificultad(self, dificultad):
        self.dificultad = dificultad

class Dieta:
    def __init__(self, nombre, objetivo, descripcion,tipoDieta,fechaInicio,semanas,paciente,menus):
        self.nombre=nombre
        self.objetivo=objetivo
        self.descripcion=descripcion
        self.tipoDieta=tipoDieta
        self.menus=menus
        self.fechaInicio=fechaInicio
        self.semanas=semanas
        self.paciente=paciente

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getObjetivo(self):
        return self.objetivo

    def setObjetivo(self, objetivo):
        self.objetivo = objetivo

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion= descripcion

    def getTipoDieta(self):
        return self.tipoDieta

    def setTipoDieta(self, tipoDieta):
        self.tipoDieta = tipoDieta

    def getMenu(self):
        for menu in self.menus:
            print(menu)

    def addMenu(self,menu):
        self.menus.append(menu)


class Menu:
    def __init__(self,desayuno,comida,merienda,cena,dia):
        self.desayuno=desayuno
        self.comida=comida #podria llamarse tbn almuerzo
        self.merienda=merienda
        self.cena=cena
        self.dia=dia  #lunes,martes,miercoles,...,etc

    def getDesayuno(self):
        return self.desayuno

    def setDesayuno(self, desayuno):
        self.desayuno = desayuno

    def getComida(self):
        return self.comida

    def setComida(self, comida):
        self.comida = comida

    def getMerienda(self):
        return self.merienda

    def setMerienda(self, merienda):
        self.merienda = merienda

    def getCena(self):
        return self.tipoDieta

    def setCena(self, cena):
        self.cena =cena

    def getDia(self):
        return self.dia

    def setDia(self, dia):
        self.dia = dia

class Comida:
    def __init__(self,nombre,tipoComida,kcal,carbohidratos,grasas,proteinas,fibra):
        self.nombre=nombre
        self.tipoComida=tipoComida
        self.kcal=kcal
        self.carbohidratos=carbohidratos
        self.grasas=grasas
        self.proteinas=proteinas
        self.fibra=fibra

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipoComida(self):
        return self.tipoComida

    def setTipoComida(self, tipoComida):
        self.tipoComida = tipoComida

    def getKcal(self):
        return self.kcal

    def setKcal(self, kcal):
        self.kcal = kcal

    def setCarbohidratos(self,carbohidratos):
        self.carbohidratos = carbohidratos

    def getCarbohidratos(self):
        return self.carbohidratos

    def setGrasas(self, cena):
        self.cena = cena

    def getGrasas(self):
        return self.grasas

    def setProteinas(self, proteinas):
        self.proteinas = proteinas

    def setProteinas(self, proteinas):
        self.proteinas = proteinas

    def setFibras(self, fibras):
        self.fibra= fibras

    def setFibra(self, fibra):
        self.fibra = fibra


class Nutricionista(Usuario):
    def __init__(self, usuario, nombre,edad,contrasenia, email,genero,especialidad,anios_experiencia, contacto):
        super().__init__(usuario, nombre,edad, contrasenia, email)

        self.genero=genero
        self.especialidad= especialidad
        self.años_experiencia = anios_experiencia
        self.contacto=contacto
        self.pacientes=[]
        self.menus=[]
        self.dieta=None
        self.dias = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    def registrar(self):
        try:
            base_nutricionistas = open("base_nutricionistas.txt", 'r')
        except FileNotFoundError:
            open("base_nutricionistas.txt", 'w')
        with open("base_nutricionistas.txt", 'a') as base_nutricionistas:
            base_nutricionistas.write(
                f"{self.usuario} {self.contrasenia} {self.nombre} {self.edad} {self.especialidad} {self.contacto}")

    def addPaciente(self,paciente):
        self.pacientes.append(paciente)

    def getPacientes(self):
        for paciente in self.pacientes:
            print(paciente)

    def crearDieta(self):
        print("Creando Dieta..................")

        nombre = input("Ingrese el nombre de la dieta: ")
        objetivo = input("Ingrese el objetivo de la dieta: ")
        descripcion = input("Describa la dieta: ")
        tipoDieta= input("Ingrese el nombre del tipo de dieta: ") #Mediterranea, Vegana, Vegetariana
        fechaInicio = input("Cual es la fecha de inicio de dieta: ")
        Semanas = input("Ingrese cuantas semanas durara la dieta: ")
        paciente=input("Ingrese el nombre del paciente para la dieta: ")
        print("==================")
        print("Creando Menu..................")

        for dia in self.dias:
            # para cada uno ingresar una lista de comidas
            print("==================")
            print("DIA: "+dia)
            print("==================")
            time.sleep(1)
            desayuno = input("\nIngrese el desayuno planificado: ")
            comida=input("Ingrese la comida planificada: ")
            merienda = input("Ingresa la merienda planificada: ")
            cena = input("Ingrese la cena planificada: ")
            day=dia
            menu=Menu(desayuno,comida,merienda,cena,day)
            self.menus.append(menu)

        self.dieta = Dieta(nombre,objetivo,descripcion,tipoDieta,fechaInicio,Semanas,paciente,self.menus)
        return self.dieta


class Servicio(Enum):
    DIETAS="Dietas"
    ENTRENAMIENTOS="Entrenamientos"
    COMBO="Combo(Ambos)"


class Socio(Usuario):
    def __init__(self, usuario, nombre,contrasenia, email,direccion, contacto):
        super().__init__(usuario, nombre, contrasenia, email)

        self.direccion= direccion
        self.contacto = contacto


    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion


    def getContacto(self):
        return self.contacto

    def setContacto(self, contacto):
        return self.contacto

    def registrar(self):
        try:
            base_socios = open("base_socios.txt", 'r')
        except FileNotFoundError:
            open("base_socios.txt", 'w')
        with open("base_socios.txt", 'a') as base_socios:
            base_socios.write(
                f"{self.usuario} {self.contrasenia} {self.nombre} {self.contacto} {self.direccion}")


class Gimnasio:
    def __init__(self, usuario, nombre, contrasenia, email, direccion,horarios, contacto):
        super().__init__(usuario, nombre, contrasenia, email)

        self.direccion= direccion
        self.horarios = horarios
        self.contacto= contacto


    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getHorarios(self):
        return self.horarios

    def setHorarios(self, horarios):
        self.horarios = horarios

    def registrar(self):
        try:
            base_socios = open("base_socios.txt", 'r')
        except FileNotFoundError:
            open("base_socios.txt", 'w')
        with open("base_socios.txt", 'a') as base_socios:
            base_socios.write(
                f"{self.usuario} {self.contrasenia} {self.nombre} {self.contacto} {self.direccion} {self.horarios}")

class ControlActividades:
    def __init__(self, corrida, pasos, gimnasio, calorias):
        self.corrida = corrida
        self.pasos= pasos
        self.gimnasio = gimnasio
        self.calorias = calorias

    def getCorrida(self):
        return self.corrida

    def setCorrida(self, corrida):
        self.corrida = corrida

    def getPasos(self):
        return self.gastos

    def setPasos(self, pasos):
        self.pasos = pasos

    def getGimnasio(self):
        return self.gimnasio

    def setGimnasio(self, gimnasio):
        self.gimnasio = gimnasio

    def getCalorias(self):
        return self.calorias

    def setCalorias(self, calorias):
        self.calorias = calorias


class CalendarioCliente:
    def __init__(self, calendar, cliente):
        self.calendar = calendar
        self.cliente= cliente

    def getCalendar(self):
        return self.calendar

    def setCliente(self, cliente):
        self.cliente= cliente

    def getCliente(self):
        return self.cliente

class Calendar:
    def __init__(self, dia, semana,mes):
        self.dia = dia
        self.semana = semana
        self.mes=mes

    def getdia(self):
        return self.calendar

    def setDia(self, cliente):
        self.cliente = cliente

    def getSemana(self):
        return self.semana

    def setSemana(self,semana):
        self.semana=semana

    def getMes(self):
        return self.mes

    def setSemana(self,mes):
        self.mes=mes



brazos = ["Flexiones", "Triceps", "Push-ups", "Press Frances", "Pull-ups"]
piernas = ["Sentadillas", "Escaladoras", "Estocadas", "Caminada de Pato"]
abdominales = ["Abdominales", "Plancha", "Patadas de Bicicleta"]

clientes_clases = []
entrenador_clases = []
nutricionista_clases=[]
lista_rutinas=[]
lista_dietas=[]
rutinas_cliente=[]
entrenador=""
nutricionista=""
cliente=""
