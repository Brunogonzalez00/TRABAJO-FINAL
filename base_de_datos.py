from cmath import sqrt

import os




class Cliente:
    def __init__(self, usuario, nombre, edad, genero, peso, estatura, cadera, objetivo, alergias):
        
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.cadera = cadera
        self.objetivo = objetivo
        self.alergias = alergias
        self.usuario = usuario
        self.genero = genero
        self.entrenadores = None
        self.entrenamiento = None
        
        

        indice_grasa = cadera / (estatura * sqrt(estatura)) - 18
        imc = peso/(estatura**2)

        self.indice_masa_corporal = imc
        self.indice_grasa = indice_grasa
    def registrar(self):
        try:
            base_cliente = open("base_cliente.txt", 'r')
        except FileNotFoundError:
            open("base_cliente.txt", 'w')
        with open("base_cliente.txt", 'a') as base_cliente:
            base_cliente.write(f"{self.usuario} {self.nombre} {self.edad} {self.peso} {self.estatura} {self.cadera} {self.objetivo} {self.alergias}")

        
                
    

class Entrenador:
    def __init__(self,usuario, nombre, edad, genero, especialidad, años_experiencia, contacto):
        self.usuario = usuario
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia
        self.contacto = contacto


brazos = ["Flexiones", "Triceps", "Push-ups", "Press Frances", "Pull-ups"]
piernas = ["Sentadillas", "Escaladoras", "Estocadas", "Caminada de Pato"]
abdominales = ["Abdominales", "Plancha", "Patadas de Bicicleta"]

clientes_clases = []
entrenador_clases = []
