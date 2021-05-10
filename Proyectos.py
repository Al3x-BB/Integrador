import re
class ManejadorProyecto:
    __id = ''   #id del proyecto
    __titulo = ''   #título del proyecto
    __pc = ''   #palabras claves del proyecto
    __puntaje = 0
    def __init__(self, id = '', titulo = '', pc = ''):
        if(re.match('^[a-z0-9\,\+]{6,9}$', id.lower())):
            if(re.match('^[a-zA-Z0-9\ã\³\.\:\±\ ]{2,100}$', titulo.lower())):
                if(re.match('^[a-z\ã\³\ ]{2,100}', pc.lower())):
                    self.__id = id
                    self.__titulo = titulo
                    self.__pc = pc
                else: print('ERROR: palabras clave inválidas')
            else: print('ERROR: título inválido')
        else: print('ERROR: id inválido')
    def __str__(self):
        return "{} - {} - {}".format(self.__id, self.__titulo, self.__pc)
    def getTitulo(self):
        return self.__titulo
    def getID(self):
        return self.__id
    def getP(self):
        return self.__puntaje
    def modP(self, puntaje):
        self.__puntaje += puntaje
    def __gt__(self, other):
        return self.__puntaje > other.getP()