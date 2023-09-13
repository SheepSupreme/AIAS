# Automatisiertes Kommissionierungssystem (AKS)


## Problemstellung:

Große Produktionsunternehmen stoßen oft auf das Problem, dass durch ihren Wachstum die Produktion immer größer und unübersichtlicher wird. Als Folge davon treten immer öfters Fehler auf, die das Unternehmen Geld kosten und die Produktion läuft nicht optimal. 


## Lösung:
Die Implementierung eines automatisierten Kommissionierungssystem ermöglicht dem Unternehmen maximale Effizienz und Platznutzung im Produktionsbereich. Die Bearbeitung von Aufträgen kann schneller erfolgen, wenn so viele Schritte wie möglich automatisiert werden können.


## Untersuchungsanliegen der individuellen Themenstellung

### Bewegungssystem
Eine Platform, die über ein Riemenband von einem Nema 17 Steppermotor getreiben wird. Um den Motor anzusteuern kommt der Steppermotordriver DRV8825 zum Einsatz. Der ermöglicht eine einfache Bedienung des Motors über den Arudino und ist fähig, zu Microsteppen. Auch im Bewegungssystem inkludiert sind die Endschalter(Limitswitches) die nur bei der Kalibrierungssequenz verwendet werden um den Bereich zu festzustellen, in dem die Platform Operieren darf.

Zuständigkeit: GREGOR Lukas

### Steuerung
Die Steuerung erfolgt über einen Rotary Encoder der gedrückt werden kann. Diese einfache Steuermethode wird verwendet, um die Anzahl der Bauteile möglichst gering zu halten. Der Rotary Encoder ist relativ intuitiv.

Zuständigkeit: GREGOR Lukas


### User Interface
Das User Interface(UI) wird auf einem 128x64 Oled Display angezeigt. Das UI soll auf einem Menü aufgebaut sein, durch das verschiedene Modi des AKS ausgewählt werden können. 

Zuständigkeit: GREGOR Lukas

### Auslesung von QR-Codes
Der QR code soll mit einem auf der Platform montiertem Scanner gescannt werden und an den Arduino zur Weiterverarbeitung geschickt werden. 

Zuständigkeit: PLEVA Philip

### Ausgabe des Paketes
Die Ausgabe des Paketes erfolgt über einen Mechanismus, der die Pakete raus aus dem Behälter auf ein dahinter liegendes Fließband schiebt. Welche Bewegungsmethode für den Mechanismus verwendet wird, ist noch nicht sicher. Mögliche Kanidaten dafür sind elektrische oder pneumatische Mechanismen.

Zuständigkeit: PLEVA Philip


### Entwicklung der Spannungsversorgung

### Systementwicklung und harmonische Zusammenführung der individuellen AKS Körper
Einzelnde Teile werden zusammengeführt und in ein funktionstüchtiges System gewandelt, dass möglichst schnell und optimiert ist.

PLEVA Philip & GREGOR Lukas