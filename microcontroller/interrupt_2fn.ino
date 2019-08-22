int input;

volatile int flag;
volatile int flagg;
volatile int counter1;
volatile int counter2;

void setup()
{
  Serial.begin(2000000);
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), ISR1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(3), ISR2, CHANGE);
  flag=0;
  flagg=0;
}

void loop() 
{
  
  if(flag==1)
  {
    counter1+=1;
    flag=0;
    Serial.println("Counter1=");
    Serial.println(counter1);
  }
  if(flagg==1)
  {
    counter2+=1;
    flagg=0;
    Serial.println("Counter2=");
    Serial.println(counter2);
  }
  

}
void ISR1()
{
    flag=1; 
}
void ISR2()
{
  flagg=1;
  
}
