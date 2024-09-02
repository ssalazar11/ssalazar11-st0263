# info de la materia: ST0263 

# Estudiante(s): Samuel Salazar Salazar, ssalazar1@eafit.edu.co

# Profesor: Ediwn Nelson Montoya Munera | Email: emontoya@eafit.edu.co

# Reto 1: Arquitectura p2p y comunicación entre procesos

# 1. breve descripción de la actividad

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Desarrollo de los nodos.
- Escalabilidad de la red a partir del soporte de entradas dinamica de nodos.
- Capacidad de busqueda de archivos entre nodos.
- Implementación de API REST
- Implementación de gRPC
- Concurrencia soportada
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Implementación de MOM
- Capacidad de ver los archivos que contiene cada nodo. (Se escribe por linea de comandos el archivo que se requiere)
- Montar el trabajo usando Docker

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

## Arquitectura

- Red decentralizada p2p
## Patrones

- Registro de nodos.
- actualizacion dinamica de nodos en la red.
- Cada nodo tiene la capacidad de cliente-servidor.
- Modularización del código

## Comunicación
- gRPC
- API REST

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Lenguaje de programación
- Python 3.12.5

## Librerias
- Flask 3.0.3
- grpcio 1.66.0
- grpcio-tools 1.66.0
- requests 2.32.3

## como se compila y ejecuta.
### 1. Clonar el trabajo.
Primero debemos clonar el repositorio:
`git clone `
### 2. Instalacion de dependencias
- Primero debe de instalar las librerías listadas anteriormente usando pip o el manejador de paquetes de su preferencia para Python:
  `pip install -r requirements.txt`
### 3. Ejecución del nodo.  
para ejecutar el nodo debe poner el siguiente comando en la terminal:  
`python main.py --config <archivo_de_configuracion.json>`  

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

El siguiente codigo es un ejemplo del json necesario para cada nodo

```json
{
    "node": {
      "ip": "",
      "port": ,
      "grpc_port": ,
      "bootstrap_peers": [""]
    },
    "resources": {
      "shared_directory": ""
    }
  }
  
```
- node.ip: Dirección IP del nodo.
- node.port: Puerto HTTP del nodo.
- node.grpc_port: Puerto gRPC del nodo.
- Resources.shared_directory: dirección de la carpeta con los archivos

## Nota
Para los primeros dos nodos, el nodo 1 debe tener la dirección ip del nodo 2 en "bootstrap_peers" y el nodo 2 debe tener la dirección ip del nodo 1.





