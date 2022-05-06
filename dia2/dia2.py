with open("input2.txt") as f:
    reader = f.readlines()

#movimiento = {"forward": 0,"down": 0, "up": 0}

# for the first part
#for linea in reader:
#    comando, n = linea.rstrip().split()
#    n = int(n)
#    movimiento[comando] += n
#distancia = movimiento["forward"]
#profundidad = movimiento["down"] - movimiento["up"]
#print(distancia*profundidad)

horizontal, profundidad, aim = 0, 0, 0
for linea in reader:
    comando, n = linea.rstrip().split()
    n = int(n)
    if comando == "down":
        aim += n
    elif comando == "up":
        aim -= n
    else:
        horizontal += n
        profundidad += aim*n

print(profundidad*horizontal)

