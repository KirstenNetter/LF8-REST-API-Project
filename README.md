# LF8-REST-API-Project

Dieses Projekt ist ein einfaches Wetterdaten-Managementsystem, das Wetterdaten von der OpenWeatherMap-API abruft und in einer SQLite-Datenbank speichert. 

## Voraussetzungen

- Python 3.x
- Abhängigkeiten: `requests`, `sqlalchemy`

## Installation

1. **Python installieren**: Stelle sicher, dass Python 3.x auf deinem System installiert ist. Du kannst Python [hier herunterladen](https://www.python.org/downloads/).

2. **Abhängigkeiten installieren**: Verwende `pip`, um die erforderlichen Python-Pakete zu installieren:

    ```bash
    pip install requests sqlalchemy
    ```

3. **API-Schlüssel erhalten**: Besorge dir einen API-Schlüssel von der OpenWeatherMap-Website. Du kannst dich [hier registrieren](https://home.openweathermap.org/users/sign_up) und einen API-Schlüssel erhalten.

4. **API-Schlüssel konfigurieren**: Ersetze den Platzhalter-API-Schlüssel in `main.py` durch deinen eigenen API-Schlüssel:

    ```python
    appid = 'Dein_API_Schlüssel'
    ```

## Verwendung

Das Programm besteht aus drei Skripten, die nacheinander ausgeführt werden müssen:

1. **Datenbank erstellen**: Führe das Skript `createDb.py` aus, um die SQLite-Datenbank zu erstellen. Dieses Skript erstellt eine Datei namens `database.db` und richtet die erforderlichen Tabellen ein.

    ```bash
    python createDb.py
    ```

2. **Wetterdaten abrufen**: Führe das Skript `transferData.py` aus, um die Wetterdaten von der OpenWeatherMap-API abzurufen und in die Datenbank zu speichern.

    ```bash
    python transferData.py
    ```

    Dieses Skript führt folgende Aktionen aus:
    - Ruft aktuelle Wetterdaten für den in `main.py` definierten Ort ab.
    - Überprüft, ob die Daten (Ort, Zeit, Wettertyp) bereits in der Datenbank vorhanden sind.
    - Fügt neue Daten zur Datenbank hinzu, falls diese noch nicht vorhanden sind.

3. **Daten abrufen und analysieren**: Die Wetterdaten sind jetzt in der SQLite-Datenbank `database.db` gespeichert. Du kannst diese Daten mit SQLAlchemy oder einem anderen SQLite-kompatiblen Tool abrufen und analysieren.

## Projektstruktur

- **`main.py`**: Dieses Skript enthält die Logik, um Wetterdaten von der OpenWeatherMap-API abzurufen.
- **`createDb.py`**: Dieses Skript erstellt die Datenbank und definiert die Tabellenstrukturen mithilfe von SQLAlchemy.
- **`transferData.py`**: Dieses Skript verbindet die beiden vorherigen Skripte und überträgt die abgerufenen Wetterdaten in die Datenbank.


