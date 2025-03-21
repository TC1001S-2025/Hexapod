# Hexapod Controlado con Python

Este proyecto consiste en la creación de una libreria en Python para controlar el robot hexápodo FNK0031 a través de una placa Arduino, permitiendo el envío de instrucciones directamente desde Python.

# Objetivo

El objetivo de este es que se puedan ejecutar comandos básicos y fáciles de entender para que estudiantes de preparatoria puedan utilizarlos durante un taller educativo. 

# Librerías

Las librerías que ocupa este proyecto son 4 para Arduino (FNHR, FlexiTimer2, RF24, Servo) Pyserial para Python.


Las 4 librerías para Arduino se encuentran en el siguiente link:
https://freenove.com/fnk0031

En Arduino, la clase principal utilizada para el control del robot es FNHR. Esta clase interactúa con dos componentes clave:

communication: Maneja la conexión y comunicación con el robot.
robotAction: Controla las acciones físicas del Hexapod.


# Primera Forma de Implementación
Para conectar Arduino con Python, utilizamos las bibliotecas pyserial y time. pyserial permite establecer la conexión serial entre Python y Arduino, mientras que time nos ayuda a controlar las pausas en la ejecución.
# Segunda Forma de Implementación
La segunda forma de implementación consistió en utilizar SWIG (Simplified Wrapper and Interface Generator) para crear una interfaz entre el código C++ y Python. Con SWIG, podemos generar automáticamente los enlaces entre el código del robot y las funciones disponibles en Python, sin necesidad de reescribirlo.

# Códigos: 
Debido a la interrupción de nuestro proyecto gracias a problemas técnicos no tuvimos la oportunidad de probar y mejorar el codigo para alcanzar todos los objetivos establecidos previamente, sin embargo cada uno de los integrantes del equipo propuso una solución que abarcaba todos los aspectos faltantes, estos códigos finales se pueden encontrar en las evidencias individuales de cada estudiante, así como una explicación de la lógica dentro de los mismos o  otros elementos que consideramos importantes. Aunque cada código es diferente al final del día siguen el mismo objetivo.
# Implementación a futuro:
Implementación como Librería en Python
A futuro, el sistema funcionará de manera similar a la librería *Tello*, usada para drones. Se desarrollará un paquete de Python que permita controlar el hexápodo con funciones intuitivas como:  

robot.avanzar()
robot.girar_izquierda()
robot.bailar()

- La librería se encargará de la comunicación con Arduino de forma transparente para el usuario.  
- Se incluirían modos predefinidos como secuencias de baile y movimientos sincronizados.  
- Se integraría un instructivo detallado, explicando el uso sin necesidad de conocimientos previos en programación.  
Este enfoque permitirá que cualquier usuario, sin importar su nivel de experiencia, pueda programar y controlar el hexápodo de manera sencilla, transformándolo en una herramienta educativa y de desarrollo avanzada.


