# Tarea06 Proceso Digital de Imagenes: Filtro Óleo

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY21xdG1xZ2xzaXoxbDdxYTNwOGRsaW4xOXJwZDV5dXdwNWJ2YzdqZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Z2y7SdhLm6Uq1pbc1q/giphy-downsized-large.gif"/>

## Author: Arrieta Mancera Luis Sebastian

# Dependencias

+ [Colorama](https://pypi.org/project/colorama/): `pip install colorama`
+ [Pillow](https://pypi.org/project/pillow/): `pip install pillow`
+ [Argparse](https://pypi.org/project/argparse/): `pip install argparse`

**Nota:** En caso de que no se especifique el tamaño de la matriz, el tamaño de la matriz será el equivalente a un 0.05% del tamaño de la imagen.

# Ejecución

Al ejecutar los ejemplos se generaran imagenes en el directorio `src/`

## Filtro Óleo: Escala de grises

Ejecución del archivo `filtro_oleo_escala_grises.py`

Para saber informacion sobre el programa y los parametros que acepta, ejecuta con **python** o **python3** el siguiente comando:

```bash
python3 filtro_oleo_escala_grises.py --help
```

### Ejemplos:

**Especificando el tamaño de la matriz**
```bash
python3 filtro_oleo_escala_grises.py ./imagenes/vangogh.png ./vangogh_oleo_gris_6x6.png --ms 6
```

**Sin especificar el tamaño de la matriz**
```bash
python3 filtro_oleo_escala_grises.py ./imagenes/vangogh.png ./vangogh_oleo_gris.png
```

## Filtro Óleo: Color

Ejecución del archivo `filtro_oleo_color.py`

Para saber informacion sobre el programa y los parametros que acepta, ejecuta con **python** o **python3** el siguiente comando:

```bash
python3 filtro_oleo_color.py --help
```

## Ejemplos:

**Especificando el tamaño de la matriz**
```bash
python3 filtro_oleo_color.py ./imagenes/vangogh.png ./vangogh_oleo_color_6x6.png --ms 6
```

**Sin especificar el tamaño de la matriz**
```bash
python3 filtro_oleo_color.py ./imagenes/vangogh.png ./vangogh_oleo_color.png
```

# Referencias:

+ [Blog de la morsa](https://la-morsa.blogspot.com/search?q=Oleo)


