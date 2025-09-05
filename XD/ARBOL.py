# Ejemplo de implementación de un árbol genealógico en Python
# Abol no binario, cada nodo puede tener múltiples hijos
# Cada nodo representa a una persona con su nombre  
#Es el constructor de la clase. Se ejecuta cuando se crea una nueva instancia del árbol
class Arbol:
    def __init__(self, elemento):
        self.hijos = [] #Inicializa una lista vacía que almacenará los nodos hijos del nodo actual. Esto permite que cada nodo tenga múltiples hijos.
        self.elemento = elemento #Guarda el valor o contenido del nodo

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre)
    subarbol.hijos.append(Arbol(elemento))


def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None
# Ejemplo de uso
abuela = "Donatila"
hija1 = "Imelda"
hija2 = "Rosa"
hija3 = "Eliana"
nieto1 = "Valhery"
nieta2 = "Astrid"
nieta3 = "Farit"
nieto4 = "Shenya"
nieto5 = "Ivanna"    
nieto6 = "Sheyna"    
arbol = Arbol(abuela)

agregarElemento(arbol, hija2, abuela)
agregarElemento(arbol, hija3, abuela)
agregarElemento(arbol, nieto4, hija2)
agregarElemento(arbol, hija1, abuela)
agregarElemento(arbol, nieto1, hija1)
agregarElemento(arbol, nieta2, hija1)
agregarElemento(arbol, nieta3, hija1)
agregarElemento(arbol, nieto5, hija3)
agregarElemento(arbol, nieto6, hija3)

def imprimirArbol(arbol, nivel=0):
    print("  " * nivel + arbol.elemento)
    for hijo in arbol.hijos:
        imprimirArbol(hijo, nivel + 1)

def eliminarPorEntrada(arbol):
    nombre = input(" Ingresa el nombre del elemento que deseas eliminar: ")
    eliminado = eliminarElemento(arbol, nombre)
    if not eliminado:
        print(f" No se encontró el elemento '{nombre}' en el árbol.")
        
def eliminarElemento(arbol, elemento):
    if arbol.elemento == elemento:
        print("No se puede eliminar el nodo raíz.")
        return False

    for i, hijo in enumerate(arbol.hijos):
        if hijo.elemento == elemento:
            del arbol.hijos[i]
            print(f"Nodo '{elemento}' eliminado correctamente.")
            return True
        else:
            if eliminarElemento(hijo, elemento):
                return True
    return False



# Imprimir el árbol antes
print("🌳 Árbol genealógico actual:")
imprimirArbol(arbol)

# Eliminar por entrada del usuario
eliminarPorEntrada(arbol)

# Imprimir el árbol después
print("\n🌳 Árbol actualizado:")
imprimirArbol(arbol)
