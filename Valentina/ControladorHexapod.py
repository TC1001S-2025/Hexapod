import serial  # Importa la librería serial para la comunicación con el hardware
import time    # Importa la librería time para poder usar delays

class Hexapod:
    """
    Clase que representa un robot hexápodo controlado a través de comandos seriales.
    """

    def __init__(self, puerto='COM3', velocidad=9600):
        """
        Inicializa la conexión con el hexápodo a través del puerto serial.

        Args:
            puerto (str): El puerto serial al que se conecta el hexápodo (por defecto 'COM3').
            velocidad (int): La velocidad de comunicación en baudios (por defecto 9600).
        """
        try:
            # Establece la conexión serial con el hexápodo
            self.conexion = serial.Serial(puerto, velocidad, timeout=1)
            time.sleep(2)  # Espera 2 segundos para garantizar que la conexión esté establecida
            print("Conexión establecida con el hexápodo.")
        except Exception as e:
            # Maneja cualquier excepción en la conexión
            print(f"Error al conectar: {e}")

    def enviar_comando(self, comando):
        """
        Envía un comando al hexápodo.

        Args:
            comando (str): El comando que se enviará al hexápodo.
        """
        try:
            # Envia el comando codificado en bytes
            self.conexion.write(f"{comando}\n".encode())
            print(f"Comando enviado: {comando}")
        except Exception as e:
            # Maneja cualquier error al enviar el comando
            print(f"Error al enviar comando: {e}")

    def conectar(self):
        """
        Inicia la conexión y envía el comando de inicio al hexápodo.
        """
        print("Conectando al hexápodo...")
        self.enviar_comando("START")  # Envia el comando para iniciar la conexión

    def mover_adelante(self):
        """
        Envía el comando para mover el hexápodo hacia adelante.
        """
        self.enviar_comando("CRAWL_FORWARD")

    def mover_atras(self):
        """
        Envía el comando para mover el hexápodo hacia atrás.
        """
        self.enviar_comando("CRAWL_BACKWARD")

    def mover_izquierda(self):
        """
        Envía el comando para girar el hexápodo hacia la izquierda.
        """
        self.enviar_comando("TURN_LEFT")

    def mover_derecha(self):
        """
        Envía el comando para girar el hexápodo hacia la derecha.
        """
        self.enviar_comando("TURN_RIGHT")

    def modo_activo(self):
        """
        Activa el modo de funcionamiento del hexápodo.
        """
        self.enviar_comando("ACTIVATE_MODE")

    def cambiar_altura(self, altura):
        """
        Cambia la altura del cuerpo del hexápodo.

        Args:
            altura (int): El valor de la altura a la que se ajustará el cuerpo.
        """
        self.enviar_comando(f"CHANGE_BODY_HEIGHT {altura}")

    def mover_cuerpo(self, x, y, z):
        """
        Mueve el cuerpo del hexápodo en las direcciones x, y, z.

        Args:
            x (int): Desplazamiento en el eje x.
            y (int): Desplazamiento en el eje y.
            z (int): Desplazamiento en el eje z.
        """
        self.enviar_comando(f"MOVE_BODY {x} {y} {z}")

    def mover_pierna(self, pierna, x, y, z):
        """
        Mueve una pierna específica del hexápodo.

        Args:
            pierna (str): La pierna a mover (ej. "F1" para la pierna delantera izquierda).
            x (int): Desplazamiento en el eje x.
            y (int): Desplazamiento en el eje y.
            z (int): Desplazamiento en el eje z.
        """
        self.enviar_comando(f"LEG_MOVE_TO_RELATIVELY {pierna} {x} {y} {z}")

    def establecer_velocidad(self, velocidad):
        """
        Establece la velocidad del robot.

        Args:
            velocidad (int): Velocidad que se quiere establecer (ej. 1, 2 o 3).
        """
        self.enviar_comando(f"SET_SPEED {velocidad}")

    def rotar_cuerpo(self):
        """
        Rota el cuerpo del hexápodo.
        """
        self.enviar_comando("ROTATE_BODY")

    def girar_izquierda(self):
        """
        Gira el robot hacia la izquierda.
        """
        self.enviar_comando("TURN_LEFT")

    def cambiar_velocidad(self, velocidad):
        """
        Cambia la velocidad de las acciones del hexápodo.

        Args:
            velocidad (int): Velocidad de la acción (un valor numérico).
        """
        self.enviar_comando(f"SET_ACTION_SPEED {velocidad}")

    def desconectar(self):
        """
        Cierra la conexión serial con el hexápodo.
        """
        if self.conexion.is_open:
            self.conexion.close()  # Cierra la conexión si está abierta
            print("Conexión cerrada.")

