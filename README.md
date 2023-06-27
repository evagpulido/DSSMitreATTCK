# DSSMitreATTCK

### Eva Gomez Pulido

### GITSIT - ETSI Telecomunicación - UPM

Este repositorio incluye todos los archivos necesarios para ejecutar el sistema desarrollado en el Trabajo de Fin de Grado.

## Requisitos
En primer lugar, se debe trabajar en un entorno que tenga Python instalado. De no ser así, se puede instalar desde el sitio web oficial https://www.python.org/downloads/ .

El único requisito antes de ejecutar el script de Python es disponer de la librería OWLReady2, la cual se puede instalar mediante el siguiente comando:
> pip install owlready2

En el caso de los notebooks de JupyterLab, se debe disponer de esta herramienta en el sistema, el cual trabaja también con Python. Si se tiene Python instalado, se procede a instalar JupyterLab con el siguiente comando:
> pip install jupyterlab



## Estructura

### Ontologia
En esta carpeta se encuentra el archivo que define la ontología creada para desarrollar el DSS

### Preprocesamiento
En esta carpeta se encuentran los notebooks de JupyterLab utilizados para preprocesar los datoso riginales del dataset.
- **ArchivosFiltrados.ipynb**: convierte cada archivo del dataset CICIDS2017 en un DataFrame y guarda únicamente los atributos de interés de cada registro.
- **CombinarTodos.ipynb**: une todos los DataFrames anteriores en uno y lo transforma a un archivo csv.
- **TransformarWebAttacks.ipynb**: realiza las modificaciones necesarias a causa de unas irregularidades encontradas.

### ResgistrosTrafico
En esta carpeta se encuentran dos archivos csv:
- **logsCICIDS.csv**: Archivo que contiene todos los registros del dataset CICIDS2017 tras un proceso de tratamienTo para adecuarlos al sistema. Los archivos originales pueden ser descargados en http://205.174.165.80/CICDataset/CIC-IDS-2017/ 
- **logsPrueba.csv**: Archivo que contiene una pequeña parte significativa del archivo anterior, en la que se ven representados todos los tipos de ataques.

### Script
Esta carpeta contiene el script que completa la ontología, automatizando distintos procesos.
Este script carga el archivo **logsPrueba.csv**. En caso de querer cargar todo el conjunto de datos habría que modificarlo para que cargase **logsCICIDS.csv**

## Ejecucion
Para ejecutar el sistema se deben descargar todos los archivos del repositorio y almacenarlos dentro de un mismo directorio.

Para ejecutar el script de Python, dentro del directorio Script se ejecuta el siguiente comando:
> python3 ontoScript.py

Para los notebooks de JupyterLab, se ejecuta el siguiente comando desde una terminal dentro del directorio Preprocesamiento:
> jupyter lab

Esto abrirá JupyterLab en el navegador web predeterminado y desde ahí se podrá trabajar con los notebooks descargados desde GitHub. 









