class Alumno(): 
    __nombre = str 
    __apellido = str 
    __dni = str 
    __carrera = str 
    __anio = str 


    def __init__(self,dni,apellido,nombre,carrera,anio): 

        self.__nombre= nombre.title()
        self.__apellido = apellido.title()
        self.__dni = dni 
        self.__carrera = carrera.title()
        self.__anio = anio 



    def getDni(self): 
        
       return self.__dni 
    

    def getApellidoyNombre(self): 
        
        return self.__apellido+" "+ self.__nombre 

    def getAnio(self): 
    
        return self.__anio 


    def __lt__(self,otro): 

        if type(self)==type(otro):
            
            return self.__anio < otro.__anio or self.getApellidoyNombre() < otro.getApellidoyNombre()



