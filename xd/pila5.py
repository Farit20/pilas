# Crear la pila de nombres
pilaNombres = []

# Ingresar 20 nombres a la pila
for i in range(1, 21):
    nombre = f"Nombre{i}"
    pilaNombres.append(nombre)

print("Pila de nombres inicial:")
print(pilaNombres)

# Sacar el primer nombre en LIFO (último ingresado)
nombre_eliminado = pilaNombres.pop()
print(f"\nNombre eliminado (LIFO): {nombre_eliminado}")

print("\nPila de nombres después de eliminar uno:")
print(pilaNombres)

