import numpy as np
import csv 
from claseAlumno import Alumno
class manejadorAlumno : 
    
    def __init__(self):
        self.__arregloAlumnos = ""
        self.__estaOrdenado = False

    def cargarAlumnos(self):


        i=0
        archivo = open('Practica Integradora 2/Assets/alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')

        cont = 0
        archivo.__next__()

        for fila in reader:
            cont = cont+1


        self.__arregloAlumnos = np.empty(cont, dtype=Alumno)
        print(self.__arregloAlumnos)

        archivo.close()

        archivo = open('Practica Integradora 2/Assets/alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        archivo.__next__()
        
        for fila in reader: 

            print(fila)

            self.__arregloAlumnos[i]=Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
            
            i+=1



    def MostrarAlumnos(self): 

        i = 0 

        for i in range (len(self.__arregloAlumnos)):

            print(self.__arregloAlumnos[i].getApellidoyNombre())


    def Ordenar(self):
        if not self.__estaOrdenado:
            self.__arregloAlumnos.sort()
            self.__estaOrdenado = True


manager = manejadorAlumno()
manager.cargarAlumnos()
manager.MostrarAlumnos()


