int a=9;
int b=10;
int angle=0;//+ve angle is clockwise
int a_current,b_current,a_prev=0;
void setup() {
  
pinMode(a,INPUT);//not sure where pullup is required?
pinMode(b,INPUT);

}

void loop() {
  a_current=digitalRead(a);
  b_current=digitalRead(b);
  if (a_current!=a_prev)
  {
    if(a_current!=b_current) //clockwise
      angle++;
    if(a_current==b_current) //anticlockwise
      angle--;
  }
  a_prev=a_current;
}
