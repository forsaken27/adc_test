/***************************************************/
/*             SIMPLE CODE TO TEST ADC             */
/***************************************************/

/* Just reading A0 pin and print it to the Serial continuously */

void setup() {
  SerialUSB.begin(1000000);
  // make ADC receive 9 bit input (0 - 512)
  analogReadResolution(9);

  //Serial.println("Starting the process ...");
}



void loop() {
  int v_0 = analogRead(A0);
  int v_1 = analogRead(A1);
  int v_2 = analogRead(A2);
  int v_3 = analogRead(A3);
  int v_4 = analogRead(A4);
  int v_5 = analogRead(A5);
  int v_6 = analogRead(A6);
  int v_7 = analogRead(A7);
  int v_8 = analogRead(A8);
  int v_9 = analogRead(A9);
  int v_10 = analogRead(A10);
  int v_11 = analogRead(A11);

  SerialUSB.print(v_0);
  SerialUSB.print(" ");
  SerialUSB.print(v_1);
  SerialUSB.print(" ");
  SerialUSB.print(v_2);
  SerialUSB.print(" ");
  SerialUSB.print(v_3);
  SerialUSB.print(" ");
  SerialUSB.print(v_4);
  SerialUSB.print(" ");
  SerialUSB.print(v_5);
  SerialUSB.print(" ");
  SerialUSB.print(v_6);
  SerialUSB.print(" ");
  SerialUSB.print(v_7);
  SerialUSB.print(" ");
  SerialUSB.print(v_8);
  SerialUSB.print(" ");
  SerialUSB.print(v_9);
  SerialUSB.print(" ");
  SerialUSB.print(v_10);
  SerialUSB.print(" ");
  SerialUSB.println(v_11);
}
