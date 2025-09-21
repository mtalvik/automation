# Docker'i edasijõudnute tehnikad

Eelmises loengus õppisime Docker'i alused. Täna keskendume optimeerimisele ja tootmiskeskkonnas kasutatavate lahenduste ehitamisele, sest tööelus ei piisa sellest, et konteiner "töötab" - see peab töötama kiiresti, turvaliselt ja stabiilselt.

Alustame kõige valusamast punktist: miks sinu Docker build võtab aega nagu vanaaegne internetiühendus ja kuidas seda parandada.

## Dockerfile'i optimeerimine

### Kihtide cache'imise probleem

Dockeri üks võimsaimaid omadusi on ka selle suurim lõks algajatele. Docker ehitab image'i kihtide kaupa ja cache'ib neid. Kui muudad ühte rida Dockerfile'is, siis kõik järgnevad kihid ehitatakse uuesti. See tähendab, et vale järjekord võib muuta iga väikese koodimuudatuse 10-minutiliseks ootamiseks.

Vaatame tüüpilist viga Node.js rakenduse puhul:

```dockerfile
FROM node:16
COPY . /app/          # Kogu kood kopeeritakse kohe
WORKDIR /app
RUN npm install      # Sõltuvused installib uuesti iga koodimuudatuse puhul
CMD ["npm", "start"]
```

Probleem seisneb selles, et kui muudad ühtki koodi faili, kopeeritakse kogu projekt uuesti ja npm install käivitatakse nullist. Kuna sõltuvused (package.json) muutuvad palju harvem kui rakenduse kood, peaks need installima eraldi kihti.

Optimeeritud versioon näeb välja selline:

```dockerfile
FROM node:16
WORKDIR /app

# Kopeeri ainult sõltuvuste failid
COPY package*.json ./
RUN npm install

# Kopeeri lähtekood alles pärast sõltuvuste installimist
COPY . .
CMD ["npm", "start"]
```

Nüüd muudab koodi muutmine ainult viimast kihti, sõltuvused jäävad cache'isse ja build on minutite asemel sekundite küsimus.

### RUN käskude optimeerimine

Docker loob iga RUN käsu jaoks eraldi kihi. Liiga palju kihte teeb image'i suuremaks ja aeglasemaks. Veelgi hullem on see, et iga kiht jääb image'i sisse, isegi kui järgmine kiht kustutab eelmise tulemusi.

Vale lähenemine:
```dockerfile
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean
```

See loob kolm kihti, kusjuures esimeses on kogu pakettide loend, teises veel rohkem faile ja alles kolmas üritab puhastada.

Õige lähenemine:
```dockerfile
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

Üks kiht, kus kõik tehakse ja kohe ka puhastatakse.

### CMD ja ENTRYPOINT erinevus

Need kaks käsku tekitavad algajates sageli segadust, kuigi nende kasutusala on üsna selge.

CMD määrab vaikimisi käsu, mida saab käivitamisel üle kirjutada:

```dockerfile
CMD ["python", "app.py"]
```

```bash
docker run myapp              # Käivitab: python app.py
docker run myapp echo hello   # Käivitab: echo hello
```

ENTRYPOINT määrab käsu, mis käivitatakse alati:

```dockerfile
ENTRYPOINT ["python", "app.py"]
```

```bash
docker run myapp              # Käivitab: python app.py
docker run myapp --debug      # Käivitab: python app.py --debug
```

Parim praktika on kasutada neid koos:

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

Nii saad paindliku käivitamise, kus rakendus käivitub alati õige skriptiga, aga argumente saab vajadusel üle kirjutada.

## Mitmestaadilised ehitused

### Probleem: ehitustööriistad tootmises

Tüüpiline Node.js rakendus vajab ehitamiseks kogu Node.js keskkonnad, npm'i, võib-olla Webpack'i, TypeScript'i ja veel hulka tööriistu. Aga tootmises pole neid vaja - seal piisab ainult ehitatud failidest ja runtime'ist.

Traditsioonilise lähenemisega jääb image suureks:

```dockerfile
FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install        # Kaasa arvatud arendussõltuvused!
COPY . .
RUN npm run build
CMD ["npm", "start"]
```

Selline image võib olla gigabaidi suurune, sest sisaldab kõike: lähtekood, arendussõltuvused, ehitustööriistad.

Mitmestaadilise ehitusega saad hoida ainult vajaliku:

```dockerfile
# Esimene staadium: ehitamine
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Teine staadium: tootmine
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY --from=builder /app/dist ./dist
CMD ["npm", "start"]
```

Tulemus on 80% väiksem image, mis laadib kiiremini ja sisaldab vähem potentsiaalseid turvaaukusi.

### Äärmuslik optimeerimine

Go keele puhul saab tulemust veelgi drastilisemalt parandada:

```dockerfile
# Ehitusstaadium
FROM golang:1.19-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o app

# Käitamisstaadium
FROM scratch  # Täiesti tühi image!
COPY --from=builder /app/app /app
EXPOSE 8080
CMD ["/app"]
```

Lõpptulemus on ainult 5MB suurune image, mis sisaldab vaid käivitatavat faili. See on võimalik, sest Go kompileerib staatilise binaari, mis ei vaja operatsioonisüsteemi teeke.

## Turvalisuse põhitõed

### Mitte-root kasutaja

Vaikimisi käivituvad Docker konteinerid root kasutajana. See tähendab, et kui ründaja saab su rakenduse üle kontrolli, on tal kohe administraatori õigused. Turvalisuse seisukohalt on see nagu anda igale külalisele oma kodu võtmed.

```dockerfile
# Kasuta konkreetseid versioone
FROM node:16.14.2-alpine  # Mitte lihtsalt: FROM node

# Loo spetsiaalne kasutaja
RUN addgroup -g 1001 -S appuser && \
    adduser -S appuser -u 1001

# Lülitu sellele kasutajale
USER appuser

# Kopeeri failid õige omanikuga
COPY --chown=appuser:appuser . .
```

### Minimalistlik lähenemine

Alpine Linux on populaarne valik Docker image'ide jaoks, sest see on drastiliselt väiksem kui tavapärased distributsioonid:

```dockerfile
FROM python:3.9-alpine  # ~50MB vs python:3.9 ~900MB
```

Samuti peaks paigaldama ainult hädavajalikke pakette ja puhastama kohe peale installimist:

```dockerfile
RUN apk add --no-cache build-base && \
    pip install -r requirements.txt && \
    apk del build-base
```

### Tervisecontrollid

Rakendus võib käivituda edukalt, aga olla siiski katki. Tervisecontroll aitab Docker'il ja orkestreerimissüsteemidel mõista, kas konteiner tegelikult töötab:

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s \
    CMD curl -f http://localhost:5000/health || exit 1
```

## Docker'i võrgustik

Algajad mõtlevad Docker'i konteineridest kui eraldatud saaretest, aga tegelikult peavad need omavahel suhtlema. Docker'i võrgustiku mõistmine on kriitilise tähtsusega mitme konteineri rakenduste ehitamiseks.

### Vaikimisi võrgu probleem

Docker'i vaikimisi käitumine on lihtne: kõik konteinerid saavad IP aadressi bridge võrgus ja saavad üksteist ping'ida. Aga see töötab ainult IP aadresside kaudu:

```bash
docker run -d --name web1 nginx
docker run -d --name web2 nginx

# Konteinerid saavad IP aadressid
docker exec web1 ping 172.17.0.3  # Töötab
docker exec web1 ping web2        # Ei tööta!
```

Probleem on selles, et vaikimisi bridge võrk ei paku nimede lahendamist. Pead teadma täpseid IP aadresse, mis on ebapraktiline ja muutub iga taaskäivitusega.

### Kohandatud võrgud

Lahendus on luua kohandatud võrk:

```bash
# Loo rakendusespetsiifiline võrk
docker network create myapp-network

# Käivita konteinerid selles võrgus
docker run -d --name web --network myapp-network nginx
docker run -d --name api --network myapp-network python:3.9

# Nüüd töötab nimede lahendamine
docker exec web ping api          # Töötab!
docker exec api ping web          # Töötab!
```

Nüüd saavad konteinerid üksteist nime järgi kätte, mis teeb konfiguratsiooni palju lihtsamaks.

### Kolmekihiline rakendus

Tõelises rakenduses tahad sageli eraldada erinevaid komponente. Näiteks veebiserver ei tohiks otse andmebaasiga rääkida - see peaks käima API kaudu.

```bash
# Loo kaks võrku
docker network create frontend   # Veeb ↔ API
docker network create backend    # API ↔ Andmebaas

# Andmebaas (ainult backend võrgus)
docker run -d --name db \
  --network backend \
  -e POSTGRES_PASSWORD=secret \
  postgres:13

# API (mõlemas võrgus)
docker run -d --name api \
  --network backend \
  python:3.9
docker network connect frontend api

# Veebiserver (ainult frontend võrgus)
docker run -d --name web \
  --network frontend \
  -p 80:80 \
  nginx
```

Nii saad turvalisema arhitektuuri, kus iga komponent näeb ainult seda, mida ta vajab.

## Podman kui Docker'i alternatiiv

Podman on Red Hat'i poolt arendatud Docker'i alternatiiv, mis lahendab mitu oluliselist turvaprobleemi. Kõige olulisem erinevus on see, et Podman ei vaja daemon'it.

### Arhitektuuri erinevus

Docker töötab klient-server mudelis:

```
Sa → Docker klient → Docker daemon → Konteiner
                           ↑
                    Alati töötab kui root
```

Podman'is pole daemon'it:

```
Sa → Podman → Konteiner
       ↑
   Otsene käivitamine
```

### Peamised erinevused

| Aspekt | Docker | Podman |
|---------|---------|---------|
| Daemon | Vajab dockerd | Ei vaja daemon'it |
| Root õigused | Vajab root õigusi | Töötab tavalise kasutajana |
| Käivitamine | Daemon peab töötama | Kohe kasutamisvalmis |
| Turvalisus | docker grupp = root | Tavaline kasutaja |

### Käsud on peaaegu identset

Podman'i suurim eelis on see, et kõik Docker'i käsud töötavad:

```bash
# Docker                 →    Podman
docker pull nginx       →    podman pull nginx
docker run -d nginx     →    podman run -d nginx
docker ps               →    podman ps
docker logs name        →    podman logs name
```

Saad isegi teha alias'e:

```bash
alias docker=podman
# Nüüd kõik Docker'i käsud töötavad Podman'iga!
```

### Rootless konteinerid

Docker'i suurim turvaprobleem on see, et docker grupi liige on sama, mis root kasutaja. Podman lahendab selle user namespace'ide abil:

```bash
# Podman'is
podman run -it alpine id
# uid=0(root) gid=0(root)  ← Konteineri sees
whoami  # user ← Host süsteemis

# Konteineri root (0) vastab host'i kasutajale (1000)
```

## Levinumad vead

### Aegunud pakettide cache

Docker'i kihtide süsteem võib sind lõksu püüda. Kui teed pakettide uuenduse ja installimise eraldi käskudega, võib juhtuda, et kasutad vana cache'i:

```dockerfile
# Vale
RUN apt-get update
RUN apt-get install -y curl  # Kasutab võimalikult vana pakettide loendit

# Õige
RUN apt-get update && apt-get install -y curl
```

### Root kasutaja probleem

Paljud alustava arendajad ei mõtle turvalisusele ja jätavad rakenduse käivituma root kasutajana:

```dockerfile
# Vale
FROM ubuntu
COPY app /app
CMD ["/app"]  # Käivitub root kasutajana

# Õige
FROM ubuntu
RUN useradd -m appuser
USER appuser
COPY app /app
CMD ["/app"]
```

### Liiga suured image'id

Base image'i valik mõjutab drastiliselt lõppliku image'i suurust:

```dockerfile
# Vale
FROM ubuntu:latest  # ~72MB + kõik tööriistad
RUN apt-get update && apt-get install -y python3

# Õige
FROM python:3.9-alpine  # ~45MB + Python juba sees
```

## Tootmiskeskkonna põhimõtted

Eduka Docker'i kasutamise tootmiskeskkonnas saab kokku võtta mõne olulise põhimõttega, mille järgimine aitab vältida kõige sagedasemaid probleeme.

Kasuta alati ametlikke base image'e. Nende turvalisust jälgitakse, need uuendatakse regulaarselt ja on optimeeritud. Kopeeri sõltuvuste failid enne rakenduse koodi, et ära kasutada kihtide cache'imise eeliseid. Kasuta mitmestaadilisi ehitusi tootmises, et hoida image väike ja turvaline.

Loo alati mitte-root kasutaja ja määra paketiversioonid kindlalt. Kombineeri RUN käsud üheks ja kasuta .dockerignore faili. Lisa tervisecontrollid, et orkestreerimissüsteemid saaksid konteineri seisundit jälgida.

Kasuta kohandatud võrke mitme konteineri rakenduste jaoks ja nimega volume'e andmete säilitamiseks tootmises.

## Praktiline näide: optimeeritud Flask rakendus

Vaatame, kuidas need kõik põhimõtted töötavad koos lihtsa Flask rakenduse näitel.

**requirements.txt:**
```
Flask==2.3.2
gunicorn==21.2.0
```

**app.py:**
```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.getenv("NODE_ENV", "unknown")
    return f'<h1>Tere, {env} keskkonnas!</h1>'

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Optimeeritud Dockerfile:**
```dockerfile
# Mitmestaadline ehitus
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Tootmisstaadium
FROM python:3.9-slim
WORKDIR /app

# Mitte-root kasutaja
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Kopeeri sõltuvused
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Kopeeri lähtekood
COPY --chown=appuser:appuser . .

# Lülitu mitte-root kasutajale
USER appuser

# Tervisecontroll
HEALTHCHECK --interval=30s --timeout=10s \
    CMD curl -f http://localhost:5000/health || exit 1

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

**Ehitamine ja käivitamine:**
```bash
# Ehita optimeeritud image
docker build -t flask-app:optimized .

# Loo kohandatud võrk
docker network create app-network

# Käivita kohandatud võrgus
docker run -d \
  --name flask-app \
  --network app-network \
  -e NODE_ENV=production \
  -p 5000:5000 \
  --restart=unless-stopped \
  flask-app:optimized

# Testi
curl http://localhost:5000
curl http://localhost:5000/health
```

## Kokkuvõte

Selles loengus õppisid Docker'i edasijõudnute tehnikaid, mis muudavad sinu image'id kiiremaks, turvalisemaks ja väiksemaks. Dockerfile'i optimeerimine kihtide cache'imisega võib muuta ehitusprotsessi minutitest sekunditeks. Mitmestaadilised ehitused hoiavad tootmise image'id väikesena ja turvalisena.

Docker'i võrgustiku mõistmine on kriitilise tähtsusega mitme konteineri rakenduste ehitamiseks. Podman pakub huvitavat alternatiivi, eriti kui turvalisus on prioriteet.

Järgmises loengus vaatame Docker Compose'i, mis aitab hallata keerukaid mitme konteineri rakendusi, kus vaja on andmebaasi, veebiserverit, cache'i ja monitooringu süsteemi kõike koos.