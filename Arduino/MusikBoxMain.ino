#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C Lcd(0x27,16,2);
//Declaring all variables we need
int s=1;
int r=1;
int t=1;
const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 391;
const int gS = 415;
const int a = 440;
const int aS = 455;
const int b = 466;
const int cH = 523;
const int cSH = 554;
const int dH = 587;
const int dSH = 622;
const int eH = 659;
const int fH = 698;
const int fSH = 740;
const int gH = 784;
const int gSH = 830;
const int aH = 880;
const int buzzerPin = 10;
const int ledPin1 = 2;
const int ledPin2 = 3; 

int counter = 0;



void setup() {
  Lcd.init();
  Lcd.setBacklight(HIGH);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);

}
void setuplcd(){
  Lcd.clear();
  Lcd.setCursor(1,0);
  Lcd.print("Currently playing:");
  Lcd.setCursor(1,1);
}

void beep(int note, int duration)
{
  tone(buzzerPin, note, duration);
  if(counter % 2 == 0)
  {
    digitalWrite(ledPin1, HIGH);
    delay(duration);
    digitalWrite(ledPin1, LOW);
  }else
  {
    digitalWrite(ledPin2, HIGH);
    delay(duration);
    digitalWrite(ledPin2, LOW);
  }
  noTone(buzzerPin);

  delay(50);
  counter++;
}
void firstSection()
{
  beep(a, 500);
  beep(a, 500);    
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);  
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);

  delay(500);

  beep(eH, 500);
  beep(eH, 500);
  beep(eH, 500);  
  beep(fH, 350);
  beep(cH, 150);
  beep(gS, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);

  delay(500);
}

void secondSection()
{
  beep(aH, 500);
  beep(a, 300);
  beep(a, 150);
  beep(aH, 500);
  beep(gSH, 325);
  beep(gH, 175);
  beep(fSH, 125);
  beep(fH, 125);    
  beep(fSH, 250);

  delay(325);

  beep(aS, 250);
  beep(dSH, 500);
  beep(dH, 325);  
  beep(cSH, 175);  
  beep(cH, 125);  
  beep(b, 125);  
  beep(cH, 250);  

  delay(350);
}
void starwars(){
  setuplcd();
  Lcd.print("Imperial March");
  {
  firstSection();
  secondSection();
  //Variant 1
  beep(f, 250);  
  beep(gS, 500);  
  beep(f, 350);  
  beep(a, 125);
  beep(cH, 500);
  beep(a, 375);  
  beep(cH, 125);
  beep(eH, 650);
  delay(500);
  secondSection();
  //Variant 2
  beep(f, 250);  
  beep(gS, 500);  
  beep(f, 375);  
  beep(cH, 125);
  beep(a, 500);  
  beep(f, 375);  
  beep(cH, 125);
  beep(a, 650);  
  delay(650);
}

void rickroll(){
  setuplcd();
  Lcd.print("Never gonna give you up");
}

void tetris(){
  setuplcd();
  Lcd.print("Tetris");
}

void loop(){
  Lcd.setCursor(6,0);
  Lcd.print("MusikBox");
  Lcd.setCursor(1,1);
  Lcd.print("Choose one of 3:");
  Lcd.setCursor(1,2);
  Lcd.print("1.Star2.Never3.Tetris");
  int starwsbtn = digitalRead(7);
  int rickbtn = digitalRead(8);
  int tetrisbtn = digitalRead(9);
  if(starwsbtn == HIGH){
    starwars();
    }
  if(rickbtn == HIGH){
    rickroll();
    }
  if(tetrisbtn == HIGH){
    tetris();
    }
  }
 
