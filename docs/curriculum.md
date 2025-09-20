# Automatiseerimise kursuse õppekava

**ITS-24 - Täiskasvanute klass (34 tundi, 8 moodulit)**

## Kursuse ülevaade

Kursus käsitleb olulisi automatiseerimisvahendeid ja praktikaid kaasaegsetes DevOps töövoogudes. Iga moodul sisaldab 4 tundi kontaktõpet ning iseseisvat tööd.

## Kursuse struktuur

| Moodul | Teema | Kontakttunnid | Praktiline ülesanne | Iseseisev töö |
|--------|-------|---------------|---------------------|---------------|
| 1 | Git versioonihaldus | 4h | Git projekti loomine näidetega | Tutvu Git'i ajaloo ja sisemise toimimisega |
| 2 | Ansible alused | 4h | LAMP keskkonna loomine (VirtualBox/Vagrant) | Tutvu Ansible arhitektuuri ja YAML süntaksiga |
| 3 | Docker alused | 4h | Mitme teenusega rakenduse konteineriseerimine | Uuri Docker'i arhitektuuri ja turvalisust |
| 4 | Docker orkestreerimine | 4h | Täieliku rakenduse paigaldamine | Tutvu konteinerite orkestreerimise mustritega |
| 5 | Ansible edasijõudnutele | Iseseisev labor | Edasijõudnud funktsioonide harjutused | Õpi Jinja2 malle ja Ansible Vault |
| 6 | Ansible rollid | Iseseisev labor | Rolli loomine ja võrdlus Puppet'iga | Tutvu rollide parimate praktikatega |
| 7 | Terraform alused | 2h | Kohaliku infrastruktuuri loomine | Õpi Infrastructure as Code põhimõtteid |
| 8 | CI/CD + Kubernetes | 2h | Pipeline loomine ja K8s tutvustus | Tutvu GitOps ja Kubernetes põhimõtetega |

## Moodulite kirjeldused

### Moodul 1: Git versioonihaldus (4h)

**Kontakttundide sisu:**
- Git'i põhimõtted ja töövoog (1h)
- Põhikäsud praktiliselt (1h)
- GitHub ja meeskonnatöö (1h)
- Harude haldamine ja ühendamine (1h)

**Käsitletavad teemad:**
- Versioonihalduse alused
- Kohalik ja kaugrepositoorium
- Meeskonnatöö ja pull request'id
- Konfliktide lahendamine

**Kodutööd:**
1. Loo Git projekt koos harude töövooga
2. Tutvu Git'i sisemise toimimisega (2-3 tundi lugemist)

### Moodul 2: Ansible alused (4h)

**Kontakttundide sisu:**
- Ansible arhitektuur (30 min)
- Virtuaalmasina seadistamine Vagrant'iga (30 min)
- SSH konfiguratsioon ja inventory (1h)
- Ad-hoc käsud praktiliselt (1h)
- Esimene playbook (1h)

**Käsitletavad teemad:**
- Ansible arhitektuur ja komponendid
- SSH võtmepõhine autentimine
- Inventory haldamine
- YAML süntaks
- Playbook'ide struktuur

**Kodutööd:**
1. Paigalda LAMP keskkond Vagrant virtuaalmasinatesse
2. Tutvu Ansible dokumentatsiooniga (2-3 tundi)

### Moodul 3: Docker alused (4h)

**Kontakttundide sisu:**
- Konteinerid vs virtuaalmasinad (30 min)
- Docker'i paigaldamine ja esimene konteiner (1h)
- Dockerfile'i loomine (1.5h)
- Võrgundus ja andmemahud (1h)

**Käsitletavad teemad:**
- Konteineritehnoloogia põhimõtted
- Docker'i põhikäsud
- Dockerfile'i parimad praktikad
- Konteinerite võrgundus

**Kodutööd:**
1. Konteineriseeri mitu omavahel suhtlevat rakendust
2. Uuri Docker'i turvalisuse aspekte (2-3 tundi)

### Moodul 4: Docker orkestreerimine (4h)

**Kontakttundide sisu:**
- Docker Compose põhimõtted (30 min)
- Compose faili loomine (1.5h)
- Mitme teenusega rakendus (1.5h)
- Keskkondade haldamine (30 min)

**Käsitletavad teemad:**
- Docker Compose süntaks
- Teenuste defineerimine
- Võrgundus Compose'is
- Keskkonna muutujad

**Kodutööd:**
1. Paigalda täielik veebirakendus Docker Compose'iga
2. Tutvu orkestreerimise mustritega (2-3 tundi)

### Moodul 5: Ansible edasijõudnutele (iseseisev labor)

**Labori struktuur:**
- Sammhaaval juhised harjutusteks
- Muutujad ja Jinja2 mallid
- Handlers ja vigade käsitlemine
- Ansible Vault praktika

**Käsitletavad teemad:**
- Keerulised playbook'id
- Mallide kasutamine
- Turvalisuse parimad praktikad
- Jõudluse optimeerimine

**Kodutööd:**
1. Täida kõik labori harjutused
2. Süvene Ansible dokumentatsiooni (2-3 tundi)

### Moodul 6: Ansible rollid (iseseisev labor)

**Labori struktuur:**
- Rolli struktuuri loomine
- Muutujad ja vaikeväärtused
- Sõltuvuste haldamine
- Ansible Galaxy kasutamine

**Käsitletavad teemad:**
- Rollide struktuur
- Korduvkasutatavus
- Galaxy kogukond
- Võrdlus teiste vahenditega

**Kodutööd:**
1. Loo oma Ansible roll
2. Võrdle Ansible ja Puppet lahendusi (2-3 tundi)

### Moodul 7: Terraform alused (2h kontaktõpe)

**Kontakttundide sisu:**
- Infrastructure as Code ülevaade (30 min)
- Terraform praktiliselt (1h)
- Harjutus kohaliku infrastruktuuriga (30 min)

**Käsitletavad teemad:**
- Terraform põhimõtted
- HCL süntaks
- State'i haldamine
- Provider'id

**Kodutööd:**
1. Loo kohalik infrastruktuur Terraform'iga
2. Tutvu IaC parimate praktikatega (2-3 tundi)

### Moodul 8: CI/CD ja Kubernetes (2h kontaktõpe)

**Kontakttundide sisu:**
- Automatiseerimise pipeline (1h)
- Kubernetes tutvustus minikube'iga (30 min)
- Tööriistade integratsioon (30 min)

**Käsitletavad teemad:**
- GitHub Actions
- Pipeline'i loomine
- Kubernetes põhimõtted
- DevOps praktikad

**Kodutööd:**
1. Loo täielik CI/CD pipeline
2. Tutvu Kubernetes dokumentatsiooniga (2-3 tundi)

## Õpiväljundid

Kursuse läbinu:
- Valdab versioonihaldust Git'iga
- Oskab automatiseerida infrastruktuuri Ansible'iga
- Mõistab konteineritehnoloogiat ja Docker'it
- Tunneb Infrastructure as Code põhimõtteid
- Omab praktilist kogemust CI/CD pipeline'idega

## Hindamine

- Praktilised tööd (60%)
- Iseseisev töö ja reflektsioon (20%)
- GitHub portfoolio (10%)
- Lõpuprojekt (10%)

## Nõutav tarkvara

- Git
- Docker Desktop
- Ansible
- Terraform
- kubectl ja minikube
- VSCode või muu koodiredaktor
- VirtualBox ja Vagrant

## Soovituslik kirjandus

- Pro Git (Scott Chacon, Ben Straub)
- Ansible for DevOps (Jeff Geerling)
- Docker in Practice (Ian Miell, Aidan Hobson Sayers)
- Terraform: Up and Running (Yevgeniy Brikman)
- Kubernetes in Action (Marko Lukša)

---

**Õppejõud:** Maria Talvik  
**Kontakt:** [lisa email või kontaktinfo]