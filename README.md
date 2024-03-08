# info de la materia: st-0263 Tópicos especiales en telematica
#
# Estudiante: Samuel Salazar Salazar, ssalazar1@eafit.edu.co
#
# Profesor: Juan Carlos Montoya Mendoza, jcmontoy@eafit.edu.co
#
# 

# 

# Reto1
#
# 1. breve descripción de la actividad
# 
<texto descriptivo>
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor 
Se logró la creación de los modulos de cliente y servidor, estos son capaces de listar los archivos que tenga cada nodo y tiene también pueden simular la carga y descarga de archivos.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor 
Los aspectos que no se pudo cumplir fue la conexión exitosa entre instancias. Si hubo una conexión entre nodos pero hubo errores a la hora de transferir la información de los archivos.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Se creó una red peer 2 peer en la cual cada nodo es representado por una instancia de AWS. Cada instancia tiene 3 archivos de codigo principales: el cliente, el servidor y la interfaz de servicio.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Para el cliente se utilizo node.js y las librerias usadas para esto reto es grpc-js para el uso de rpc, protoloader para cargar la interfaz de servicio y readline para recibir input desde consola.
Para el servidor se utilizó python y las librerias usadas fueron grpc, concurrent para permitir la concurrencia, os para leer los archivos que tiene la instancia, y configparser para leer el archivo .config que tiene todas las configuraciones del servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc
No es necesario configurar ningun tipo de parametro ya que cada servidor tiene su .config.


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Para ejecutar toda la red, simplemente se debe conectarse a la instancia y correr el archivo server.py en cada instancia, despues desde la instancia que quiera se inicia el client.js

# IP o nombres de dominio en nube o en la máquina servidor.
IP ServidorReto1: 3.85.49.250
IP ServidorReto2: 3.93.44.24
IP ServidorReto3: 54.81.74.155
ip ServidorReto4: 3.81.123.52


## una mini guia de como un usuario utilizaría el software o la aplicación
 Al iniciar el cliente habrá en menu en el que puede escoger que opción a realizar.
