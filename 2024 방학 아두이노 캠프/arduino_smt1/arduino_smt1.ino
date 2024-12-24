#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define BT_RXD 13
#define BT_TXD 12

SoftwareSerial bluetooth(BT_RXD, BT_TXD);

DHT dht(5, DHT11);

LiquidCrystal_I2C lcd(0x27, 16, 2);

SoftwareSerial mySerial(7,6); // Arudino Uno port RX, TX

void setup() {
  // for debuging 
  Serial.begin(115200);  
  bluetooth.begin(115200);
  dht.begin();
  pinMode(A0, INPUT);
  lcd.init();
  lcd.backlight();
  delay(2000);
  lcd.noBacklight();
  // Use software serial
  mySerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  static int CheckFirst=0;
  static int pm_add[3][5]={0,};
  static int pm_old[3]={0,};
  int chksum=0,res=0;;
  int val;
  unsigned char pms[32]={0,};

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float hic = dht.computeHeatIndex(t, h, false);

  if(bluetooth.available())
  {
    Serial.write(bluetooth.read());
  }
  if(Serial.available())
  {
    bluetooth.write(Serial.read());
  }
  
  if(mySerial.available()>=32){

    for(int j=0; j<32 ; j++){
      pms[j]=mySerial.read();
      if(j<30)
        chksum+=pms[j];
    }

    if(pms[30] != (unsigned char)(chksum>>8) 
        || pms[31]!= (unsigned char)(chksum) ){

      return res;
    }
    if(pms[0]!=0x42 || pms[1]!=0x4d )
      return res;

  Serial.print("Dust raw data debugging :  ");
  Serial.print("1.0ug/m3:");
  Serial.print(pms[10]);
  Serial.print(pms[11]);
  Serial.print("  ");
  Serial.print("2.5ug/m3:");
  Serial.print(pms[12]);
  Serial.print(pms[13]);
  Serial.print("  ");
  Serial.print("2.5ug/m3:");
  Serial.print(pms[14]);
  Serial.println(pms[15]);
  } 

  Serial.print("온도:");
  Serial.print(t);
  Serial.print(" 습도:");
  Serial.print(h);
  Serial.print(" 체감온도:");
  Serial.print(hic);

  val = analogRead(0) * 0.0976;
  Serial.println(val);
  delay(1000);
}
