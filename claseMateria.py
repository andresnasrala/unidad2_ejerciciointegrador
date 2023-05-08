class Materia : 
    __dni = str 
    __nombremat = str 
    __fecha = str 
    __nota = float 
    __aprobacion = str 


    def __init__(self,dni,nombremat,fecha,nota,aprobacion):

        self.__dni = dni 
        self.__nombremat = nombremat 
        self.__fecha = fecha 
        self.__nota = nota 
        self.__aprobacion = aprobacion 

    def getDNI(self): 

        return self.__dni 
    
    def getNota(self): 

        return self.__nota 
    
    def getAprobacion(self): 

        return self.__aprobacion 
    
    def getNombreMateria(self): 

        return self.__nombremat