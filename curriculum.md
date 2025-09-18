# 📚 Automatiseerimise Kursuse Õppekava

**ITS-24 - Täiskasvanute klass (34 tundi, 8 moodulit)**

---

## 📋 Kursuse Ülevaade

See kursus katab olulisi automatiseerimise tööriistu ja praktikaid kaasaegsetes DevOps töövoogudes. Iga moodul sisaldab 4 tundi kontaktõpet ning struktureeritud kodutöid.

---

## 📊 Kursuse Struktuur

| Moodul | Teema | Kontaktaeg | Kodutöö Ülesanne 1 | Kodutöö Ülesanne 2 |
|--------|-------|------------|-------------------|-------------------|
| 1 | **Git Versioonihaldus** | 4h | Git projekti portfoolio näidetega | Lugemine: Git ajalugu, sisemused, edasijõudnud kontseptsioonid |
| 2 | **Ansible Alused** | 4h | Kohalik LAMP stack (VirtualBox/Vagrant) | Lugemine: Ansible arhitektuur, YAML, moodulid |
| 3 | **Docker Alused** | 4h | Mitme-rakendusega konteineriseerimise projekt | Lugemine: Docker arhitektuur, turvalisus |
| 4 | **Docker Orkestratsioon** | 4h | Täispinu kohalik paigaldus | Lugemine: Konteinerite orkestreerimise mustrid |
| 5 | **Ansible Edasijõudnud** | **Iseseisvad Labored** | Edasijõudnud funktsioonide laboriharjutused | Lugemine: Jinja2, muutujad, Ansible Vault |
| 6 | **Ansible Rollid** | **Iseseisvad Labored** | Rolli loomise labor + Puppet võrdlus | Lugemine: Rollide parimad praktikad, Galaxy |
| 7 | **Terraform Alused** | 2h | Kohalik infrastruktuur (failid, konfiguratsioon) | Lugemine: IaC põhimõtted, Terraform mustrid |
| 8 | **CI/CD + Kubernetes** | 2h | Täielik pipeline + K8s ülevaade (kohalik minikube) | Lugemine: GitOps, Kubernetes, produktsioon |

---

## 🎯 Moodulite Detailid

### **Moodul 1: Git Versioonihaldus (4h)**

**Kontaktaja Struktuur:**
- Git kontseptsioonid ja töövoog (1h)
- Põhilised käsud praktikas (1h)
- GitHub koostöö (1h)
- Harude loomine ja ühendamine praktikas (1h)
- **Boonus:** Edasijõudnud Git funktsioonid (hooks, submodules, kohandatud käsud)

**Käsitletud Teemad:**
- Git alused ja versioonihalduse põhimõtted
- Kohalik Git kasutamine ja põhilised käsud
- GitHub ja kaugrepositooriumid
- Meeskonnatöö ja Pull Request'id

**Kodutööd:**
- **Ülesanne 1:** Täielik Git projekti portfoolio harude töövooga
- **Ülesanne 2:** Loe Git ajalugu, sisemusi ja edasijõudnud kontseptsioone (2-3 tundi)

---

### **Moodul 2: Ansible Alused (4h)**

**Kontaktaja Struktuur:**
- Ansible arhitektuuri ülevaade (30 min)
- Kohalik VM seadistus Vagrant'iga (30 min)
- SSH seadistus ja inventory (1h)
- Ad-hoc käskude praktika (1h)
- Esimese playbook'i loomine (1h)
- **Boonus:** Edasijõudnud playbook'id, veakkäsitlemine, kohandatud moodulid

**Käsitletud Teemad:**
- Ansible arhitektuur ja SSH konfiguratsioon
- Kohalik testimine Vagrant/VirtualBox'iga
- Inventory haldamine ja ad-hoc käsud
- YAML süntaks ja põhilised playbook'id
- Esimesed automatiseerimise töövood

**Kodutööd:**
- **Ülesanne 1:** Paigalda LAMP stack kohalikult Vagrant VM'idega + palju näiteid
- **Ülesanne 2:** Loe Ansible arhitektuur, YAML ja moodulite ökosüsteem (2-3 tundi)

---

### **Moodul 3: Docker Alused (4h)**

**Kontaktaja Struktuur:**
- Konteinerite kontseptsioonid vs VM'id (30 min)
- Docker'i installimine ja esimene konteiner (1h)
- Dockerfile'i loomise töötuba (1.5h)
- Põhiline võrgustik ja helitugevused (1h)
- **Boonus:** Mitme-etapiline ehitus, turvalisus, edasijõudnud võrgustik

**Käsitletud Teemad:**
- Konteineritehnoloogia ülevaade
- Docker'i installimine ja põhilised käsud
- Dockerfile'i loomine ja parimad praktikad
- Docker'i võrgustik ja helitugevused

**Kodutööd:**
- **Ülesanne 1:** Konteineriseeri mitu rakendust paljude näidetega
- **Ülesanne 2:** Loe Docker'i arhitektuur, turvalisus ja parimad praktikad (2-3 tundi)

---

### **Moodul 4: Docker Orkestratsioon (4h)**

**Kontaktaja Struktuur:**
- Mitme-konteineriga kontseptsioonid (30 min)
- Compose faili loomine (1.5h)
- Mitme-teenusega rakenduse seadistus (1.5h)
- Kohalik orkestratsioon näidetega (30 min)

**Käsitletud Teemad:**
- Docker Compose süntaks ja kasutamine
- Mitme-konteineriga rakendused
- Keskkonna-spetsiifilised konfiguratsioonid
- Kohalikud arenduse töövood

**Kodutööd:**
- **Ülesanne 1:** Paigalda full-stack rakendus kohalikult paljude teenuste näidetega
- **Ülesanne 2:** Loe konteinerite orkestreerimise mustreid ja strateegiaid (2-3 tundi)

---

### **Moodul 5: Ansible Edasijõudnud (Iseseisvad Labored)**

**Iseseisva Labori Struktuur:**
- Juhendatud harjutused samm-sammuliste juhistega
- Muutujate ja Jinja2 mallide labor
- Käsitlejate ja veakäsitlemise labor
- Ansible Vault turvalisuse labor
- Mitmesugused praktilised näited

**Käsitletud Teemad:**
- Muutujad ja Jinja2 mallid
- Käsitlejad ja veakäsitlemise strateegiad
- Ansible Vault saladuste haldamiseks
- Parimad praktikad ja optimeerimine

**Kodutööd:**
- **Ülesanne 1:** Lõpeta kõik iseseisva labori harjutused näidetega
- **Ülesanne 2:** Loe Jinja2 mallid, muutujad ja Vault turvalisus (2-3 tundi)

---

### **Moodul 6: Ansible Rollid (Iseseisvad Labored)**

**Iseseisva Labori Struktuur:**
- Rolli loomise samm-sammuline juhend
- Rolli muutujate ja sõltuvuste labor
- Ansible Galaxy uurimine
- Puppet vs Ansible võrdlusharjutus

**Käsitletud Teemad:**
- Ansible rollide struktuur ja parimad praktikad
- Rolli muutujad ja sõltuvused
- Ansible Galaxy kogukond
- Konfiguratsiooni haldamise võrdlus

**Kodutööd:**
- **Ülesanne 1:** Loo roll + Puppet võrdlus paljude näidetega
- **Ülesanne 2:** Loe rolli parimaid praktikaid ja Galaxy ökosüsteemi (2-3 tundi)

---

### **Moodul 7: Terraform Alused (2h Kontaktõpe)**

**Kontaktaja Struktuur:**
- Infrastructure as Code ülevaade (30 min)
- Kohalik Terraform demo (failisüsteemi haldamine) (1h)
- Praktiline: Loo kohalik infrastruktuur (30 min)
- **Boonus:** Moodulid, tööruumid, edasijõudnud mallid

**Käsitletud Teemad:**
- Terraform alused ja HCL keel
- Kohalikud providerid (failisüsteemi haldamine)
- State'i haldamise kontseptsioonid
- Infrastructure as Code põhimõtted

**Kodutööd:**
- **Ülesanne 1:** Kohalik infrastruktuuriprojekt (failid, konfiguratsioon, skriptid) paljude näidetega
- **Ülesanne 2:** Loe IaC põhimõtteid ja Terraform mustreid (2-3 tundi)

---

### **Moodul 8: CI/CD + Kubernetes (2h Kontaktõpe)**

**Kontaktaja Struktuur:**
- Täieliku automatiseerimise pipeline demo (1h)
- Kubernetes ülevaade kohaliku minikube'iga (30 min)
- Kõigi tööriistade integratsioon (30 min)

**Käsitletud Teemad:**
- GitHub Actions eelnevate tööriistadega
- Täielik automatiseerimise töövoog
- Kubernetes tutvustus (kohalik)
- DevOps pipeline integratsioon

**Kodutööd:**
- **Ülesanne 1:** Täielik automatiseerimise projekt kõigi tööriistade integratsiooniga + näited
- **Ülesanne 2:** Loe GitOps, Kubernetes ja produktsiooni mustreid (2-3 tundi)

---

## 📁 Failide Struktuur

### Iga Moodul Sisaldab:
```
modul_nimi/
├── lecture.md              # Peamine loengumaterjal
├── lab.md                  # Praktilised harjutused
├── homework.md             # Praktiline ülesanne (Ülesanne 1)
└── reading_materials.md    # Teooria ja taust (Ülesanne 2)
```

### Võrdlusmaterjal (kui rakendatav):
```
modul_nimi/
├── reference/              # Kiired viited ja juhendid
└── examples/               # Koodinäited ja mallid
```

---

## 🎯 Õpieesmärgid

- **Praktiline kogemus** kõigi automatiseerimise tööriistadega
- **Projektipõhise õppimise** lähenemine
- **Meeskonnatöö** oskused
- **Tööstuse standardid** ja parimad praktikad
- **Iseseisev õppimine** lugemiülesannete kaudu

---

## 📝 Hindamisstrateegia

- **Ülesanne 1:** Praktiline töö (hinnatakse funktsionaalsuse järgi)
- **Ülesanne 2:** Lugemise refleksioon (hinnatakse mõistmise järgi)
- **Portfoolio:** GitHub repositoorium kogu tööga
- **Lõpuprojekt:** Kõigi tööriistade integratsioon

---

## 🔧 Seadistamise Juhendid

### **Enne kursuse alustamist:**
- **Windows kasutajad:** [Windows Seadistamise Juhend](WINDOWS_SETUP_GUIDE.md)
- **Linux/macOS kasutajad:** [Kodu Masina Ehitus Juhend](docker_orchestration/kodu_masina_ehitus_juhend.md)

### **Vajalikud tööriistad:**
- Git (versioonihaldus)
- Docker Desktop (konteinerid)
- Ansible (konfiguratsiooni haldamine)
- Terraform (infrastruktuuri kood)
- kubectl + Minikube (Kubernetes)
- VSCode (arenduskeskkond)