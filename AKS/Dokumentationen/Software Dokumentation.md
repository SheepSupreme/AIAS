
# Maximale Geschwindigkeit

![[Pasted image 20230731194207.png]]
Die schnellste mögliche Geschwindigkeit ohne Modifikationen and der SpeedyStepper library zu unternehmen, ist mit dem Befehl 
```
speedy.setSpeedInStepsPerSecond(speed);
```
und der Geschwindigkeit *speed* auf circa 16000 steps/s
Umgerechnet sind das circa $$ \frac {16000} {800} * 60 = 1200rpm $$
Laut dem Author der library ist für den Quarterstep-Betrieb eine Maximalgeschwindigkeit von 937 RPM möglich. Das Limit bei der Ausführung des Codes und den Spezifikationen des Arduinos liegt allerdings bei circa 1200 RPM. 
Dieses Limit kann hoffentlich durch Optimierung des Codes erhöht werden.

Die Beschleunigung auf diese Geschwindigkeit erfolgt ohne weiteren Problemen mit $$ 250000 steps/s^2 $$
## Dauer eines Programms messen
Mit der `millis();` Funktion kann mit folgendem Code die Dauer des Programmes gemessen werden. 
```cpp
unsigned long startTime = millis(); //1. Messung
//Programm
unsigned long endTime = millis(); // 2. Messung
unsigned long executionTime = endTime - startTime; // Berechnung
```
