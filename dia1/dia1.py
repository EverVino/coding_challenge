def check_increasing(datos):
    S = 0
    for i in range(1, len(datos)):
        if datos[i] - datos[i-1] > 0:
            S += 1
    return S 

with open("input1.txt") as f:
    reader = f.readlines()

datos = [int(n[:-1]) for n in reader]

print(check_increasing(datos))

datos3 = [sum(datos[i-3:i]) for i in range(3, len(datos)+1)]

print(check_increasing(datos3))

