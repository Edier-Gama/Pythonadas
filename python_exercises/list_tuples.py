def run():

    # Escribir un programa que almacene las asignaturas de un curso
    # (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en
    # una lista y la muestre por pantalla el mensaje Yo estudio
    # <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

    asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']

    for i in asignaturas:
        # print(f"Yo estudio {i}")
        pass

    #  Escribir un programa que almacene las asignaturas de un curso
    #  en una lista, pregunte al usuario la nota que ha sacado en
    #  cada asignatura, y después las muestre por pantalla con el mensaje
    #  En <asignatura> has sacado <nota>

    asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
    notas = []
    for i in asignaturas:
        nota = input(f"Cuanto sacaste en {i}? ")
        notas.append(nota)
    for i, x in zip(asignaturas, notas):
        print(f"En {i} sacaste {x}")




if __name__ == "__main__":
    run()
