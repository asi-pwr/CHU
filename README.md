# CHU
Count Host Up wersja jeden zero (w skrócie CHU1.0)

## Cel aplikacji
Jest to implementacja tzw. 'ASI CZUJKI'.

Celem skryptu jest zliczenie ilości osób które aktualnie są podłaczone w ramach konkretnej podsieci.

Przykładowe wywołanie:

```
./chu_1.0.py 192.168.1 100 109 dupa.8 
```

Program ten sprawdzi, czy hosty od 100 do 109 w podsieci 192.168.1 odpowiadają na PING i zapisze wynik do pliku 'dupa.8'.
Trzy ostatnie parametry są opcjonalne. Podstawowe wartości:
* Poczatkowy host: 100
* Końcowy host: 254
* Nazwa pliku: output.txt
