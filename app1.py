artemis = []
sputnik = []

def menu ():
    while True: 
        print(" -------------------------MENU-------------------------- \n 1.  CREAR GRUPO ARTEMIS: \n 1.1 LISTAR CAMPERS DE ARTEMIS \n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERS DE ARTEMIS \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS \n 2.  CREAR GRUPO SPUTNIK: \n 2.1 LISTAR CAMPERS DE SPUTNIK \n 2.2 AGREGAR CAMPERS A SPUTNIK \n 2.3 ELIMINAR CAMPERS DE SPUTNIK \n 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK \n 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK \n Digite opcion:  ")
        respuesta = str(input())
        bandera = True
        bandera2 = True 
        if respuesta == "1":
            print("Creaste artemis")
        elif respuesta == "1.1":
            print(artemis)
        elif respuesta == "1.2":
            while bandera:
                agregar = input("Ingrese el nombre del estudiante:")
                artemis.append(agregar)
                opc = input("Quiere ingresar mas estudiantes? y/n:")
                if  opc == "n":
                    bandera = False
        elif respuesta == "1.3":
            print(artemis)
            eliminar = input("Que estudiante desea eliminar de la lista?:")
            for x in artemis:
                if x == eliminar:
                    artemis.remove(x)
        elif respuesta == "1.4":
            artemis.sort()
            print(artemis)
        elif respuesta == "1.5":
            buscar = input("que persona quiere buscar?")
            for i in artemis:
                if i == buscar:
                    print(buscar, "esta en artemis")
                else:
                    print(f"{buscar} no esta en artemis")
        if respuesta == "2":
            print("Creaste sputnik")
        elif respuesta == "2.1":
            print(sputnik)
        elif respuesta == "2.2":
            while bandera2:
                agregar = input("Ingrese el nombre del estudiante:")
                sputnik.append(agregar)
                opc = input("Quiere ingresar mas estudiantes? y/n:")
                if  opc == "n":
                    bandera2 = False
        elif respuesta == "2.3":
            print(sputnik)
            eliminar = input("Que estudiante desea eliminar de la lista?:")
            for x in sputnik:
                if x == eliminar:
                    sputnik.remove(x)
        elif respuesta == "2.4":
            sputnik.sort()
            print(sputnik)
        elif respuesta == "2.5":
            buscar = input("que persona quiere buscar?")
            for i in sputnik:
                if i == buscar:
                    print(buscar, "esta en sputnik")
                else:
                    print(f"{buscar} no esta en sputnik")
        else:
            break
menu()
