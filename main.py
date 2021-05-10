from Proyectos import ManejadorProyecto
from Integrantes import ManejadorIntegrantesProyecto
import csv
def test():
    print('Proyecto: ')
    id = input('ID: ')
    titulo = input('Título: ')
    pc = input('Palabras claves: ')
    proyecto = ManejadorProyecto(id, titulo, pc)
    print(proyecto)
    print('Integrante: ')
    id = input('ID: ')
    an = input('Apellido y Nombre: ')
    dni = input('DNI: ')
    ci = input('Categoría de investigación: ')
    rol = input('Rol: ')
    integrante = ManejadorIntegrantesProyecto(id, an, dni, ci, rol)
    print(integrante)
def reglaNegocio(listaProyectos, listaIntegrantes):
    #variables
    integrantes = [False, False]
    director = False
    codirector = False
    #tareas
    cint = 0  # cantidad de integrantes
    for i in range(len(listaProyectos)):
        print('|----Proyecto: {}----|'.format(listaProyectos[i].getTitulo()))
        for j in range(len(listaIntegrantes)):
            if ((listaProyectos[i].getID() == listaIntegrantes[j].getID()) and
                    (listaIntegrantes[j].getRol() == 'integrante')):  # cuenta los integrantes
                cint += 1
            if ((listaProyectos[i].getID() == listaIntegrantes[j].getID()) and
                    (listaIntegrantes[j].getRol().lower() == 'director')):  # busca si hay un director
                integrantes[0] = True
                if (listaIntegrantes[j].getCI().lower() == 'i' or listaIntegrantes[j].getCI().lower() == 'ii'):
                    director = True
            if ((listaProyectos[i].getID() == listaIntegrantes[j].getID()) and
                    (listaIntegrantes[j].getRol().lower() == 'codirector')):  # busca si hay un cdirector
                integrantes[1] = True
                if (listaIntegrantes[j].getCI().lower() == 'i' or listaIntegrantes[j].getCI().lower() == 'ii'
                        or listaIntegrantes[j].getCI().lower() == 'iii'):
                    codirector = True
        if (integrantes[0] == False):  # evalua si hay director y codirector
            print('-> El Proyecto debe tener un Director')
            listaProyectos[i].modP(-10)
        elif (integrantes[1] == False):
            print('-> El Proyecto debe tener un Codirector')
            listaProyectos[i].modP(-10)
        if (director == True):  # evalua la existencia del director
            listaProyectos[i].modP(10)
        else:
            listaProyectos[i].modP(-5)
            print('-> El Director del Proyecto debe tener categoría I o II')
        if (codirector == True):  # evalua la existencia del codirector
            listaProyectos[i].modP(10)
        else:
            listaProyectos[i].modP(-5)
            print('-> El Codirector del Proyecto debe tener categoría I o II o III')
        if (cint < 3):
            listaProyectos[i].modP(-20)
            print('-> El Proyecto debe tener como mínimo 3 integrantes')
        else:
            listaProyectos[i].modP(10)
        cint = 0
        director = False
        codirector = False
def ordenar(lista):
    aux = None
    min = 0
    cota = len(lista)
    k = 1
    while(k!=-1):
        k = -1
        for i in range(cota-1):
            if(lista[i+1]>lista[i]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                k = i
        cota = k
    mostrar(lista)
def mostrar(lista):
    for i in lista:
        print(i)
if __name__ == '__main__':
    if(input('¿Testear?: ')=='si'):
        test()
    else:
        #variables
        band = False
        archi1 = open('proyectos.csv')
        archi2 = open('integrantesProyecto.csv')
        listaProyectos = []
        listaIntegrantes = []
        #tareas
        #crea lista proyectos
        reader = csv.reader(archi1, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unProyecto = ManejadorProyecto(fila[0], fila[1], fila[2])
                listaProyectos.append(unProyecto)
        if(listaProyectos != None):
            print('DATO: proyectos.csv cargada')
        else: print('ERROR: proyectos.csv cargada incorrectamente')
        input()
        #crea lista integrantes
        reader = csv.reader(archi2, delimiter = ';')
        for fila in reader:
            if(band == True):
                band = False
            else:
                unIntegrante = ManejadorIntegrantesProyecto(fila[0], fila[1], fila[2], fila[3], fila[4])
                listaIntegrantes.append(unIntegrante)
        if(listaIntegrantes != None):
            print('DATO: integrantesProyecto.csv cargada')
        else: print('ERROR: integrantesProyecto.csv cargada incorrectamente')
        input()
        #reglas de negocio
        reglaNegocio(listaProyectos, listaIntegrantes)
        #ordenar lista
        ordenar(listaProyectos)
        #mostramos la lista