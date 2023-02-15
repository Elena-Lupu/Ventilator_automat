# Ventilator_automat

Ventilator cu element de încălzire care poate atât să recircule auerul, cât să-l și încălzească. Își modifică modul de funcționare automat pe baza senzorului de temperatură.

În acest repository ar trebui să se regăsească codul Python pentru microcontroller RaspberryPi Pico și schema electrică a proiectului.

Mod de funcționare:
- Pe ecranul LCD sunt afișate temperatura curentă și pragul setat de utilizator;
- Cu ajutorul butoanelor, utilizatorul poate modifica pragul;
- În timpul funcționării, dacă temperatura:

-- scade sub pragul setat, se pornește alimentarea pentru elementul de încălzire;
-- ajunge la nivelul pragului setat, se oprește atât alimentarea elementului de încălzire cât și a motorului ventilatorului;
-- crește peste pragul setat, se oprește alimentarea elementului de încălzire și se pornește alimentarea motorului ventilatorului.
