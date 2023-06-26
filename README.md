# DSSMitreATTCK

### Eva Gomez Pulido

### GITSIT - ETSI Telecomunicación - UPM

Este repositorio incluye todos los archivos necesarios para ejecutar el sistema desarrollado en el Trabajo de Fin de Grado.

## Estructura

### Ontologia
En esta carpeta se encuentra el archivo que define la ontología creada para desarrollar el DSS

### ResgistrosTrafico
En esta carpeta se encuentran dos archivos csv:
- **logsCICIDS.csv**: Archivo que contiene todos los registros del dataset CICIDS2017 tras un proceso de tratamienTo para adecuarlos al sistema. Los archivos originales pueden ser descargados en http://205.174.165.80/CICDataset/CIC-IDS-2017/ 
- **logsPrueba.csv**: Archivo que contiene una pequeña parte significativa del archivo anterior, en la que se ven representados todos los tipos de ataques.

### Script
Esta carpeta contiene el script que completa la ontología, automatizando distintos procesos.
Este script carga el archivo **logsPrueba.csv**. En caso de querer cargar todo el conjunto de datos habría que modificarlo para que cargase **logsCICIDS.csv**

## Ejecucion
Para ejecutar el sistema se deben descargar todos los archivos de este repositorio y almacenarlos dentro de un mismo directorio.
El unico requerimiento antes de ejectuar eel sript es disponer de la libreria OWLReady2 de Python mediante el siguiente comando

> pip install owlready2

A continuación, se podría ejecutar el script con el siguiente comando, dentro del directorio Script:

> python3 ontoScript.py








