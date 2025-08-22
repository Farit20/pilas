# Crear la cola de nombres
colaNombres = []

# Ingresar 20 nombres a la cola
for i in range(1, 21):
    nombre = f"Nombre{i}"
    colaNombres.append(nombre)

print("Cola de nombres inicial:")
print(colaNombres)

# Sacar el primer nombre en FIFO (primer ingresado)
nombre_eliminado = colaNombres.pop(0)
print(f"\nNombre eliminado (FIFO): {nombre_eliminado}")

print("\nCola de nombres después de eliminar uno:")
print(colaNombres)
