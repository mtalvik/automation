# IT automatiseerimise kursus

Serverite ja rakenduste automatiseerimine - Git'ist Kubernetes'eni.

[Veebileht](https://mtalvik.github.io/automation) | [Discord](https://discord.gg/qXEjUGJKAF)

## Teemad

- Git versioonihaldus ja meeskonnatöö
- Docker konteinerid ja orkestratsioon
- Ansible automatiseerimine ja rollid  
- CI/CD torujuhtmed
- Kubernetes orkestreerimine
- Terraform infrastruktuur koodina

## Kohalik seadistamine

```bash
git clone https://github.com/mtalvik/automation.git
cd automation
pip install -r requirements.txt
mkdocs serve
```

Ava brauser: http://127.0.0.1:8000

## Ajakava

| Nädalad | Teema |
|---------|-------|
| 9 | Git põhitõed |
| 10-11 | Docker konteinerid |  
| 12 | Docker Compose |
| 13-14 | Ansible alused |
| 15 | Ansible rollid |
| 16-18 | CI/CD ja GitHub Actions |
| 19-20 | Kubernetes |
| 21-22 | Terraform |

## Struktuur

```
docs/
├── index.md                    # Avaleht
├── curriculum.md               # Õppekava
├── git_version_control/        # Git moodul
├── docker_fundamentals/        # Docker alused
├── docker_orchestration/       # Docker Compose
├── ansible_basics/             # Ansible alused  
├── ansible_advanced/           # Ansible edasijõudnud
├── ansible_roles/              # Ansible rollid
├── terraform_basics/           # Terraform
└── ci_cd_advanced/             # CI/CD + Kubernetes
```

Iga moodul sisaldab:
- `lecture.md` - teooria
- `lab.md` - praktikum  
- `homework.md` - kodutöö

## Publitseerimine

```bash
mkdocs gh-deploy
```

Automaatne juurutamine GitHub Actions'iga peale iga push'i.

## Kontakt

Maria Talvik | maria.talvik@taltech.ee | ITI0302

---

MIT litsents
```

**Fixed:**
- Removed corporate buzzwords and AI patterns
- Simplified structure explanations
- Used actual Discord link
- Removed fake badges and placeholder URLs
- Made it concise and to-the-point
- Removed unnecessary sections like "contribution guidelines"

Much more readable and human!
