from ControladorHexapod import Hexapod
import time

# Crear una instancia del robot
robot = Hexapod()

# Conectar al robot
robot.conectar()

# Mover hacia adelante y esperar 2 segundos
robot.mover_adelante()
time.sleep(2)

# Mover hacia atrás y esperar 2 segundos
robot.mover_atras()
time.sleep(2)

# Girar a la izquierda y esperar 2 segundos
robot.mover_izquierda()
time.sleep(2)

# Girar a la derecha y esperar 2 segundos
robot.mover_derecha()
time.sleep(2)

# Activar el modo del robot
robot.modo_activo()
time.sleep(2)

# Cambiar la altura del cuerpo
robot.cambiar_altura(10)
time.sleep(2)

# Mover el cuerpo en 3 dimensiones
robot.mover_cuerpo(5, 0, 2)
time.sleep(2)

# Mover una pierna
robot.mover_pierna("F1", 2, 3, 1)
time.sleep(2)

# Establecer velocidad 3
robot.establecer_velocidad(3)
time.sleep(2)

# Rotar el cuerpo
robot.rotar_cuerpo()
time.sleep(2)

# Cambiar la velocidad a 50
robot.cambiar_velocidad(50)
time.sleep(2)

# Desconectar el robot
robot.desconectar()
