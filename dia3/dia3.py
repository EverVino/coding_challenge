with open("input3.txt") as f:
    reader = f.readlines()
#lista = [ 0 for _ in range(12)]
#for line in reader:
#    n_lista = [int(x)  for x in list(line.rstrip())]
#    lista = [lista[i] + n_lista[i] for i in range(12)]
#    print(lista)
#
#gamma, epsilon = "", ""
#
#for n in lista:
#    if len(reader) - int(n) > len(reader)//2:
#        gamma += "0"
#        epsilon += "1"
#    else:
#        gamma += "1"
#        epsilon += "0"
#
#print(int(gamma,2)*int(epsilon,2))

p = 0
filas = len(reader)
validO = [x.rstrip() for x in reader]
while filas > 1:
    suma = sum([int(numero[p]) for numero in validO])
    if suma - filas/2 >= 0:
        validO = [validO[i] for i in range(filas) if validO[i][p] == "1"]
    else:
        validO = [validO[j] for j in range(filas) if validO[j][p] == "0"]
    p += 1
    filas = len(validO)

p = 0
filas = len(reader)
validC = [y.rstrip() for y in reader]

while filas > 1:
    suma = sum([int(numero[p]) for numero in validC])
    if suma - filas/2 >= 0:
        validC = [validC[i] for i in range(filas) if validC[i][p] == "0"]
    else:
        validC = [validC[i] for i in range(filas) if validC[i][p] == "1"]
    p += 1
    filas =len(validC)

print(int(validC[0],2)*int(validO[0],2))
