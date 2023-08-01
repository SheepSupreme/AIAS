1. `#ifndef LukiStepper_h` und `#define LukiStepper_h`: Diese Zeilen werden als Include-Guards oder Header-Guards bezeichnet. Sie verhindern, dass die Header-Datei mehr als einmal in der gleichen Übersetzungseinheit eingefügt wird, was passieren kann, wenn mehrere Dateien dieselbe Header-Datei einbinden. Wenn die Header-Datei bereits eingebunden wurde, überspringt der Präprozessor den gesamten Inhalt zwischen `#ifndef` und `#endif`, um sicherzustellen, dass der Inhalt nicht dupliziert wird. Der Name `LukiStepper_h` basiert in der Regel auf dem Namen der Bibliothek und sollte eindeutig für diese spezifische Bibliothek sein.
    
2. `#include <Arduino.h>`: Diese Zeile bindet die Datei `Arduino.h` ein, die den Zugriff auf die Standard-Arduino-Funktionen und -Definitionen ermöglicht. Es ist erforderlich, diese Header-Datei einzubinden, um Arduino-spezifische Funktionen in der Bibliothek verwenden zu können.
    
3. `#include <stdlib.h>`: Diese Zeile bindet die Header-Datei `stdlib.h` der Standard-C-Bibliothek ein, die Funktionen für allgemeine Operationen wie Speicherverwaltung und Umwandlung bereitstellt. Sie wird in der Bibliothek möglicherweise für verschiedene Zwecke verwendet.

# Classes
Werden benützt um Unterprogramme und Attribute zu sammeln. Diese werden wiederrum in public: und private: unterteilt. Das macht aus, ob der Wert auch außerhalb der Class übernommen wird oder nur innerhalb der Class eine Bedeutung spielt.
```cpp
    LukiStepper(); // Constructor declaration
    ~LukiStepper(); // Destructor declaration
```
## Datentypen die Funktionen annehmen können

**Basic Data Types**:
- `int`: Represents integers, e.g., 1, -42, 1000.
- `float` and `double`: Represent floating-point numbers with decimal places, e.g., 3.14, -0.005, 123.456.
- `char`: Represents single characters, e.g., 'A', 'z', '@'.
- `bool`: Represents a boolean value, which can be either `true` or `false`.

**Void**:
- The `void` data type is used to indicate that a function does not return a value. It's often used for functions that perform actions or operations without producing a result.

## private:
Hier werden alle Variablen mit unterschiedlichen Datentypen festgelegt. *void* ist keiner davon, da der nur bei Funktionen vorkommt.

## public: 
Hier werden alle in der Class benutzten Funktionen festgehalten. Der *void* Datentyp ist hier die Norm mit ein paar wenigen Ausßnahmen.

