from claseMateria import Materia 
import csv
class ManejadorMateria: 

    __lista = []


    def __init__(self):

        self.__lista = []

    def cargarLista(self): 

        i=0
        archivo = open('Practica Integradora 2/Assets/materiasAprobadas.csv')
        reader = csv.reader(archivo,delimiter=';')

        archivo.__next__()

        for fila in reader : 
            
            materia = Materia(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(materia)



        
