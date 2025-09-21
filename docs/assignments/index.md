# Ülesanded - Infrastructure Automation

Tere tulemast infrastruktuuri automatiseerimise kursuse ülesannete lehele! Siin leiad kõik praktilised ülesanded DevOps tööriistade kohta.

## Kursuse ülesehitus

Kursus koosneb 6 peamisest moodulist:

1. **Git & Versioonihaldus** - Alus kõigele
2. **Docker & Konteineriseerimine** - Rakenduste pakkimine
3. **Ansible & Configuration Management** - Infrastruktuuri automatiseerimine
4. **CI/CD & GitHub Actions** - Pidev integratsioon ja tarnimine
5. **Kubernetes** - Konteinerite orkestreerimine
6. **Terraform** - Infrastructure as Code

## Aktiivsed ülesanded

### Moodul 1: Git & Versioonihaldus
**[Rain Pickles Website](../git_version_control/homework.md)**
- Versioonihaldus veebilehe jaoks
- Branching, merging, konfliktide lahendamine
- **Tähtaeg:** Nädal 9

### Moodul 2: Docker
**[Multi-Container Application](../docker_fundamentals/homework.md)**
- Dockerize veebirakendus
- Docker Compose kasutamine
- **Tähtaeg:** Nädal 12

### Moodul 3: Ansible
**[NGINX + SSL + PostgreSQL](classroom.md#nadal-13-15-ansible-automation)**
- Automatiseeri LAMP stack
- SSL sertifikaadid, andmebaas
- **Tähtaeg:** Nädal 15

### Moodul 4: CI/CD
**[GitHub Actions Pipeline](../ci_cd_advanced/homework.md)**
- Automated testing
- Docker build & push
- **Tähtaeg:** Nädal 19

### Moodul 5: Kubernetes
**[3-Tier App Deploy](../kubernetes_overview/homework.md)**
- Deploy frontend, backend, database
- Services, ConfigMaps, Secrets
- **Tähtaeg:** Nädal 21

### Moodul 6: Terraform
**[Terraform Põhitõed](../terraform_basics/homework1.md)** | **[Terraform Moodulid](../terraform_basics/homework2.md)**
- VPC, EC2, RDS provisioning
- State management
- **Tähtaeg:** Nädal 23

## Hindamissüsteem

### Ülesannete kaalud
- **Git:** 10%
- **Docker:** 15%
- **Ansible:** 20%
- **CI/CD:** 15%
- **Kubernetes:** 20%
- **Terraform:** 20%

### Hindamiskriteeriumid
- **Funktsionaalsus:** Kas lahendus töötab?
- **Best Practices:** Kas järgitud parimaid praktikaid?
- **Dokumentatsioon:** README, kommentaarid
- **Automatiseerimine:** Idempotency, error handling

## 🏠 Kodulabori seadistamine

### Option 1: Vagrant + VirtualBox
```bash
vagrant init ubuntu/focal64
vagrant up
vagrant ssh
```

### Option 2: Docker Desktop
- Windows/Mac: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Linux: Docker Engine + Docker Compose

### Option 3: Cloud (tasuta)
- AWS Free Tier (12 kuud)
- Azure Student Account
- Google Cloud Free Credits

## 🛠 Vajalikud tööriistad

```bash
# Paigalda kõik korraga (Ubuntu/Debian)
sudo apt update
sudo apt install -y git docker.io ansible terraform kubectl

# Mac (Homebrew)
brew install git docker ansible terraform kubectl
```

## ⚡ Quick Links

- [🎓 GitHub Classroom](classroom.md) - Automatiseeritud ülesanded
- [Leaderboard](leaderboard.md) - Tulemuste tabel
- [Discussions](https://github.com/mtalvik/automation/discussions) - Küsi abi
- [📖 Materjalid](../ansible_basics/reading_materials.md) - Lisalugemine

## Abi ja tugi

### Kui jääd hätta:
1. **Vaata lecture materjale** - Iga mooduli `lecture.md`
2. **Proovi lab ülesandeid** - Iga mooduli `lab.md`
3. **Vaata näidiskoode** - `teacher_repo/` kaustas
4. **Küsi abi** - GitHub Discussions või praktikumis

### Sage vead:
- **Permission denied** → Kasuta `sudo` või kontrolli õigusi
- **Connection refused** → Kontrolli firewall/ports
- **Module not found** → Paigalda puuduvad sõltuvused
- **Timeout** → Suurenda timeout väärtusi

## Gamification & Achievements

Teeni badge'e:
- **Speed Demon** - Esita ülesanne 24h jooksul
- **Security First** - Implementeeri SSL/TLS õigesti
- **Container Master** - Docker multi-stage build < 100MB
-  **CI/CD Hero** - 0 failed pipeline runs
- **K8s Navigator** - Deploy ilma kubectl edit'ita
- **Terraform Architect** - 0 drift detected

---

**Pro tip:** Alusta varakult, testi lokaalses keskkonnas, automatiseeri kõik mis võimalik!

**Remember:** It's not about doing it perfectly the first time, it's about iterating and improving!
