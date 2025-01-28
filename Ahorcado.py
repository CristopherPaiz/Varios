import os
import random

# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    palabras = [
    "aire", "mar", "sol", "luna", "estrella", "cielo", "nube", "rio", "monte",
    "valle", "ciudad", "pueblo", "calle", "avenida", "parque", "jardin", "bosque",
    "arbol", "flor", "fruto", "semilla", "hoja", "rama", "raiz", "tierra", "agua",
    "fuego", "metal", "roca", "arena", "playa", "oceano", "lago", "isla", "continente",
    "mapa", "brujula", "nave", "barco", "avion", "tren", "coche", "bicicleta",
    "camino", "puente", "edificio", "casa", "ventana", "puerta", "techo", "habitacion",
    "cocina", "baño", "sala", "comedor", "silla", "mesa", "cama", "almohada",
    "manta", "espejo", "armario", "lampara", "libro", "cuaderno", "papel", "boligrafo",
    "lapiz", "dibujo", "pintura", "escultura", "arte", "musica", "cancion", "instrumento",
    "guitarra", "piano", "tambor", "flauta", "melodia", "ritmo", "danza", "teatro",
    "pelicula", "actor", "actriz", "escena", "guion", "director", "camara", "foto",
    "imagen", "sonido", "silencio", "voz", "palabra", "frase", "letra", "numero",
    "signo", "forma", "linea", "circulo", "cuadrado", "triangulo", "rectangulo",
    "diamante", "corazon", "animal", "perro", "gato", "caballo", "vaca", "cerdo",
    "oveja", "cabra", "raton", "pajaro", "pez", "insecto", "planta", "selva",
    "desierto", "montaña", "volcan", "planeta", "galaxia", "universo", "materia",
    "energia", "fuerza", "movimiento", "velocidad", "aceleracion", "tiempo", "espacio",
    "dimension", "punto", "superficie", "volumen", "angulo", "curva", "espiral",
    "circunferencia", "elipse", "parabola", "hiperbola", "poligono", "rombo",
    "trapecio", "esfera", "cilindro", "cono", "piramide", "cubo", "prisma", "tetraedro",
    "octaedro", "dodecaedro", "icosaedro", "poliedro", "geometria", "algebra",
    "aritmetica", "calculo", "estadistica", "probabilidad", "logica", "conjunto",
    "funcion", "limite", "derivada", "integral", "serie", "sucesion", "ecuacion",
    "inecuacion", "algoritmo", "programa", "codigo", "sistema", "internet",
    "computadora", "teclado", "pantalla", "raton", "software", "hardware", "usuario",
    "contraseña", "perfil", "correo", "archivo", "carpeta", "servidor", "nube",
    "enlace", "pagina", "sitio", "buscador", "blog", "foro", "chat", "mensaje",
    "noticia", "articulo", "columna", "revista", "periodico", "reportaje", "entrevista",
    "fotografia", "video", "audio", "radio", "television", "canal", "programacion",
    "emision", "serie", "documental", "reality", "concurso", "anuncio", "publicidad",
    "comercial", "pelicula", "cine", "teatro", "musica", "concierto", "festival",
    "disco", "cancion", "album", "gira", "tour", "espectaculo", "evento", "celebracion",
    "fiesta", "carnaval", "feria", "exposicion", "conferencia", "seminario", "taller",
    "curso", "clase", "escuela", "colegio", "instituto", "universidad", "academia",
    "profesor", "maestro", "alumno", "estudiante", "aprendiz", "conocimiento", "aprendizaje",]
    return random.choice(palabras)

# Función para mostrar el tablero del ahorcado
def mostrar_tablero(intentos):
    figura = [
        '''
               ♥♥♥♥♥♥
          +---¬
          |  \|
              |
              |
              |
              |
              |
        ========''',
        '''
               ♥♥♥♥♥
          +---¬
          |  \|
          ●   |
              |
              |
              |
              |
        ========''',
        '''
               ♥♥♥♥
          +---¬
          |  \|
          ●   |
          |   |
          |   |
              |
              |
        ========''',
        '''
               ♥♥♥
          +---¬
          |  \|
          ●   |
         /|   |
          |   |
              |
              |
        ========''',
        '''
               ♥♥
          +---¬
          |  \|
          ●   |
         /|\\  |
          |   |
              |
              |
        ========''',
        '''
               ♥
          +---¬
          |  \|
          ●   |
         /|\\  |
          |   |
         /    |
              |
        ========''',
        '''

          +---¬
          |  \|
          ●   |
         /|\\  |
          |   |
         / \\  |
              |
        ========'''
    ]
    print(figura[intentos])

# Función para jugar al ahorcado
def jugar_ahorcado():
    while True:
        palabra = obtener_palabra_aleatoria()
        letras_adivinadas = []
        intentos = 0

        while True:
            # Limpiar la pantalla
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n      A H O R C A D O')
            mostrar_tablero(intentos)
            print("\n")
            estado = ''
            for letra in palabra:
                if letra in letras_adivinadas:
                    estado += letra + ' '
                else:
                    estado += '_ '
            print(estado)


            if estado.replace(" ", "") == palabra:
                print('\n¡Felicidades! ¡Has adivinado la palabra correctamente!\n\n')
                break


            if intentos == 6:
                print('\n¡Oh no! Te has quedado sin intentos. La palabra era:', palabra.upper())
                print('\n\t¡G͢r͢a͢c͢i͢a͢s͢    p͢o͢r͢     j͢u͢g͢a͢r͢!\n\n')
                break

            #letras fallidas
            print('\nLetras fallidas:', ', '.join(letra for letra in letras_adivinadas if letra not in palabra))
            print('\n')
            letra = input('\nIngresa una letra: ').lower()

            if len(letra) != 1 or not letra.isalpha():
                print('')
                continue

            if letra in letras_adivinadas:
                print('')
                continue

            letras_adivinadas.append(letra)

            if letra not in palabra:
                intentos += 1
                print('La letra', letra, 'no está en la palabra. ¡Te quedan', 6 - intentos, 'intentos!')

        jugar_de_nuevo = input('¿Quieres jugar de nuevo? (Enter o S para continuar / N para salir): ').lower()
        #if S or s or enter = jugar de nuevo
        if jugar_de_nuevo == 's' or jugar_de_nuevo == '':
            continue
        else:
            print('')
            break

# Iniciar el juego
jugar_ahorcado()