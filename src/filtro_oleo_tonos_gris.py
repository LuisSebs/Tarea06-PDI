# Autor: Arrieta Mancera Luis Sebastian
import math
import argparse
import numpy as np
from PIL import Image
from utils.progress_bar import progress_bar  # Importa la barra de progreso que ya tienes implementada
from utils.colores import random_color, rojo, verde, azul, reset

def filtro_oleo_tonos_gris(imagen: Image, matriz_size: int = None):
    """
        Aplica el filtro oleo en tonos de gris a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a aplicarle el filtro
            
            matriz_size: 
                tamaño de la matriz
        
        Returns :
        ---------

            nueva imagen con el filtro aplicado
    """
    # Convertir la imagen a tonos de gris
    imagen_gris = imagen.convert('L')

    # Dimensiones de la imagen
    ancho, alto = imagen_gris.size

    # Porcentaje de la imagen que tomaremos para la matriz
    porcentaje = 0.05
    matriz_size = int(math.sqrt(((ancho*alto)*porcentaje)/100)) if matriz_size is None else matriz_size
    
    # Definir el tamaño del paso para el bloque de píxeles
    step = matriz_size // 2

    # Crear una copia para evitar modificar la imagen mientras la procesamos
    nueva_imagen = imagen.copy().convert('L')

    # Calcular el número total de píxeles a procesar (excluyendo bordes)
    total_pixeles = (ancho - 2 * step) * (alto - 2 * step)
    pixeles_procesados = 0
    ultimo_porcentaje_mostrado = 0

    # Colores randoms
    color = random_color()

    # Mensaje informativo
    print(azul+f"Generando imagen recursiva..."+reset)

    # Recorrer todos los píxeles de la imagen
    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            # Definir el área del bloque
            bloque = imagen_gris.crop((x - step, y - step, x + step, y + step))
            
            # Obtener el valor del píxel más frecuente en el bloque
            mayor = mayor_frecuencia(histograma(bloque))
            
            # Reemplazar el píxel actual con el valor de mayor frecuencia
            nueva_imagen.putpixel((x, y), mayor)

            # Actualizar el contador de píxeles procesados
            pixeles_procesados += 1

            # Calcular el porcentaje de progreso actual
            porcentaje_actual = (pixeles_procesados / total_pixeles) * 100

            # Mostrar el progreso solo si ha aumentado en un múltiplo de 2%
            if porcentaje_actual - ultimo_porcentaje_mostrado >= 2:
                progress_bar(pixeles_procesados, total_pixeles, color)
                ultimo_porcentaje_mostrado = porcentaje_actual
                color = random_color()

    # Mostramos el ultimo progreso
    progress_bar(pixeles_procesados, total_pixeles, color)
    print(verde+f"Imagen con filtro oleo en tonos de gris creada ʕ•ᴥ•ʔ"+reset)
    
    return nueva_imagen

def mayor_frecuencia(histograma: dict):
    """
        Regresa el valor con mayor frecuencia de un histograma

        Parameters :
        ------------
            
            histograma:
                histograma de pixeles representado en un diccionario
        
        Returns :
        ---------

            valor con mayor frecuencia del histograma
    """
    # Encontrar el valor de intensidad con la mayor frecuencia
    mayor = None
    frecuencia = -1
    for clave, valor in histograma.items():
        if valor > frecuencia:
            frecuencia = valor
            mayor = clave
    return mayor        

def histograma(imagen: Image):
    """
        Genera un histograma de una imagen

        Parameters :
        ------------

            imagen:
                imagen a calcular el histograma

        Returns :
        ---------

            histograma en forma de diccionario de una imagen
    """
    # Convertir el bloque de la imagen a un arreglo de NumPy
    area = np.array(imagen)
    
    # Aplanar los valores y contar las frecuencias de los tonos de gris
    valores = area.flatten()
    histograma_dict = {}
    
    # Crear el histograma con los valores del bloque
    for valor in valores:
        valor = int(valor)
        if valor in histograma_dict:
            histograma_dict[valor] += 1
        else:
            histograma_dict[valor] = 1
            
    return histograma_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que aplica el filtro oleo en tonos de gris a una imagen")

    # Argumentos no opcionales
    parser.add_argument("imagen", help="Ruta de la imagen de entrada")
    parser.add_argument("salida", help="Ruta del archivo de salida")

    # Argumentos opcionales (Matriz Size)
    parser.add_argument("--ms", type=int, default=None, help="Tamaño de la matriz. Si no especifica se calcula el tamaño de la matriz equivalente al 0.05 porciento del area de la imagen")

    # Parseamos los argumentos
    args = parser.parse_args()

    # Cargamos la imagen
    imagen = None
    try:
        imagen = Image.open(args.imagen)
    except Exception as e:
        print(rojo+f"Error al cargar la imagen: {e}"+reset)
        exit()
    
    # Aplicamos el filtro oleo y la guardamos
    filtro_oleo_tonos_gris(imagen=imagen, matriz_size=args.ms).save(args.salida)
