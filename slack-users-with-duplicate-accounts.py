# Identify users with duplicate accounts in Slack (Blackboard and Anthology emails) and deactivate the inactive one. 
import re

def eliminar_numeros(lista):
    # Expresión regular para eliminar los números de una cadena.
    patron = r'\d+'

    # Inicializamos una lista para almacenar los elementos procesados.
    elementos_procesados = []

    # Recorremos la lista original.
    for elemento in lista:
        # Utilizamos re.sub para reemplazar los números con una cadena vacía en cada elemento.
        elemento_procesado = re.sub(patron, '', elemento)
        elementos_procesados.append(elemento_procesado)

    return elementos_procesados


def usuarios_repetidos_con_estado(username, status):
    # Crear un diccionario para contar cuántas veces aparece cada usuario con el estado "Member".
    conteo = {}
    resultados = []

    # Recorremos las listas de usuarios y estados al mismo tiempo.
    for u, s in zip(username, status):
        if s == "Member":
            # Si el estado es "Member", incrementamos el contador para ese usuario.
            conteo[u] = conteo.get(u, 0) + 1

            # Si el usuario ha aparecido dos veces con "Member", lo agregamos a la lista de resultados.
            if conteo[u] == 2:
                resultados.append(u)

    return resultados
username = ['996589', 'anthony.vanwinkle', '997406']
username_without_numbers = eliminar_numeros(username)

states = ['Deactivated', 'Member', 'Deactivated']

# Obtener los nombres de usuario que se repiten dos veces con el estado "Member".
resultado = usuarios_repetidos_con_estado(username_without_numbers, states)
print(resultado)
