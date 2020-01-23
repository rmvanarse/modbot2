//Author: Aditya Bidwai
//Date: 23/01/2020
//This is the sample code for interrupts. It counts the twice the number of pulses passed to the interrupt pins
//Board: Arduino UNO


#define outputA1 2
#define outputB1 3
volatile long counter1=0;
volatile long counter2=0;


void count1() //ISR: Interrupt Service Routine
{
  counter1++;
  Serial.println("Ëncoder1: ");
  Serial.println(counter1);
}
void count2() //ISR: Interrupt Service Routine
{
  counter2++;
  Serial.println("Ëncoder2: ");
  Serial.println(counter2);
}

void setup() {

  attachInterrupt(digitalPinToInterrupt(outputA1), count1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(outputB1), count2, CHANGE);
  Serial.begin (2000000);
}

void loop() {
  
}
