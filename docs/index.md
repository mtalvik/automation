# 🚀 Automatiseerimine ja Konfiguratsioonihaldus

!!! success "ITI8560 - Kevad 2025"
    **Õppejõud:** Maria Talvik  
    **Keel:** Eesti  
    **Maht:** 6 EAP  
    **Toimumisaeg:** Teisipäeviti 18:00-21:00

## 🎯 Mida Sa Õpid?

<div class="grid cards" markdown>

-   :material-git:{ .lg .middle } **Versioonihaldus**

    ---

    Git, GitHub, branching strategies ja collaboration workflows

    [:octicons-arrow-right-24: Alusta siit](git_version_control/lecture.md)

-   :material-docker:{ .lg .middle } **Konteineriseerimine**

    ---

    Docker, Docker Compose, container orchestration

    [:octicons-arrow-right-24: Õpi Docker](docker_fundamentals/lecture.md)

-   :material-ansible:{ .lg .middle } **Automatiseerimine**

    ---

    Ansible playbooks, roles, inventory management

    [:octicons-arrow-right-24: Automatiseeri](ansible_basics/lecture.md)

-   :material-kubernetes:{ .lg .middle } **Orkestreerimine**

    ---

    Kubernetes, pods, services, deployments

    [:octicons-arrow-right-24: K8s alused](kubernetes_overview/lecture.md)

</div>

## ⚡ Quick Start

=== "1️⃣ Setup"

    ```bash
    # Klooni kursuse repo
    git clone https://github.com/mtalvik/automation.git
    cd automation
    
    # Installi Python deps
    pip install -r requirements.txt
    
    # Käivita lokaalne server
    mkdocs serve
    ```

=== "2️⃣ Join"

    1. **GitHub Classroom**  
       [![Join Classroom](https://img.shields.io/badge/Join-GitHub%20Classroom-blue?style=for-the-badge&logo=github)](https://classroom.github.com/classrooms/xxx)
    
    2. **Discord Server**  
       [![Discord](https://img.shields.io/discord/xxx?label=Discord&logo=discord&style=for-the-badge)](https://discord.gg/xxx)
    
    3. **Discussions**  
       [![Discussions](https://img.shields.io/github/discussions/mtalvik/automation?style=for-the-badge)](https://github.com/mtalvik/automation/discussions)

=== "3️⃣ First Task"

    ```python
    # Sinu esimene automatiseerimine
    import subprocess
    
    def hello_automation():
        """Tervita automatiseerimise maailma!"""
        subprocess.run(["echo", "Hello, Automation! 🤖"])
        
    if __name__ == "__main__":
        hello_automation()
    ```

## 📅 Ajakava

| Nädal | Kuupäev | Teema | Praktikum | Kodutöö |
|-------|---------|-------|-----------|---------|
| **1** | 28.01 | [Git & GitHub](git_version_control/lecture.md) | [Setup & Basics](git_version_control/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](git_version_control/homework.md) |
| **2** | 04.02 | [Docker Fundamentals](docker_fundamentals/lecture.md) | [Containers](docker_fundamentals/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](docker_fundamentals/homework.md) |
| **3** | 11.02 | [Docker Compose](docker_orchestration/lecture.md) | [Multi-container](docker_orchestration/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](docker_orchestration/homework.md) |
| **4** | 18.02 | [Ansible Basics](ansible_basics/lecture.md) | [Playbooks](ansible_basics/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](ansible_basics/homework.md) |
| **5** | 25.02 | [Ansible Roles](ansible_roles/lecture.md) | [Role Creation](ansible_roles/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](ansible_roles/homework.md) |
| **6** | 04.03 | [CI/CD](ci_cd_advanced/lecture.md) | [GitHub Actions](ci_cd_advanced/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](ci_cd_advanced/homework.md) |
| **7** | 11.03 | **Vaheaeg** | - | - |
| **8** | 18.03 | [Kubernetes](kubernetes_overview/lecture.md) | [K8s Deploy](kubernetes_overview/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](kubernetes_overview/homework.md) |
| **9** | 25.03 | [Terraform](terraform_basics/lecture.md) | [IaC](terraform_basics/lab.md) | [![Start](https://img.shields.io/badge/Start-blue)](terraform_basics/homework.md) |
| **10** | 01.04 | **Projekt** | Mentoring | Work on Project |

## 🏆 Leaderboard

<div id="leaderboard-container">
    <loading>Laadin...</loading>
</div>

<script>
// Fetch GitHub Classroom data
fetch('https://api.github.com/repos/mtalvik/automation/issues?labels=completed&state=all')
  .then(response => response.json())
  .then(data => {
    const leaderboard = {};
    data.forEach(issue => {
      const user = issue.user.login;
      leaderboard[user] = (leaderboard[user] || 0) + 1;
    });
    
    const sorted = Object.entries(leaderboard)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5);
    
    let html = '<table><thead><tr><th>Koht</th><th>Nimi</th><th>Punktid</th></tr></thead><tbody>';
    sorted.forEach((entry, index) => {
      const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : `${index + 1}.`;
      html += `<tr><td>${medal}</td><td>${entry[0]}</td><td>${entry[1]}</td></tr>`;
    });
    html += '</tbody></table>';
    
    document.getElementById('leaderboard-container').innerHTML = html;
  })
  .catch(err => {
    document.getElementById('leaderboard-container').innerHTML = '<p>Leaderboard tuleb varsti!</p>';
  });
</script>

## 💬 Community & Support

<div class="grid" markdown>

:material-forum: **Discussions**  
Küsi küsimusi ja jaga ideid  
[GitHub Discussions →](https://github.com/mtalvik/automation/discussions)

:material-discord: **Discord**  
Real-time chat ja abi  
[Join Discord →](https://discord.gg/xxx)

:material-email: **Email**  
maria.talvik@tlu.ee  
[Saada email →](mailto:maria.talvik@tlu.ee)

:material-calendar: **Konsultatsioon**  
Kolmapäeviti 16:00-17:00  
[Broneeri aeg →](https://calendly.com/maria-talvik)

</div>

## 🎓 Hindamine

<div class="progress-bars" markdown>

- **Praktikumid** - 30%
- **Kodutööd** - 30%  
- **Projekt** - 30%
- **Osalemine** - 10%

</div>

!!! tip "Pro Tip"
    Kasuta GitHub Copilot'i tasuta õpilastele! [GitHub Student Pack →](https://education.github.com/pack)

## 📚 Soovitatud Lugemine

- [The Phoenix Project](https://www.goodreads.com/book/show/17255186-the-phoenix-project) - DevOps romaan
- [Docker Deep Dive](https://www.goodreads.com/book/show/36411996-docker-deep-dive) - Nigel Poulton
- [Ansible for DevOps](https://www.ansiblefordevops.com/) - Jeff Geerling
- [Kubernetes in Action](https://www.manning.com/books/kubernetes-in-action) - Marko Lukša

---

!!! question "Küsimused?"
    Kui jääd hätta, vaata [FAQ](faq.md) või küsi [Discordis](https://discord.gg/xxx)!
