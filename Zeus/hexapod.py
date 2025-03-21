import serial
import time

# Configuración de conexión serial (ajusta el puerto según tu sistema)
puerto = 'COM3'  # Cambia esto al puerto correcto
velocidad_baudios = 9600

# Intenta conectar con el Arduino
try:
    print(f"Conectando al Arduino en el puerto {puerto}...")
    arduino = serial.Serial(puerto, velocidad_baudios, timeout=1)
    time.sleep(2)  # Espera a que se establezca la conexión
    print("Conexión establecida con el Arduino.")
except Exception as e:
    print(f"Error al conectar con el Arduino: {e}")
    exit()

# Función para enviar comandos al Arduino
def enviar_comando(comando):
    """
    Envía un comando al Arduino y muestra un mensaje de depuración.
    """
    try:
        print(f"Enviando comando: {comando.strip()}")  # Muestra el comando enviado
        arduino.write(comando.encode())  # Envía el comando al Arduino
    except Exception as e:
        print(f"Error al enviar el comando: {e}")

# Función para leer la respuesta del Arduino
def leer_respuesta():
    """
    Lee la respuesta del Arduino y la muestra en la consola.
    """
    try:
        while arduino.in_waiting > 0:  # Verifica si hay datos disponibles
            respuesta = arduino.readline().decode().strip()  # Lee la respuesta
            print(f"Respuesta del Arduino: {respuesta}")
    except Exception as e:
        print(f"Error al leer la respuesta: {e}")

# Funciones que envían comandos al Arduino para controlar el robot
def controlar_robot(accion):
    """
    Función para controlar el robot con base en una acción.
    Las acciones posibles son 'avanzar', 'retroceder', 'girar_izquierda', 'girar_derecha'.
    """
    acciones = {
        'avanzar': "AVANZAR\n",
        'retroceder': "RETROCEDER\n",
        'girar_izquierda': "GIRO_IZQUIERDO\n",
        'girar_derecha': "GIRO_DERECHO\n"
    }
    
    if accion in acciones:
        enviar_comando(acciones[accion])
        leer_respuesta()
    else:
        print(f"Acción desconocida: {accion}")

def mover_pierna(pierna, x, y, z):
    """
    Mueve una pierna del robot a las coordenadas especificadas.
    """
    enviar_comando(f"MOVER_PIERNA {pierna} {x} {y} {z}\n")
    leer_respuesta()

def cambiar_altura(altura):
    """
    Cambia la altura del cuerpo del robot.
    """
    enviar_comando(f"AJUSTAR_ALTURA {altura}\n")
    leer_respuesta()

# Ejemplo de control del robot con variables sencillas
if __name__ == "__main__":
    print("Iniciando control del robot...")

    # Variables de control
    accion = 'avanzar'  # Puede ser 'avanzar', 'retroceder', 'girar_izquierda', 'girar_derecha'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'girar_izquierda'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'retroceder'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'girar_derecha'
    controlar_robot(accion)
    time.sleep(2)

    # Control de piernas (puedes modificar las coordenadas)
    mover_pierna(1, 10, 20, 30)  # Mueve la pierna 1 a las coordenadas (10, 20, 30)
    time.sleep(2)

    # Cambiar altura (puedes cambiar el valor de altura)
    cambiar_altura(15)
    time.sleep(2)

    print("Control del robot completado.")
    
    # Cerrar la conexión serial
    arduino.close()
    print("Conexión serial cerrada.")


import serial
import time

# Configuración de conexión serial (ajusta el puerto según tu sistema)
puerto = 'COM3'  # Cambia esto al puerto correcto
velocidad_baudios = 9600

# Intenta conectar con el Arduino
try:
    print(f"Conectando al Arduino en el puerto {puerto}...")
    arduino = serial.Serial(puerto, velocidad_baudios, timeout=1)
    time.sleep(2)  # Espera a que se establezca la conexión
    print("Conexión establecida con el Arduino.")
except Exception as e:
    print(f"Error al conectar con el Arduino: {e}")
    exit()

# Función para enviar comandos al Arduino
def enviar_comando(comando):
    """
    Envía un comando al Arduino y muestra un mensaje de depuración.
    """
    try:
        print(f"Enviando comando: {comando.strip()}")  # Muestra el comando enviado
        arduino.write(comando.encode())  # Envía el comando al Arduino
    except Exception as e:
        print(f"Error al enviar el comando: {e}")

# Función para leer la respuesta del Arduino
def leer_respuesta():
    """
    Lee la respuesta del Arduino y la muestra en la consola.
    """
    try:
        while arduino.in_waiting > 0:  # Verifica si hay datos disponibles
            respuesta = arduino.readline().decode().strip()  # Lee la respuesta
            print(f"Respuesta del Arduino: {respuesta}")
    except Exception as e:
        print(f"Error al leer la respuesta: {e}")

# Funciones que envían comandos al Arduino para controlar el robot
def controlar_robot(accion):
    """
    Función para controlar el robot con base en una acción.
    Las acciones posibles son 'avanzar', 'retroceder', 'girar_izquierda', 'girar_derecha'.
    """
    acciones = {
        'avanzar': "AVANZAR\n",
        'retroceder': "RETROCEDER\n",
        'girar_izquierda': "GIRO_IZQUIERDO\n",
        'girar_derecha': "GIRO_DERECHO\n"
    }
    
    if accion in acciones:
        enviar_comando(acciones[accion])
        leer_respuesta()
    else:
        print(f"Acción desconocida: {accion}")

def mover_pierna(pierna, x, y, z):
    """
    Mueve una pierna del robot a las coordenadas especificadas.
    """
    enviar_comando(f"MOVER_PIERNA {pierna} {x} {y} {z}\n")
    leer_respuesta()

def cambiar_altura(altura):
    """
    Cambia la altura del cuerpo del robot.
    """
    enviar_comando(f"AJUSTAR_ALTURA {altura}\n")
    leer_respuesta()

# Ejemplo de control del robot con variables sencillas
if __name__ == "__main__":
    print("Iniciando control del robot...")

    # Variables de control
    accion = 'avanzar'  # Puede ser 'avanzar', 'retroceder', 'girar_izquierda', 'girar_derecha'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'girar_izquierda'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'retroceder'
    controlar_robot(accion)
    time.sleep(2)

    accion = 'girar_derecha'
    controlar_robot(accion)
    time.sleep(2)

    # Control de piernas (puedes modificar las coordenadas)
    mover_pierna(1, 10, 20, 30)  # Mueve la pierna 1 a las coordenadas (10, 20, 30)
    time.sleep(2)

    # Cambiar altura (puedes cambiar el valor de altura)
    cambiar_altura(15)
    time.sleep(2)

    print("Control del robot completado.")
    
    # Cerrar la conexión serial
    arduino.close()
    print("Conexión serial cerrada.")
