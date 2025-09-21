# Ansible lugemismaterjalid (Kodutöö ülesanne 2)

**Eeldatav lugemisaeg:** 2-3 tundi  
**Tähtaeg:** Enne järgmist tundi

---

## Kohustuslik lugemine (1,5 tundi)

#### Ansible arhitektuuri süvaanalüüs
**Allikas:** Ansible dokumentatsioon ja arhitektuuri juhend

**Põhiteemad:**
- Agentless arhitektuur ja selle eelised
- Control node vs hallatavad sõlmed
- SSH-põhine kommunikatsioon
- Ansible'i täitmismudel
- Inventory haldamise kontseptsioonid

**Lugemisküsimused:**
- Miks kasutab Ansible agentless arhitektuuri?
- Millised on agentless vs agent-põhiste süsteemide eelised ja puudused?
- Kuidas käsitleb Ansible autentimist ja autoriseerimist?
- Mis juhtub Ansible playbook'i täitmise ajal?

#### YAML süntaks ja parimad praktikad
**Allikas:** YAML dokumentatsioon ja Ansible stiili juhend

**Põhiteemad:**
- YAML andmetüübid ja struktuurid
- Taandrimise ja vormindamise reeglid
- Ansible-spetsiifilised YAML konventsioonid
- Levinud YAML lõksud ja kuidas neid vältida
- YAML valideerimise tööriistad

**Lugemisküsimused:**
- Millised on peamised erinevused YAML'i ja JSON'i vahel?
- Miks on taandrimine YAML'is nii oluline?
- Millised on levinud YAML süntaksivead?
- Kuidas saab YAML süntaksit valideerida?

#### Ansible moodulite ökosüsteem
**Allikas:** Ansible moodulite dokumentatsioon

**Põhiteemad:**
- Põhimoodulid vs kogukonna moodulid
- Moodulite kategooriad (süsteem, võrk, pilv jne)
- Mooduli parameetrid ja tagastusväärtused
- Idempotentsus Ansible moodulites
- Kohandatud moodulite arendamise alused

**Lugemisküsimused:**
- Mis teeb moodulist "idempotentse"?
- Kuidas leida ülesandele õige moodul?
- Mis vahe on põhi- ja kogukonna moodulitel?
- Millal võib vaja minna kohandatud moodulit?

---

## Valikuline lugemine (1 tund)

#### Ansible parimad praktikad
**Allikas:** Ansible parimate praktikate juhend

**Põhiteemad:**
- Playbook'i organisatsioon ja struktuur
- Muutujate nimetamise konventsioonid
- Vigade käsitlemise strateegiad
- Jõudluse optimeerimise tehnikad
- Turvalisuse kaalutlused

#### Ansible vs muud konfiguratsioonihalduse tööriistad
**Allikas:** Tööstuse võrdlused ja dokumentatsioon

**Põhiteemad:**
- Ansible vs Puppet vs Chef vs Salt
- Iga tööriista kasutusjuhud
- Õppimiskõvera võrdlused
- Kogukonna ja ökosüsteemi erinevused
- Millal valida Ansible alternatiivide asemel

---

## Viitematerjalid (hoidke käepärast)

### Ansible käskude kiirülevaade
```bash
# Põhikäsud
ansible --version              # Kontrolli Ansible versiooni
ansible all -m ping            # Testi ühenduvust kõigi hostidega
ansible all -m setup           # Kogu fakte kõigist hostidest
ansible-playbook playbook.yml  # Käivita playbook

# Inventory haldamine
ansible-inventory --list       # Näita inventory struktuuri
ansible-inventory --graph      # Näita inventory graafiliselt

# Ad-hoc käsud
ansible webservers -m copy -a "src=/local/file dest=/remote/file"
ansible dbservers -m service -a "name=mysql state=started"
ansible all -m shell -a "uptime"
```

### Levinud YAML mustrid Ansible'is
```yaml
# Põhiline playbook'i struktuur
---
- name: Näidis playbook
  hosts: webservers
  become: yes
  vars:
    app_name: myapp
    app_port: 8080
  
  tasks:
    - name: Installi paketid
      apt:
        name: "{{ item }}"
        state: present
      loop:
        - nginx
        - python3
        - git
    
    - name: Käivita teenus
      service:
        name: nginx
        state: started
        enabled: yes
```

### Ansible faktid ja muutujad
```yaml
# Faktide kasutamine
- name: Kuva süsteemi info
  debug:
    msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"

# Kohandatud muutujad
- name: Seadista kohandatud muutuja
  set_fact:
    app_path: "/opt/{{ app_name }}"

# Muutujate prioriteedid
## extra vars (käsurida)
## task vars
## block vars
## role ja include vars
## play vars
## host faktid
## host vars
## group vars
## inventory vars
## role defaults
```

---

## Lugemise refleksioon ülesanne

Pärast lugemise lõpetamist esitage lühike refleksioon (200-300 sõna), mis katab:

1. **Peamised avastused:** Mis oli Ansible'i kohta kõige üllatavam või olulisem, mida õppisite?
2. **Küsimused:** Millised Ansible kontseptsioonid on veel ebaselged või vajavad rohkem selgitust?
3. **Rakendamine:** Kuidas arvate, et Ansible'i agentless arhitektuur aitab teie automatiseerimistööd?
4. **Edasine õppimine:** Milliseid Ansible teemasid sooviksite rohkem uurida?

**Esitamise formaat:** Lisage oma GitHub repositooriumisse failina `ansible_basics_reading_reflection.md`

---

## 🔗 Lisamaterjalid

- [Ansible dokumentatsioon](https://docs.ansible.com/)
- [Ansible parimad praktikad](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible moodulite indeks](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)
- [YAML dokumentatsioon](https://yaml.org/spec/)
- [Ansible Galaxy](https://galaxy.ansible.com/)

---

## Märkused järgmiseks tunniks

Tulge valmistatud:
- Küsimustega lugemisest
- Mis tahes Ansible stsenaariumidega, mida soovite harjutada
- Ideedega oma Ansible automatiseerimisprojektile
- YAML süntaksi ja struktuuri mõistmisega