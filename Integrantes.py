import re
class ManejadorIntegrantesProyecto:
    __id = ''   #id del proyecto
    __an = ''   #apellido y nombre
    __dni = ''  #dni
    __ci = ''   #categoría de investigación
    __rol = ''  #rol
    def __init__(self, id = '', an = '', dni = '', ci = '', rol = ''):
        if(re.match('^[a-z0-9\,\+]{6,9}$', id.lower())):
            if(re.match('^[a-z\ \ã\-\¡\±]{2,30}', an.lower())):
                if(re.match('^[0-9]', dni.lower()) and len(dni) == 8):
                    if(re.match('^[a-z]{1,2}', ci.lower())):
                        if(re.match('^[a-z]{8,10}', rol.lower())):
                            self.__id = id
                            self.__an = an
                            self.__dni = dni
                            self.__ci = ci
                            self.__rol = rol
                        else: print('ERROR: rol inválido')
                    else: print('ERROR: categoría de investigación inválido')
                else: print('ERROR: dni inválido')
            else: print('ERROR: apellido y nombre inválidos')
        else: print('ERROR: id inválido')
    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.__id, self.__an, self.__dni, self.__ci, self.__rol)
    def getID(self):
        return self.__id
    def getCI(self):
        return self.__ci
    def getRol(self):
        return self.__rol