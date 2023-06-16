#include <ezButton.h>
#include <AccelStepper.h>
#include <SPI.h>
#include <SD.h>

AccelStepper q1 = AccelStepper(1, 2, 5); //(1, q1.STEP, q1.DIR)
AccelStepper q2 = AccelStepper(1, 3, 6);//(1, q2.STEP, q2.DIR)
AccelStepper q3 = AccelStepper(1, 4, 7);//(1, q3.STEP, q3.DIR) 
ezButton s1(A0); //q1 Limit switch.
ezButton s2(A1); //q2 Limit switch.
ezButton s3(A2); //q3 Limit switch.
File sd;

// Arduino UNO: PIN-> 12(MISO), 11(MOSI), 10(SS) and 13(SCK). 
// Arduino MEGA: PIN-> 50(MISO), 51(MOSI), 53(SS) and 52(SCK). 

// --------------------------------------------------------
bool f1 = false, f2 = false, f3 = false, f4 = false;
bool f5 = false, f6 = false, f7 = false;
double P[6];

// ---------------------------------------------------------
void setup() {
  pinMode(8, OUTPUT); //Enable q3.
  pinMode(9, OUTPUT); //Disable q1 and q2.
  Serial.begin(9600);
  if (!SD.begin()) //Pin 10 SD (Slave Select).
  {
    Serial.println("Initialization Failed");
  }
}

void loop() {
  Home();
  Data();
}

void Home() {
  if (!f4 && !f5) {
    digitalWrite(8, HIGH); //Disable q3.
    digitalWrite(9, LOW); //Enable q1 and q2.
    q1.setMaxSpeed(8000);
    q1.moveTo(0x7FFFFFFF); //0x7FFFFFFF maximum of position we can set (long type).
    q1.setSpeed(2000);
    q2.setMaxSpeed(8000);
    q2.moveTo(-0x7FFFFFFF);
    q2.setSpeed(-2000);
    q3.setMaxSpeed(8000);
    q3.moveTo(0x7FFFFFFF);
    q3.setSpeed(1000);
    f5 = !f5;
  }

  while (!f4) {
    //q1 home position.
    if (!f1) {
      s1.loop();
      if (s1.isReleased()) {
        q1.setCurrentPosition(0); // set position.
        q1.moveTo(-5500);
        q1.setSpeed(-2000);
      }
      if (q1.distanceToGo() == 0) {
        q1.setCurrentPosition(0); // set position.
        q1.disableOutputs();
        f1 = !f1;
      }
    }

    //q2 home position.
    if (!f2) {
      s2.loop();
      if (s2.isReleased()) {
        q2.setCurrentPosition(0); // set position.
        q2.moveTo(2000); //3000
        q2.setSpeed(1000);
      }
      if (q2.distanceToGo() == 0) {
        q2.setCurrentPosition(0); // set position.
        q2.disableOutputs();
        f2 = !f2;
      }
    }

    //q3 home position.
    if (!f3) {
      s3.loop();
      if (s3.isReleased()) {
        q3.setCurrentPosition(0); // set position.
        q3.moveTo(-900);
        q3.setSpeed(-1500);
      }
      if (q3.distanceToGo() == 0) {
        q3.setCurrentPosition(0); // set position.
        q3.disableOutputs();
        f3 = !f3;
      }
    }

    q1.runSpeed();
    q2.runSpeed();

    if (f1 && f2) {
      digitalWrite(8, LOW);
      q3.runSpeed();
    }

    if (f1 && f2 && f3 && !f4) {
      f1 = !f1;
      f2 = !f2;
      f3 = !f3;
      f4 = !f4;
      f5 = !f5;
    }
  }
}

void Data() {
  while (!f7) {
    if (q1.distanceToGo() == 0 && q2.distanceToGo() == 0 && q3.distanceToGo() == 0) {
      SDlookup();
      q1.moveTo(P[0]);
      q1.setSpeed(P[3]);
      q2.moveTo(P[1]);
      q2.setSpeed(P[4]);
      q3.moveTo(-P[2]);
      q3.setSpeed(-P[5]);
    }

    if (q1.distanceToGo() == 0 && (q2.distanceToGo() != 0 || q3.distanceToGo() != 0)) {
      q1.setSpeed(0);
      q1.disableOutputs();
    }

    if (q2.distanceToGo() == 0 && (q1.distanceToGo() != 0 || q3.distanceToGo() != 0)) {
      q2.setSpeed(0);
      q2.disableOutputs();
    }

    if (q3.distanceToGo() == 0 && (q1.distanceToGo() != 0 || q2.distanceToGo() != 0)) {
      q3.setSpeed(0);
      q3.disableOutputs();
    }

    q1.runSpeed();
    q2.runSpeed();
    q3.runSpeed();
  }
}

void SDlookup() {
  if (Serial.available()) {
        int valueFromPython = Serial.parseInt();
        if (valueFromPython == 0) {
        if (!f6) {
        sd = SD.open("piedra.txt", FILE_READ);
        f6 = !f6;
      }
    }
     if (valueFromPython == 1) {
        if (!f6) {
        sd = SD.open("Papel.txt", FILE_READ);
        f6 = !f6;
        }
     }

     if (valueFromPython == 2) {
        if (!f6) {
        sd = SD.open("Tijera.txt", FILE_READ);
        f6 = !f6;
        }
     }
  }



  
  if (sd) {
    if (sd.available() <= 5) {
      sd.close();
      f6 = !f6;
      f7 = !f7;
      f4 = !f4;
    } else {
          for (int i = 0; i < 6; i++) {
            P[i] = sd.readStringUntil(' ').toDouble();
          }
        }
      }
    }
