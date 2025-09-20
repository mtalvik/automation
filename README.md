# Automatiseerimise Kursus

**ITS-24 Täiskasvanute klass - 34 tundi, 8 moodulit**

[![Deploy to GitHub Pages](https://github.com/your-username/automation-course/workflows/Deploy%20to%20GitHub%20Pages/badge.svg)](https://github.com/your-username/automation-course/actions)
[![Website](https://img.shields.io/badge/website-live-brightgreen)](https://your-username.github.io/automation-course)

---

## Kursuse Ülevaade

See kursus tutvustab kaasaegseid automatiseerimise tööriistu ja DevOps praktikaid. Õpite kasutama tööstuse standardeid ja parimaid praktikaid automatiseerimiseks.

### Mida õpite?

- **Git** - Versioonihaldus ja meeskonnatöö
- **Ansible** - Konfiguratsiooni haldamine
- **Docker** - Konteineriseerimine
- **Terraform** - Infrastructure as Code
- **Kubernetes** - Konteinerite orkestreerimine
- **CI/CD** - Pidev integratsioon ja juurutamine

---

## Veebileht

Kursuse materjalid on saadaval veebilehel: **[https://your-username.github.io/automation-course](https://your-username.github.io/automation-course)**

---

## Struktuur

```
automation-course/
├── docs/                          # MkDocs dokumentatsioon
│   ├── index.md                   # Avaleht
│   ├── curriculum.md              # Kursuse ülevaade
│   └── [module_name]/             # Iga mooduli materjalid
│       ├── lecture.md             # Loengumaterjal
│       ├── lab.md                 # Laboriharjutused
│       ├── homework.md            # Kodutöö ülesanded
│       └── reading_materials.md   # Lugemismaterjal
├── teacher_repo/                  # Õppejõu materjalid (privaatne)
├── mkdocs.yml                     # MkDocs konfiguratsioon
├── requirements.txt               # Python sõltuvused
└── .github/workflows/             # GitHub Actions
    └── deploy.yml                 # Automaatne juurutamine
```

---

## Kohalik Seadistamine

### Eeltingimused

- Python 3.8+
- Git
- Veebibrauser

### Installimine

1. **Klooni repositoorium:**
   ```bash
   git clone https://github.com/your-username/automation-course.git
   cd automation-course
   ```

2. **Installi sõltuvused:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Käivita kohalik server:**
   ```bash
   mkdocs serve
   ```

4. **Ava brauseris:** `http://127.0.0.1:8000`

---

## Moodulid

| Moodul | Teema | Kontaktaeg | Link |
|--------|-------|------------|------|
| 1 | Git Versioonihaldus | 4h | [Materjalid](docs/git_version_control/) |
| 2 | Ansible Alused | 4h | [Materjalid](docs/ansible_basics/) |
| 3 | Docker Alused | 4h | [Materjalid](docs/docker_fundamentals/) |
| 4 | Docker Orkestratsioon | 4h | [Materjalid](docs/docker_orchestration/) |
| 5 | Ansible Edasijõudnud | Iseseisvad Labored | [Materjalid](docs/ansible_advanced/) |
| 6 | Ansible Rollid | Iseseisvad Labored | [Materjalid](docs/ansible_roles/) |
| 7 | Terraform Alused | 2h | [Materjalid](docs/terraform_basics/) |
| 8 | CI/CD + Kubernetes | 2h | [Materjalid](docs/ci_cd_advanced/) |

---

## Arendamine

### MkDocs Konfiguratsioon

- **Teema:** Material for MkDocs
- **Keel:** Eesti
- **Funktsioonid:** Otsing, navigatsioon, süntaksi esiletõstmine
- **Plugins:** Git revision date, minify, search

### Kohalik Arendamine

```bash
# Install development dependencies
pip install -r requirements.txt

# Start development server
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages (manual)
mkdocs gh-deploy
```

---

## Juurutamine

Kursuse veebileht juurutatakse automaatselt GitHub Actions abil:

1. **Push** `main` haru
2. **GitHub Actions** ehitab MkDocs lehe
3. **GitHub Pages** avaldab lehe

### Manuaalne Juurutamine

```bash
mkdocs gh-deploy
```

---

## Kaastöö

1. **Fork** repositoorium
2. **Loo** feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** muudatused (`git commit -m 'Add amazing feature'`)
4. **Push** haru (`git push origin feature/amazing-feature`)
5. **Ava** Pull Request

---

## Kontakt

- **Õppejõud:** Maria Talvik
- **Email:** [your-email@example.com]
- **GitHub:** [@your-username](https://github.com/your-username)

---

## Litsents

See projekt on litsentseeritud MIT litsentsi all - vaata [LICENSE](LICENSE) faili detaile.

---

## Tänud

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Dokumentatsiooni teema
- [GitHub Pages](https://pages.github.com/) - Veebilehe hostimine
- [GitHub Actions](https://github.com/features/actions) - CI/CD

---

**Edu õppimisel!**
# automation
