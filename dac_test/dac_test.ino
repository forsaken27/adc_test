/***************************************************/
/*             SIMPLE CODE TO TEST ADC             */
/***************************************************/

/* Just reading A0 pin and print it to the Serial continuously */

void setup() {
  Serial.begin(9600);
  // make ADC receive 12 bit input
  analogReadResolution(12);

  Serial.println("Starting the process ...");
}



void loop() {
  int value = analogRead(A0);
  Serial.println((value/4095.0)*3.3);
  delay(10);                           /* delay time between two reads*/
}
