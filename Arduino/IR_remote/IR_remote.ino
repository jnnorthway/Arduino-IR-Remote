#include <Adafruit_GFX.h>   
#include <Adafruit_TFTLCD.h>
#include <TouchScreen.h>
#include <IRremote.h>
#include <Servo.h>

IRsend irsend;

#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0

#define LCD_RESET A4

#define TS_MINX 108
#define TS_MINY 81
#define TS_MAXX 908
#define TS_MAXY 918

#define YP A3
#define XM A2
#define YM 9
#define XP 8

#define BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF8C0//        0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE3
#define WHITE   0xFFFF
#define GREY    0x4C12//        0xC618

#define RED1        0xF800
#define ORANGE1     0xFCA0
#define YELLOW1     0xFFE0
#define GREEN1      0x3FE0
#define LIGHTBLUE1  0x07FD
#define BLUE1       0x00DF
#define PURPLE1     0xE99F
#define PINK1       0xF816
#define WHITE1      0xFFFF

#define TURQUOISE1  0x07FF
#define TURQUOISE2  0x04D6
#define TURQUOISE3  0x034F

#define RED2        0xFB40
#define ORANGE2     0xFEC0
#define GREEN2      0x26A0
#define LIGHTBLUE2  0x067F
#define BLUE2       0x5C1F
#define PURPLE2     0xBA1F
#define PURPLE3     0xD81F
#define PINK2       0xF818


#define MINPRESSURE 5
#define MAXPRESSURE 1000

Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 364);

void(* resetFunc) (void) = 0;

int res = 0;

void setbtn(){

  tft.setCursor(40,25);
  tft.setTextSize(3);
  tft.setTextColor(WHITE);
  tft.print("James' Remote");

  tft.fillRect(30,90,100,100,GREY);
  tft.drawRect(30,90,100,100,WHITE);
  tft.setCursor(65,120);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("LED");

  tft.fillRect(190,90,100,100,GREY);
  tft.drawRect(190,90,100,100,WHITE);
  tft.setCursor(200,120);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("Samsung");

}

void backBtn(){

    //back
    tft.fillRect(10,10,80,30,GREY);
    tft.drawRect(10,10,80,30,WHITE);
    tft.setCursor(15,18);
    tft.setTextColor(BLACK);
    tft.setTextSize(2);
    tft.print(" BACK");

}

void samBtn(){

  tft.fillRect(10,80,80,80,RED);
  tft.drawRect(10,80,80,80,WHITE);
  tft.setCursor(15,115);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("ON/OFF");

  tft.fillRect(10,200,80,30,GREY);
  tft.drawRect(10,200,80,30,WHITE);
  tft.setCursor(15,208);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("Source");

  tft.fillRect(127,10,106,70,GREY);
  tft.drawRect(127,10,106,70,WHITE);
  tft.setCursor(132,35);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print(" Vol UP");

  tft.fillRect(127,160,106,70,GREY);
  tft.drawRect(127,160,106,70,WHITE);
  tft.setCursor(132,185);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("Vol DOWN");

  tft.fillRect(150,107,60,30,GREY);
  tft.drawRect(150,107,60,30,WHITE);
  tft.setCursor(155,113);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("MUTE");

  tft.fillRect(270,70,40,40,GREY);
  tft.drawRect(270,70,40,40,WHITE);
  tft.setCursor(280,77);
  tft.setTextColor(BLACK);
  tft.setTextSize(4);
  tft.print("+");

  tft.fillRect(270,130,40,40,GREY);
  tft.drawRect(270,130,40,40,WHITE);
  tft.setCursor(280,137);
  tft.setTextColor(BLACK);
  tft.setTextSize(4);
  tft.print("-");

}

void ledBtn(){

  tft.fillRect(10,50,80,80,RED);
  tft.drawRect(10,50,80,80,WHITE);
  tft.setCursor(15,85);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("ON/OFF");

  tft.fillRect(20,140,60,40,GREY);
  tft.drawRect(20,140,60,40,WHITE);
  tft.setCursor(20,155);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("  +");

  tft.fillRect(20,190,60,40,GREY);
  tft.drawRect(20,190,60,40,WHITE);
  tft.setCursor(20,205);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("  -");

  tft.fillRect(110,90,85,85,YELLOW);
  tft.drawRect(110,90,85,85,WHITE);
  tft.setCursor(115,125);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print(" MODS");

  //tft.fillRect(215,90,85,85,GREY);
  tft.fillRect(215,90,28,28,RED1);
  tft.fillRect(243,90,29,28,ORANGE1);
  tft.fillRect(272,90,28,28,YELLOW1);
  tft.fillRect(215,118,28,29,GREEN1);
  tft.fillRect(243,118,29,29,TURQUOISE1);
  tft.fillRect(272,118,28,29,BLUE1);
  tft.fillRect(215,147,28,28,PURPLE1);
  tft.fillRect(243,147,29,28,PINK1);
  tft.fillRect(272,147,28,28,WHITE1);
  tft.drawRect(215,90,85,85,WHITE1);
  tft.setCursor(220,125);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("COLOUR");
}

void funcBtn(){

  tft.fillRect(0,80,80,80,RED);
  tft.drawRect(0,80,80,80,WHITE);
  tft.setCursor(5,115);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print("ON/OFF");

  tft.fillRect(0,160,80,80,GREY);
  tft.drawRect(0,160,80,80,WHITE);
  tft.setCursor(10,195);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("FLASH");

  tft.fillRect(80,80,80,80,GREY);
  tft.drawRect(80,80,80,80,WHITE);
  tft.setCursor(90,115);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("FADE1");

  tft.fillRect(80,160,80,80,GREY);
  tft.drawRect(80,160,80,80,WHITE);
  tft.setCursor(90,195);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("FADE2");

  tft.fillRect(160,80,80,80,GREY);
  tft.drawRect(160,80,80,80,WHITE);
  tft.setCursor(170,115);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("JUMP1");

  tft.fillRect(160,160,80,80,GREY);
  tft.drawRect(160,160,80,80,WHITE);
  tft.setCursor(170,195);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("JUMP2");

  tft.fillRect(240,80,80,80,GREY);
  tft.drawRect(240,80,80,80,WHITE);
  tft.setCursor(250,115);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("QUICK");

  tft.fillRect(240,160,80,80,GREY);
  tft.drawRect(240,160,80,80,WHITE);
  tft.setCursor(255,195);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);
  tft.print("SLOW");

}

void colourBtn(){

  tft.fillRect(0,102,46,46,RED);
  tft.drawRect(0,102,46,46,WHITE);
  tft.setCursor(6,123);
  tft.setTextColor(BLACK);
  tft.setTextSize(1);
  tft.print("ON/OFF");

  tft.fillRect(0,148,46,46,RED1);
  tft.drawRect(0,148,46,46,WHITE);

  tft.fillRect(0,194,46,46,RED2);
  tft.drawRect(0,194,46,46,WHITE);

  tft.fillRect(46,102,45,46,ORANGE1);
  tft.drawRect(46,102,45,46,WHITE);

  tft.fillRect(46,148,45,46,ORANGE2);
  tft.drawRect(46,148,45,46,WHITE);

  tft.fillRect(46,194,45,46,YELLOW1);
  tft.drawRect(46,194,45,46,WHITE);

  tft.fillRect(91,102,46,46,GREEN1);
  tft.drawRect(91,102,46,46,WHITE);

  tft.fillRect(91,148,46,46,GREEN2);
  tft.drawRect(91,148,46,46,WHITE);

  tft.fillRect(91,194,46,46,TURQUOISE1);
  tft.drawRect(91,194,46,46,WHITE);

  tft.fillRect(137,102,46,46,TURQUOISE2);
  tft.drawRect(137,102,46,46,WHITE);

  tft.fillRect(137,148,46,46,TURQUOISE3);
  tft.drawRect(137,148,46,46,WHITE);

  tft.fillRect(137,194,46,46,BLUE1);
  tft.drawRect(137,194,46,46,WHITE);

  tft.fillRect(183,102,46,46,BLUE2);
  tft.drawRect(183,102,46,46,WHITE);

  tft.fillRect(183,148,46,46,PURPLE1);
  tft.drawRect(183,148,46,46,WHITE);

  tft.fillRect(183,194,46,46,PURPLE2);
  tft.drawRect(183,194,46,46,WHITE);

  tft.fillRect(229,102,45,46,PURPLE3);
  tft.drawRect(229,102,45,46,WHITE);

  tft.fillRect(229,148,45,46,WHITE1);
  tft.drawRect(229,148,45,46,WHITE);

  tft.fillRect(229,194,45,46,PINK1);
  tft.drawRect(229,194,45,46,WHITE);

  tft.fillRect(274,102,46,46,PINK2);
  tft.drawRect(274,102,46,46,WHITE);

  tft.fillRect(274,148,46,46,LIGHTBLUE1);
  tft.drawRect(274,148,46,46,WHITE);

  tft.fillRect(274,194,46,46,LIGHTBLUE2);
  tft.drawRect(274,194,46,46,WHITE);



}

void coords(TSPoint p){
    Serial.print("("); Serial.print(p.x);
    Serial.print(", "); Serial.print(p.y);
    Serial.println(")");
}

void mainmenu(){

    if(res >= 20){

      tft.fillScreen(WHITE);
      tft.setCursor(40,110);
      tft.setTextColor(BLACK);
      tft.setTextSize(3);
      tft.print("One Moment");
      delay(500);
      tft.print(".");
      delay(500);
      tft.print(".");
      delay(500);
      tft.print(".");
      delay(1000);
      resetFunc();
    }
    Serial.println("main");


    bool m = true; //in menu

    while(m == true){


      digitalWrite(13, HIGH);
      TSPoint p = ts.getPoint();
      digitalWrite(13, LOW);

      pinMode(XM, OUTPUT);
      pinMode(YP, OUTPUT);

      if(p.z > MINPRESSURE ){

        p.x = map(p.x, TS_MAXX, TS_MINX, tft.width(), 0);
        p.y = map(p.y, TS_MAXY, TS_MINY, tft.height(), 0);

        coords(p);

        if(p.y>20 && p.y<100 && p.x>120 && p.x<260){
          m = false;
          LED();
        }
        if(p.y>140 && p.y<220 && p.x>120 && p.x<260){
          m = false;
          SAM();
        }
        tft.fillScreen(BLACK);
        setbtn();


      }
    }
}

void LED(){
  Serial.println("LED");
  bool l = true;
  tft.fillScreen(BLACK);
  backBtn();
  ledBtn();
  while(l){
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if(p.z > MINPRESSURE ){

      p.x = map(p.x, TS_MAXX, TS_MINX, tft.width(), 0);
      p.y = map(p.y, TS_MAXY, TS_MINY, tft.height(), 0);

      coords(p);

      if(p.y>20 && p.y<60 && p.x>10 && p.x<70){
        Serial.println("Back");
        //l = false;
        res++;
        mainmenu();
      }
      if(p.y>10 && p.y<70 && p.x>70 && p.x<180){
        Serial.println("ON/OFF");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF02FD, 24);
          delay(40);
        }
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFFFFFF, 24);
          delay(40);
        }

      }
      if(p.y>15 && p.y<60 && p.x>195 && p.x<250){
        Serial.println("Brightness UP");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF3AC5, 24);
          delay(40);
        }
      }
      if(p.y>15 && p.y<60 && p.x>260 && p.x<315){
        Serial.println("Brightness DOWN");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFFBA45, 24);
          delay(40);
        }
      }
      if(p.y>80 && p.y<145 && p.x>125 && p.x<245){
        Serial.println("FUNCTION");
        FUNCTION();
      }

      if(p.y>160 && p.y<225 && p.x>125 && p.x<245){
        Serial.println("COLOUR");
        COLOUR();
      }
    }
  }
}

void FUNCTION(){

  bool F = true;
  tft.fillScreen(BLACK);
  backBtn();
  funcBtn();
  while(F){
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if(p.z > MINPRESSURE ){

      p.x = map(p.x, TS_MAXX, TS_MINX, tft.width(), 0);
      p.y = map(p.y, TS_MAXY, TS_MINY, tft.height(), 0);

      coords(p);

      if(p.y>20 && p.y<60 && p.x>10 && p.x<70){
        Serial.println("Back");
        //F = false;
        res++;
        LED();
      }
      if(p.y>10 && p.y<70 && p.x>70 && p.x<180){
        Serial.println("ON/OFF");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF02FD, 24);
          delay(40);
        }
      }
      if(p.y>15 && p.y<60 && p.x>195 && p.x<250){
        Serial.println("Brightness UP");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF3AC5, 24);
          delay(40);
        }
      }
      if(p.y>15 && p.y<60 && p.x>260 && p.x<315){
        Serial.println("Brightness DOWN");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFFBA45, 24);
          delay(40);
        }
      }
    }
  }
}

void COLOUR(){
  bool C = true;
  tft.fillScreen(BLACK);
  backBtn();
  colourBtn();
  while(C){
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if(p.z > MINPRESSURE ){

      p.x = map(p.x, TS_MAXX, TS_MINX, tft.width(), 0);
      p.y = map(p.y, TS_MAXY, TS_MINY, tft.height(), 0);

      coords(p);

      if(p.y>20 && p.y<60 && p.x>10 && p.x<70){
        Serial.println("Back");
        //C = false;
        res++;
        LED();
      }
      if(p.y>0 && p.y<35 && p.x>140 && p.x<200){
        Serial.println("ON/OFF");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF02FD, 24);
          delay(40);
        }
      }
      if(p.y>0 && p.y<35 && p.x>201 && p.x<260){
        Serial.println("red-1");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFF3AC5, 24);
          delay(40);
        }
      }
      if(p.y>0 && p.y<35 && p.x>261 && p.x<320){
        Serial.println("red-2");
        for (int i = 0; i < 3; i++) {
          irsend.sendNEC(0xFFBA45, 24);
          delay(40);
        }
      }
    }
  }
}

void SAM(){
  Serial.println("SAMSUNG");

          bool s = true;
          tft.fillScreen(BLACK);
          backBtn();
          samBtn();
          while(s){
            digitalWrite(13, HIGH);
            TSPoint p = ts.getPoint();
            digitalWrite(13, LOW);

            pinMode(XM, OUTPUT);
            pinMode(YP, OUTPUT);
            if(p.z > MINPRESSURE ){

              p.x = map(p.x, TS_MAXX, TS_MINX, tft.width(), 0);
              p.y = map(p.y, TS_MAXY, TS_MINY, tft.height(), 0);
              coords(p);
              if(p.y>20 && p.y<60 && p.x>10 && p.x<70){
                Serial.println("Back");
                //s = false;
                res++;
                mainmenu();
              }
              if(p.y>10 && p.y<70 && p.x>110 && p.x<220){
                Serial.println("ON/OFF");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CA807F, 32);
                  delay(40);
                }
              }
              if(p.y>10 && p.y<70 && p.x>270 && p.x<310){
                Serial.println("SOURCE");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CA8877, 32);
                  delay(40);
                }
              }
              if(p.y>100 && p.y<175 && p.x>10 && p.x<110){
                Serial.println("Volume UP");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CACC33, 32);
                  delay(40);
                }
              }
              if(p.y>110 && p.y<160 && p.x>150 && p.x<190){
                Serial.println("MUTE");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CA9C63, 32);
                  delay(40);
                }
              }
              if(p.y>100 && p.y<175 && p.x>220 && p.x<310){
                Serial.println("Volume DOWN");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CADC23, 32);
                  delay(40);
                }
              }
              if(p.y>205 && p.y<235 && p.x>100 && p.x<150){
                Serial.println("Tune UP");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CAC43B, 32);
                  delay(40);
                }
              }
              if(p.y>205 && p.y<235 && p.x>180 && p.x<230){
                Serial.println("Tune DOWN");
                for (int i = 0; i < 3; i++) {
                  irsend.sendSAMSUNG(0xC2CAD42B, 32);
                  delay(40);
                }
              }
            }
          }
}
void setup(void) {

  Serial.begin(9600);
  Serial.println(F("TFT LCD test"));

#ifdef USE_ADAFRUIT_SHIELD_PINOUT
  Serial.println(F("Using Adafruit 2.4\" TFT Arduino Shield Pinout"));
#else
  Serial.println(F("Using Adafruit 2.4\" TFT Breakout Board Pinout"));
#endif
  tft.setRotation(3);
  Serial.print("TFT size is "); Serial.print(tft.width()); Serial.print("x"); Serial.println(tft.height());

  tft.reset();

  uint16_t identifier = tft.readID();
   if(identifier == 0x9325) {
    Serial.println(F("Found ILI9325 LCD driver"));
  } else if(identifier == 0x9328) {
    Serial.println(F("Found ILI9328 LCD driver"));
  } else if(identifier == 0x4535) {
    Serial.println(F("Found LGDP4535 LCD driver"));
  }else if(identifier == 0x7575) {
    Serial.println(F("Found HX8347G LCD driver"));
  } else if(identifier == 0x9341) {
    Serial.println(F("Found ILI9341 LCD driver"));
  } else if(identifier == 0x8357) {
    Serial.println(F("Found HX8357D LCD driver"));
  } else if(identifier==0x0101)
  {
      identifier=0x9341;
       Serial.println(F("Found 0x9341 LCD driver"));
  }else {
    Serial.print(F("Unknown LCD driver chip: "));
    Serial.println(identifier, HEX);
    Serial.println(F("If using the Adafruit 2.8\" TFT Arduino shield, the line:"));
    Serial.println(F("  #define USE_ADAFRUIT_SHIELD_PINOUT"));
    Serial.println(F("should appear in the library header (Adafruit_TFT.h)."));
    Serial.println(F("If using the breakout board, it should NOT be #defined!"));
    Serial.println(F("Also if using the breakout, double-check that all wiring"));
    Serial.println(F("matches the tutorial."));
    identifier=0x9341;

  }

  tft.begin(identifier);
  tft.setRotation(3);
  tft.fillScreen(BLACK);

  setbtn();

}


void loop() {

  unsigned long start = micros();

  digitalWrite(13, HIGH);
  TSPoint p = ts.getPoint();
  digitalWrite(13, LOW);
  pinMode(XM, OUTPUT);
  pinMode(YP, OUTPUT);

  mainmenu();


  }
