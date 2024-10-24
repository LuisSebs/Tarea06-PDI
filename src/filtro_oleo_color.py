# Autor: Arrieta Mancera Luis Sebastian
import math
import argparse
import numpy as np
from PIL import Image
from utils.progress_bar import progress_bar  # Importa la barra de progreso que ya tienes implementada
from utils.colores import random_color, rojo, verde, azul, reset

def filtro_oleo_color(imagen: Image, matriz_size: int = None):
    """
        Aplica el filtro oleo en color a una imagen.

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
    # Convertir la imagen a RGB
    imagen_color = imagen.convert('RGB')

    # Dimensiones de la imagen
    ancho, alto = imagen_color.size

    # Porcentaje de la imagen que tomaremos para la matriz
    porcentaje = 0.05
    matriz_size = int(math.sqrt(((ancho*alto)*porcentaje)/100)) if matriz_size is None else matriz_size

    # Desplazamiento
    step = matriz_size // 2
    
    # Imagen a regresar
    nueva_imagen = imagen.copy().convert('RGB')

    # Calcular el número total de píxeles a procesar (excluyendo bordes)
    total_pixeles = (ancho - 2 * step) * (alto - 2 * step)
    pixeles_procesados = 0
    ultimo_porcentaje_mostrado = 0

    # Colores randoms
    color = random_color()

    # Mensaje informativo
    print(azul+f"Generando imagen recursiva..."+reset)

    # Iteramos sobre la imagen
    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            # Definir el área del bloque
            bloque = imagen_color.crop((x - step, y - step, x + step, y + step))
            # Nuevo pixel
            nuevo_pixel = genera_pixel(bloque)
            # Agregamos el pixel
            nueva_imagen.putpixel((x,y), nuevo_pixel)
            # Actualizamos el contador de píxeles procesados
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
    print(verde+f"Imagen con filtro oleo a color creada ʕ•ᴥ•ʔ"+reset)
    
    return nueva_imagen

def genera_pixel(imagen: Image):
    """
        Genera un pixel en base a una imagen. 
        Calcula el histograma de la imagen y genera 
        un nuevo pixel en base a la frecuencia mayor 
        de cada canal

        Parameters :
        ------------

            imagen:
                imagen de la cual se generara el pixel
        
        Returns :
        ---------

            pixel en base al histograma de la imagen
    """
    valores_rojo = []
    valores_verde = []
    valores_azul = []
    # Iteramos sobre la nueva imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            r, g, b = imagen.getpixel((x,y))
            valores_rojo.append(r)            
            valores_verde.append(g)
            valores_azul.append(b)
    # Obtemeos los valores mayores
    mayor_rojo = mayor_frecuencia(histograma(valores_rojo))
    mayor_verde = mayor_frecuencia(histograma(valores_verde))
    mayor_azul = mayor_frecuencia(histograma(valores_azul))

    # Nuevo pixel
    nuevo_pixel = (mayor_rojo, mayor_verde, mayor_azul)
    
    return nuevo_pixel

def histograma(valores: list):
    """
        Genera un histograma de una lista de valores

        Parameters :
        ------------

            valores:
                lista de valores

        Returns :
        ---------

            histograma en forma de diccionario de una lista de valores
    """
    histograma = {}
    for valor in valores:
        if valor in histograma:
            histograma[valor] += 1
        else:
            histograma[valor] = 1
    return histograma

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
    mayor = None
    frecuencia = -1
    for clave, valor in histograma.items():
        if valor > frecuencia:
            frecuencia = valor
            mayor = clave
    return mayor
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que aplica el filtro oleo a color en una imagen")

    # Argumentos no opcionales
    parser.add_argument("imagen", help="Ruta de la imagen de entrada")
    parser.add_argument("salida", help="Ruta del archivo de salida")

    # Argumentos opcionales (Matriz Size)
    parser.add_argument("--ms", type=int, default=None, help="Tamaño de la matriz")

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
    filtro_oleo_color(imagen=imagen, matriz_size=args.ms).save(args.salida)
