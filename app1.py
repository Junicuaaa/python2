atletas = []
while True:
    atleta = input("Ingresa el nombre del atleta: ")
    marca = float(input("Ingresa la marca de salto en metros: "))
    atletas.append([atleta, marca])
    if input("Desea agregar otro atleta? (s/n):  ") == "n":
        break

salto = 0
for atleta, marca in atletas:
    if marca > salto:
        salto = marca
        atleta_ganador = atleta

print("El atleta con el salto mas largo es {} con un salto de {} metros.".format(atleta_ganador, salto))