# Automatisiertes Kommissionierungssystem (AKS)


## Problemstellung:

Große Produktionsunternehmen stoßen oft auf das Problem, dass durch ihren Wachstum die Produktion immer größer und unübersichtlicher wird. Als Folge davon treten immer öfters Fehler auf, die das Unternehmen Geld kosten und die Produktion läuft nicht optimal. 


## Lösung:
Die Implementierung eines automatisierten Kommissionierungssystem ermöglicht dem Unternehmen maximale Effizienz und Platznutzung im Produktionsbereich. Die Bearbeitung von Aufträgen kann schneller erfolgen, wenn so viele Schritte wie möglich automatisiert werden können.


## Untersuchungsanliegen der individuellen Themenstellung

### Bewegungssystem
Eine Platform, die über ein Riemenband von einem Nema 17 Steppermotor getreiben wird. Um den Motor anzusteuern kommt der Steppermotordriver DRV8825 zum Einsatz. Der ermöglicht eine einfache Bedienung des Motors über den Arudino und ist fähig, zu Microsteppen. Auch im Bewegungssystem inkludiert sind die Endschalter(Limitswitches) die nur bei der Kalibrierungssequenz verwendet werden um den Bereich zu festzustellen, in dem die Platform Operieren darf.

### Steuerung
Die Steuerung erfolgt über einen Rotary Encoder der gedrückt werden kann. Diese einfache Steuermethode wurde gewählt, weil die Anzahl der Bauteile so möglichst gering ist und der Rotary Encoder relativ intuitiv ist.


### User Interface

### Auslesung von QR-Codes

### Ausgabe des Pakets

### Systementwicklung und harmonische Zusammenführung der individuellen AKS Körper
