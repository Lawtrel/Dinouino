int Pino = A0;    //Sensor LDR vai no Pino A0
int LDRvalor = 0;  // variavel que vai amazerna o valor do ldr
int Valor = 45; //margem de error
void setup() {
  Serial.begin(9600);
}

void loop() {
  Valor = analogRead(LDRvalor); //Ler Sensor
  if(LDRvalor <= Valor){   //Condição de detectar objetos
    Serial.println(1);
  }
  delay(40);
}
