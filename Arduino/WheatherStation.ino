#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <SD.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#include <dht11.h>
#define DHT11PIN 4

dht11 DHT11;
File txtfile;

void setup()
{
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  Serial.println("Initialising SD-Card");

  if (!SD.begin(5))
  {
    Serial.println("Initialising failed");
    return;
  }

  txtfile = SD.open("data.txt", FILE_WRITE);
  if (!txtfile)
  {
    Serial.println("Error when opening tcxt file");
    return;
  }

  Serial.println("Initialising finished");
}

void loop()
{
  int chk = DHT11.read(DHT11PIN);

  Serial.print("Humidity (%): ");
  Serial.println((float)DHT11.humidity, 2);
  lcd.setCursor(0, 0);
  lcd.print("Humidity: ");
  lcd.setCursor(10, 0);
  lcd.print((float)DHT11.humidity, 2);

  if (txtfile)
  {
    txtfile.print(millis());
    txtfile.print(" | Humidity: ");
    txtfile.println((float)DHT11.humidity, 2);
    txtfile.print("Temperature: ");
    txtfile.println((float)DHT11.temperature, 2);
    txtfile.flush();

    Serial.println("Data written successfully");
  }
  else
  {
    Serial.println("Error opening file");
  }

  Serial.print("Temperature  (C): ");
  Serial.println((float)DHT11.temperature, 2);
  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.setCursor(6, 1);
  lcd.print((float)DHT11.temperature, 2);

  delay(2000);
}
