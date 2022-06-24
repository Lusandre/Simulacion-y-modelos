import random
dinero = 0
dineroT = 0
ronda = 0
rondaT = 0
corrida = 0
par = 0
impar = 0

print("Simulador de apuesta al lanzamiento de un dado.")
input("Precione enter para comenzar.\n")

for i in range(0, 100):
    dinero = 200
    ronda = 0
    while dinero > 0 and ronda < 100:
        ronda += 1
        ''''print(ronda)'''
        resultado = random.randint(1, 6)
        ''''print("dado", resultado)'''
        if resultado % 2 == 0:
            par += 1
            dinero += 10
        else:
            dinero -= 10
            impar += 1
    corrida += 1
    dineroT += dinero
    rondaT += ronda

print("Resultado:\nPromedio de rondas completadas:", rondaT/100)
print("Promedio de dinero en la cartera:", dineroT/100)
print("Veces que salio impar:", impar)
print("Veces que salio par:", par)
