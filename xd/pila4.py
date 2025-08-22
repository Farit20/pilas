pilaFia = []
pilaFia2 = []

# Ingresar 15 valores a la pila
for i in range(1, 16):
    pilaFia.append(i)

print("Pila inicial:", pilaFia)

# Lista de elementos a eliminar
elementos_a_eliminar = [7, 3]

for sacarD in elementos_a_eliminar:
    while pilaFia:
        temp = pilaFia.pop()
        if temp == sacarD:
            print(f"¡Número {sacarD} eliminado!")
            break
        else:
            pilaFia2.append(temp)

    # Restaurar los elementos en el orden original
    while pilaFia2:
        pilaFia.append(pilaFia2.pop())

print("Pila final (sin los números eliminados):", pilaFia)
