# Docker põhialused

Eelmisel nädalal õppisime Ansible role'e, kuidas automatiseerida serverite konfiguratsiooni. Täna astume järgmisesse dimensiooni - konteinerite maailma. Kui Ansible aitab hallata olemasolevaid servereid, siis Docker muudab selle, kuidas me rakendusi üldse ehitame ja jooksutame.

Mõtle konteineritele kui LEGO klotside süsteemile - iga konteiner on üks klots, mis saab kiiresti kokku panna suuremateks rakendusteks. Aga erinevalt LEGO-st, need "klotsid" sisaldavad terveid rakendusi ja jooksevad igal arvutil täpselt ühesuguselt.

## Mis on Docker ja miks seda vaja

Docker on tööriist konteinerite loomiseks ja haldamiseks. Aga mis need konteinerid siis on ja miks nad paremad on kui traditsioonilised lahendused?

Põhiline probleem, mida Docker lahendab, on kuulus "töötab mu masinas" sündroom. Sa ehitad rakenduse oma laptopil, see töötab suurepäraselt. Liigutad serverisse - ei tööta. Kolleeg üritab käivitada oma masinas - ei tööta. Probleem pole sinus ega sinu koodis, vaid selles, et erinevates keskkondades on erinevad versioonid, sõltuvused ja konfiguratsioonid.

Docker võimaldab sul pakkida rakenduse koos kõigi sõltuvustega ühte "kasti" ehk konteinerisse, mis töötab igal arvutil täpselt ühesuguselt. See konteiner sisaldab kõike vajalikku: operatsioonisüsteemi osi, runtime'i, teeke, sõltuvusi ja sinu rakendust ennast.

### Põhilised mõisted

Enne kui edasi liikume, pead mõistma nelja põhilist mõistet:

**Image** on mall konteineri jaoks, nagu CD-ROM või programmi installer. See sisaldab kõike vajalikku: operatsioonisüsteemi osi, rakendust ja kõiki sõltuvusi. Image on muutumatu - kui sa teed sinna muudatusi, loodi tegelikult uus image.

**Container** on käivitatud image, nagu programm, mis jookseb su arvutis. Container elab ja töötab, teda saab peatada, taaskäivitada või kustutada. Iga kord kui käivitad sama image'i, saad uue konteineri.

**Dockerfile** on tekstifail, mis sisaldab retsepti image'i loomiseks. See kirjeldab samm-sammult, kuidas image ehitada: millist base image'i kasutada, millised failid kopeerida, millised käsud käivitada.

**Registry** on pood image'ite jaoks, nagu App Store nutitelefonile. Kõige populaarsem on Docker Hub, kus leidub tuhandeid valmis image'e kõikvõimalike rakenduste jaoks.

## Konteinerid versus virtuaalmasinad

Et mõista, miks konteinerid on revolutsiooniline, vaatame, kuidas server infrastruktuur on aastate jooksul arenenud.

### Tehnoloogia evolutsioon

Füüsiliste serverite ajastul (kuni 2000. aastate algus) tähendas üks rakendus üht serverit. See oli kallis ja ebaefektiivne - enamik servereid kasutasid ainult 5-15% oma võimsusest, aga maksma pidid täishinnaga.

Virtuaalmasinad (2000-2010) lahendasid osa probleemist. Üks võimas server sai majutada mitu virtuaalmasinat, igaüks oma operatsioonisüsteemiga. Aga iga virtuaalmasin vajab täispikka operatsioonisüsteemi, mis tähendab 1-2GB mälukasutust ja 20GB kettaruumi isegi lihtsa rakenduse jaoks.

Konteinerid (alates 2013) viisid efektiivsuse järgmisele tasemele. Erinevalt virtuaalmasinadest jagavad kõik konteinerid sama operatsioonisüsteemi kerneli. See tähendab, et üks konteiner kasutab ainult 10-100MB mälu ja käivitub sekundite jooksul.

### Praktiline erinevus

Virtuaalmasin on nagu terve eraldi korter - seal on oma köök, vannituba, elekter, kõik. Iga korter on täiesti eraldatud, aga ka ressursimahukas.

Konteiner on nagu tuba jagatud korteris - sa jagad kööki ja vannituba (operatsioonisüsteemi kerneli), aga sinu tuba (rakendus) on täiesti privaatne. See on palju efektiivsem.

Numbrites väljendub see drastilises erinevuses:

| Kriteerium | Virtuaalmasinad | Konteinerid |
|------------|------------------|------------|
| Käivitusaeg | 1-2 minutit | 1-5 sekundit |
| Mälukasutus | 1-8GB | 10-100MB |
| Mahtuvus serveris | 10-50 | 100-1000 |
| Kettaruumi vajadus | 10-50GB | 100MB-1GB |

### Millal kasutada mida

Virtuaalmasinad on endiselt õiged valik, kui vajad erinevaid operatsioonisüsteeme samal serveril, maksimaalset turvalist eraldatust või töötad legacy süsteemidega, mis pole konteineri jaoks sobivad.

Konteinerid on ideaalsed kaasaegsete veebirakenduste, mikroteenuste arhitektuuri, arendus- ja testimiskeskkondade ning kiire deployment'i jaoks.

## Docker'i installimine ja seadistamine

Docker'i installimine Ubuntu või Debian süsteemis käib mitmeastmeliselt, sest tahame kasutada ametlikku Docker'i repositooriumit, mitte distributsiooniga kaasas olevat aegunud versiooni.

Kõigepealt uuenda pakettide nimistut ja installi vajalikud eeldused:

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
```

Lisa Docker'i ametlik GPG võti ja repositoorium:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Nüüd saad installida Docker'i:

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

Käivita Docker'i teenus ja seadista see automaatselt käivituma:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Viimane samm on lisada oma kasutaja docker gruppi, et sa ei peaks pidevalt sudo kasutama:

```bash
sudo usermod -aG docker $USER
```

Pärast seda pead välja logima ja tagasi sisse logima, või käivitama `newgrp docker` käsu.

Testi installatsiooni:

```bash
docker --version
docker run hello-world
```

Viimane käsk laadib väikese testi image'i ja käivitab selle. Kui näed tervitussõnumit, on Docker edukalt installitud.

## Docker'i käsurea põhialused

Docker'i käsurea süntaks järgib lihtsat mustrit: `docker [VALIKUD] KÄSK [ARGUMENDID]`. Kõik Docker'i funktsioonid on kättesaadavad alamkäskude kaudu.

### Image'ide haldamine

Image'ide allalaadimine käib `pull` käsuga:

```bash
docker pull nginx             # Viimane versioon
docker pull nginx:1.21        # Konkreetne versioon
docker pull ubuntu:20.04      # Erinevad operatsioonisüsteemid
```

Lokaalse image'ide vaatamiseks kasuta:

```bash
docker images                 # Kõik lokaalsed image'id
docker search mysql           # Otsi Docker Hub'ist
```

Kasutamata image'ide kustutamiseks:

```bash
docker rmi nginx              # Kustuta konkreetne image
docker image prune            # Kustuta kõik kasutamata image'id
```

### Konteinerite käivitamine

Lihtsaim viis konteineri käivitamiseks:

```bash
docker run nginx
```

See käsk laadib nginx image'i (kui see veel masinas pole), loob sellest konteineri ja käivitab selle. Probleem on see, et käsk blokeerib terminali.

Praktilisemad variandid:

```bash
docker run -d nginx                 # Käivita taustال (detached)
docker run --name my-web nginx     # Anna konteinerile nimi
docker run -p 8080:80 nginx        # Ühenda port 8080 konteineri port 80-ga
```

Interaktiivse konteineri jaoks, näiteks kui tahad Ubuntu'ga katsetada:

```bash
docker run -it ubuntu bash         # Interaktiivne terminal
```

Käivitatud konteineris käsu jooksutamiseks:

```bash
docker exec -it container_name bash # Ühenda käivitatud konteinerisse
```

### Konteinerite jälgimine ja haldamine

Vaata, millised konteinerid töötavad:

```bash
docker ps                     # Töötavad konteinerid
docker ps -a                  # Kõik konteinerid (ka peatatud)
```

Konteineri logide vaatamiseks:

```bash
docker logs container_name    # Näita loge
docker logs -f container_name # Jälgi loge reaalajas
```

Konteineri elutsükli haldamine:

```bash
docker start container_name   # Käivita peatatud konteiner
docker stop container_name    # Peata konteiner
docker restart container_name # Taaskäivita
docker rm container_name      # Kustuta konteiner
```

### Praktiline näide

Vaatame, kuidas käivitada lihtne veebiserver:

```bash
# Käivita Nginx konteiner
docker run -d --name my-web -p 8080:80 nginx

# Testi brauseris või curl'iga
curl http://localhost:8080

# Vaata konteineri loge
docker logs my-web

# Peata ja kustuta
docker stop my-web
docker rm my-web
```

## Dockerfile - rakenda konteineri retsept

Dockerfile on tekstifail, mis sisaldab juhiseid Docker'ile, kuidas ehitada image sinu rakenduse jaoks. See on nagu retsept, mis kirjeldab kõik vajalikud sammud.

### Põhilised juhised

**FROM** määrab base image'i, millelt hakata ehitama:

```dockerfile
FROM nginx:alpine           # Väike ja kiire
FROM python:3.9             # Python runtime
FROM node:16                # Node.js runtime
```

Tootmises kasuta alati konkreetseid versioone:

```dockerfile
FROM node:16.14.2-alpine    # Täpne versioon, mitte "latest"
```

**WORKDIR** määrab töökatalogi konteineris:

```dockerfile
WORKDIR /app                # Kõik järgnevad käsud tehakse siin
```

**COPY** kopeerib faile host süsteemist konteinerisse:

```dockerfile
COPY app.py /app/           # Üks fail
COPY src/ /app/src/         # Terve kaust
COPY . /app/                # Kõik praegusest kaustast
```

**RUN** käivitab käsu image'i ehitamise ajal:

```dockerfile
RUN apt-get update && apt-get install -y curl
RUN pip install -r requirements.txt
```

**CMD** määrab vaikimisi käsu, mis käivitatakse konteineri käivitamisel:

```dockerfile
CMD ["python", "app.py"]
CMD ["nginx", "-g", "daemon off;"]
```

### Praktiline näide: Python rakendus

Loome lihtsa Flask rakenduse ja pakime selle konteinerisse.

Loo fail `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Tere Docker'i maailmast!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Loo fail `requirements.txt`:

```
Flask==2.3.2
```

Loo `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Kopeeri sõltuvuste fail esimesena (cache optimeerimiseks)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopeeri rakenduse kood viimasena
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
```

Ehita ja käivita:

```bash
# Ehita image
docker build -t my-python-app .

# Käivita konteiner
docker run -d --name flask-app -p 5000:5000 my-python-app

# Testi
curl http://localhost:5000
```

### Cache optimeerimise saladus

Märkasid, et kopeerisime `requirements.txt` enne `app.py` faili? See pole juhus. Docker cache'ib iga kihi ja ehitab ainult muutunud kihid uuesti.

Kui paneksime kogu koodi korraga, siis iga väike muudatus `app.py` failis põhjustaks kõigi sõltuvuste uuesti installimist. Sõltuvuste failide kopeerimine eraldi tähendab, et need installitakse uuesti ainult siis, kui sõltuvused muutuvad.

### .dockerignore fail

Nagu `.gitignore`, aitab `.dockerignore` hoida image'ist välja faile, mida pole vaja:

```
__pycache__
*.pyc
.git
README.md
.env
node_modules
```

## Andmete säilitamine volume'idega

Vaikimisi kaotad kõik andmed, kui konteineri kustutad. See on hea isolatsiooni jaoks, aga halb andmebaasidele või failide säilitamiseks.

### Probleem demonstratsioon

```bash
# Käivita Ubuntu konteiner
docker run -it --name test ubuntu bash

# Konteineris
echo "Oluline andmeid" > /tmp/data.txt
exit

# Kustuta konteiner
docker rm test

# Andmed on läinud igavesti!
```

### Named volume'id

Volume'id on Docker'i viis andmete säilitamiseks väljaspool konteinerit:

```bash
# Loo volume
docker volume create mydata

# Kasuta volume'i
docker run -d \
  --name database \
  -v mydata:/var/lib/mysql \
  mysql:8.0

# Volume info
docker volume ls
docker volume inspect mydata
```

### Bind mount'id

Vahel tahad otse host süsteemi kausta konteinerisse ühendada:

```bash
# Ühenda host'i kaust konteinerisse
docker run -d \
  --name web \
  -v /home/kasutaja/veebisait:/usr/share/nginx/html \
  nginx

# Muudatused host'is on kohe nähtavad konteineris
echo "<h1>Tere!</h1>" > /home/kasutaja/veebisait/index.html
curl http://localhost  # Uus sisu on kohe nähtav
```

### Andmebaasi näide

Vaatame, kuidas volume'id praktikas töötavad PostgreSQL'i näitel:

```bash
# Loo volume andmebaasi jaoks
docker volume create postgres_data

# Käivita andmebaas
docker run -d \
  --name mydb \
  -e POSTGRES_PASSWORD=secret \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:13

# Loo natuke andmeid
docker exec -it mydb psql -U postgres
```

PostgreSQL shell'is:

```sql
CREATE TABLE kasutajad (id SERIAL, nimi TEXT);
INSERT INTO kasutajad (nimi) VALUES ('Alice'), ('Bob');
\q
```

Nüüd kustuta konteiner:

```bash
docker stop mydb
docker rm mydb
```

Käivita uus konteiner sama volume'iga:

```bash
docker run -d \
  --name newdb \
  -e POSTGRES_PASSWORD=secret \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:13

# Kontrolli, et andmed on alles
docker exec -it newdb psql -U postgres -c "SELECT * FROM kasutajad;"
```

Andmed on täpselt seal, kus nad olid!

## Arendamise töövoog

Üks Docker'i suurimaid eeliseid on arendamise kiiruse suurendamine. Sa saad oma rakendust arendada konteineris ilma, et peaks vaeva nägema sõltuvuste installimisega oma masinas.

```bash
# Mount'i oma lähtekood arendamiseks
docker run -it \
  --name dev \
  -v $(pwd):/workspace \
  -w /workspace \
  -p 3000:3000 \
  node:16 bash
```

Nüüd saad editeerida faile oma lemmik redaktoris host süsteemis, aga käivitada need konteineris. Kõik muudatused on kohe nähtavad.

## Levinumad probleemid ja lahendused

### Õiguste probleem

Kui saad "permission denied" vea Docker'i käskude käivitamisel, pole sa tõenäoliselt docker grupis:

```bash
sudo usermod -aG docker $USER
# Logi välja ja tagasi sisse
```

### Port juba kasutusel

Kui port on juba kasutusel, leia konfliktne konteiner:

```bash
docker ps                      # Leia, mis kasutab porti
docker stop container_name     # Peata see
# Või kasuta teist porti: -p 8081:80
```

### Konteiner kohe väljub

Kui konteiner käivitub ja kohe väljub, vaata loge:

```bash
docker logs container_name
```

Tavaliselt puudub foreground protsess. Kontrolli, et CMD Dockerfile'is käivitab midagi, mis ei lõpe kohe.

### Ressursside puhastamine

Docker kipub aja jooksul palju ruumi kasutama:

```bash
docker system df             # Vaata kettakasutust
docker system prune          # Kustuta kasutamata objektid
docker system prune -a       # Kustuta ka kasutamata image'id
```

## Kokkuvõte

Selles loengus õppisid Docker'i alused: mis on konteinerid, kuidas nad erinevad virtuaalmasinadest ja miks nad on kaasaegse tarkvara arendamise põhialus. Oskad nüüd Docker'it installida, lihtsat Dockerfile'i kirjutada ja volume'ide abil andmeid säilitada.

Docker'i tõeline võimsus tuleb esile, kui hakata ehitama keerulisemaid süsteeme. Järgmises loengus õpime optimeerimise tehnikaid, mitmestaadilisi ehitusi, võrgustiku konfiguratsiooni ja tutvume Podman'iga kui Docker'i alternatiiviga.

Valmistumine järgmiseks: mõtle sellele, kuidas optimeerida Docker image'eid nii, et need oleksid väiksemad, kiiremad ja turvalisemad. Kuidas hallata keerulist rakendust, mis vajab andmebaasi, veebiserverit ja cache'i kõike koos?