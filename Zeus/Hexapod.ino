#ifndef ARDUINO_AVR_MEGA2560
#error "Por favor selecciona 'Arduino/Genuino Mega o Mega 2560' como placa."
#endif

#include <FNHR.h>  // Librería del robot

FNHR robot;  // Crear una instancia del robot

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial a 9600 baudios
  robot.Initialize();   // Inicializa el robot
  Serial.println("Robot activado. A la espera de instrucciones...");
}

void loop() {
  if (Serial.available() > 0) {
    String inputCommand = Serial.readStringUntil('\n');  // Lee el comando que se envía desde la computadora
    inputCommand.trim();  // Elimina espacios innecesarios
    Serial.print("Comando recibido: ");
    Serial.println(inputCommand);
    procesarComando(inputCommand);  // Llama a la función para procesar el comando
  }
}

void procesarComando(String inputCommand) {
  if (inputCommand == "AVANZAR") {
    Serial.println("Ejecutando movimiento hacia adelante...");
    robot.CrawlForward();  // Hace que el robot avance
  } else if (inputCommand == "RETROCEDER") {
    Serial.println("Ejecutando movimiento hacia atrás...");
    robot.CrawlBackward();  // Hace que el robot retroceda
  } else if (inputCommand == "GIRO_IZQUIERDO") {
    Serial.println("Ejecutando giro a la izquierda...");
    robot.TurnLeft();  // Hace que el robot gire a la izquierda
  } else if (inputCommand == "GIRO_DERECHO") {
    Serial.println("Ejecutando giro a la derecha...");
    robot.TurnRight();  // Hace que el robot gire a la derecha
  } else if (inputCommand == "BAILAR") {
    Serial.println("Ejecutando baile...");
    bailar();  // Llama a la función que hará que el robot baile
  } else {
    Serial.println("Comando no reconocido.");
  }
}

void bailar() {
  for (int i = 0; i < 3; i++) {  // Realiza 3 ciclos de baile
    robot.CrawlForward();  // Avanza
    delay(500);  // Espera 500ms
    robot.TurnRight();  // Gira a la derecha
    delay(500);  // Espera 500ms
    robot.CrawlBackward();  // Retrocede
    delay(500);  // Espera 500ms
    robot.TurnLeft();  // Gira a la izquierda
    delay(500);  // Espera 500ms
  }
  Serial.println("Baile terminado.");
}
