# mms-zavrsni
<img src="https://raw.github.com/SlavicPixel/mms-zavrsni/master/static/green_panda_nav.svg" alt="img" width="75%">

## O stranici
Ova stranica koristi [Flask-git](https://github.com/pallets/flask) framework na bazi Pythona. Nudi mnoge mogućnosti koje olakšavaju izradu stranica i web aplikacija. Važno je za napomenut da upravo zbog toga se stranice ne mogu gledati lokalno bez da se framework koristi te su ispod ispisane upute kako pokrenuti stranicu lokalno.

## Upute za pokrenuti lokalni Flask server (Windows)
1. Potrebno je instralirati [Python3](https://www.python.org/downloads/)
2. Otvoriti Command Prompt te navigirati u root folder stranice komandom `cd mms-zavrsni-main`<br /> npr. `C:\Users\User>cd Downloads\mms-zavrsni-main`
3. Unutar foldera napraviti virtual environment `py -3 -m venv venv`
4. Aktivirati virtual environment `venv\Scripts\activate`, nakon čega bi Command Prompt trebao dobiti (venv) na početku trenutne staze npr. `(venv) C:\Users\User\Downloads\mms-zavrsni-main>`
5. Instalirati pakete koji su potrebni za izvođenje Flask servera `pip install -r requirements.txt`
6. Promijeniti ime python datoteke koju ćemo pokrenuti `ren mms.py app.py` (iz nekog razloga imao sam problema na Windowsima ako se datoteka ne zove app.py, taj se problem nije pojavljivao u Linuxu)
7. Postaviti python datoteku za pokretanje `setx FLASK_APP "app.py"`
8. Pokrenuti Flask server `flask run` nakon čega bi trebali ovo dobiti:
```
(venv) C:\Users\User\Downloads\mms-zavrsni-main>flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
9. Otvoriti `http://127.0.0.1:5000/` u web pregledniku.
