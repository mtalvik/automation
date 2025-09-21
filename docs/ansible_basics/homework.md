# LAMP Stack Playbook

**Tähtaeg:** Järgmise nädala alguseks  
**Eesmärk:** Õppida Ansible playbook'i loomist praktiliselt ja iseseisvalt  
lahendamist ja uurimist

---

## Ülesande kirjeldus

See kodutöö ei anna valmis koodi - see annab probleemid lahendamiseks! Kasutage lab'is õpitud oskusi ja Ansible dokumentatsiooni, et ehitada LAMP stack samm-sammult.

**Põhimõte:** Igal sammul antakse ülesanne, kontrollviis ja nõuanded. Kood peate ise kirjutama!

---

## Task 1: Projekti seadistamine (enne alustamist)

### Ülesanne 1.1: Looge projekti struktuur

**Mida vaja teha:**
Looge järgmine kataloogide ja failide struktuur (kasutage `mkdir` ja `touch` käske):

```
ansible-lamp/
├── inventory/
│   └── hosts.yml
├── group_vars/
│   └── webservers.yml  
├── templates/
│   ├── (failid lisate hiljem)
├── lamp-stack.yml
├── ansible.cfg
└── README.md
```

**Kontroll:** `tree ansible-lamp` peaks näitama õiget struktuuri

** Küsimus:** Miks kasutame group_vars/ kausta? (Vastake README.md'sse)

---

## Task 2: Inventory seadistamine

### Ülesanne 1.1: Inventory fail

**Probleem:** Vajate inventory faili, mis töötab nii localhost'iga kui ka teise serveriga.

**Nõuded:**
- Looge YAML formaat inventory (kasutage lab'is õpitut)
- Gruppi nimi: `webservers`
- Localhost peab kasutama `ansible_connection: local`
- Jätke kommentaaridesse näide teise serveri lisamiseks

**Fail:** `inventory/hosts.yml`

**Kontroll:** `ansible-inventory --list` peaks näitama teie servereid

** Uurige:** Käivitage `ansible webservers -m ping` - kas töötab?

---

### Ülesanne 1.2: Muutujate defineerimine

**Probleem:** LAMP stack vajab palju konfiguratsiooni. Kus muutujaid hoida?

**Nõuded:** Looge `group_vars/webservers.yml` ja defineerige:
- MySQL root parool
- Rakenduse andmebaasi nimi  
- Rakenduse kasutaja nimi ja parool
- PHP pakettide loend
- Document root tee
- Rakenduse nimi ja versioon

** Näpunäide:** Vaadake lab'i näiteid muutujate kohta

** Mõelge:** Millised muutujad peaksid olema "salajased"? Kuidas neid hiljem kaitsta?

**Kontroll:** `ansible webservers -m debug -a "var=hostvars[inventory_hostname]"` - kas näete oma muutujaid?

---

## Task 3: Vigane playbook parandamine

### Ülesanne 2.1: Parandage see vigane playbook

**Antud on vigane playbook algus. Leidke ja parandage vead:**

```yaml
---
- name: LAMP Stack Setup
  hosts: all                    # <- VIGA 1: vale grupp
  become: true
  
  tasks:
    - name: Update cache
      package:
        update_cache: true      # <- VIGA 2: vale moodul
        
    - name: Install Apache
      apt:
        name: apache            # <- VIGA 3: vale paketi nimi
        state: present
      notify: restart apache
      
    - name: Start Apache
      systemd:                  # <- VIGA 4: miks mitte service?
        name: apache2
        state: started
        
  handlers:                     # <- VIGA 5: handlers vale kohas?
    - name: restart apache
      service:
        name: apache2
        state: restarted
```

**Ülesanne:** 
1. Kopeerige see kood faili `lamp-stack.yml`
2. Leidke kõik 5+ viga
3. Parandage need
4. Lisage proper YAML vormistus (`---` alguses)

**Kontroll:** `ansible-playbook --syntax-check lamp-stack.yml`

** Uurige:** Mis vahe on `package` ja `apt` moodulil? Kumb on parem?

---

## Task 4: MySQL seadistamine

### Ülesanne 3.1: MySQL installimine ja turvamine

**Probleem:** MySQL vajab spetsiaalset seadistamist. Lab'is nägite lihtsaid näiteid.

**Teie ülesanne:**
1. Installige `mysql-server` ja `python3-pymysql`
2. Käivitage MySQL teenus
3. Seadke MySQL root kasutajale parool (kasutage group_vars muutujat)
4. Looge rakenduse andmebaas
5. Looge rakenduse kasutaja õigustega ainult sellele andmebaasile

**Moodulid, mida vajate:**
- `package` või `apt`
- `service` 
- `mysql_user`
- `mysql_db`

** Nõuanded:**
- MySQL root parooli seadistamine on keeruline - uurige `login_unix_socket` parameetrit
- `mysql_user` moodul vajab `login_user` ja `login_password` parameetrit
- Kasutage `priv: "database_name.*:ALL"` õigusteks

** Uurige dokumentatsiooni:** `ansible-doc mysql_user`

**Kontroll:** 
```bash
mysql -u [teie_kasutaja] -p [teie_andmebaas] -e "SELECT 'Success!' as test;"
```

** Debugimise küsimus:** Kui MySQL ühendus ei tööta, kuidas te viga otsite?

---

## Task 5: Template'ide loomine

### Ülesanne 4.1: Puudulik PHP template

**Antud on template algus. Lõpetage see:**

**Fail:** `templates/info.php.j2`

```php
<?php
// {{ app_name }} - Info leht
// TODO: lisage kuupäev kasutades ansible muutujat

echo "<h1>{{ ??? }}</h1>";  // TODO: kasutage app_name muutujat

echo "<h2>Serveri info</h2>";
// TODO: lisage hostname, IP, OS info

echo "<h2>MySQL test</h2>";
$host = 'localhost';
$database = '{{ ??? }}';  // TODO: kasutage õiget muutujat
$username = '{{ ??? }}';  // TODO: kasutage õiget muutujat  
$password = '{{ ??? }}';  // TODO: kasutage õiget muutujat

try {
    // TODO: kirjutage PDO ühenduse test
    // Kui õnnestub, näidake "Ühendus töötab!"
    // Kui ebaõnnestub, näidake error'it
} catch(PDOException $e) {
    // TODO: error handling
}

// TODO: lisage phpinfo() kutse
?>
```

**Ülesanne:**
1. Asendage kõik `{{ ??? }}` õigete muutujatega
2. Implementeerige MySQL PDO ühenduse test
3. Lisage proper error handling
4. Lisage phpinfo() väljund

** Nõuanded:**
- Vaadake lab'i template näiteid
- Ansible faktid: `{{ ansible_hostname }}`, `{{ ansible_default_ipv4.address }}`
- PHP PDO: `new PDO("mysql:host=$host;dbname=$database", $username, $password)`

**Kontroll:** PHP ei tohi sisaldada `{{ ??? }}` märke

---

### Ülesanne 4.2: HTML põhileht loomine

**Probleem:** Vajate ilusat HTML lehte, mis näitab LAMP stack'i infot.

**Nõuded:**
- Kasutage template'i `templates/index.html.j2`
- Näidake serveri infot (hostname, OS, kuupäev)
- Lisage link `/info.php` lehele
- Kasutage CSS'i, et see oleks ilus
- Kõik info peab tulema Ansible muutujatest/faktidest

** Inspiratsioon:** Vaadake lab'i HTML näidet, aga ärge kopeerige!

** Väljakutse:** Kas oskate lisada JavaScripti, mis näitab praegust kellaaega?

**Kontroll:** HTML peab valideeruma (saate kontrollida https://validator.w3.org/)

---

## Task 6: Playbook lõpetamine

### Ülesanne 5.1: Tasks'ide implementeerimine

**Nüüd implementeerige playbook tasks'id:**

**Vajalikud sammud (kirjutage ise task'id):**
1. **Süsteemi ettevalmistus** - pakettide cache uuendamine
2. **Apache seadistamine** - installimine, käivitamine, document root loomine
3. **MySQL seadistamine** - (juba tegite Probleem 3's)
4. **PHP seadistamine** - installimine koos moodulikega
5. **Template'ide deployment** - kopeerige template'id õigetesse kohtadesse
6. **Firewall** - lubage HTTP trafik
7. **Valideerimised** - kontrollige, et kõik töötab

** Nõuanne:** Iga task vajab:
- Selget `name` välja
- Õiget moodulit
- Proper parameetreid
- Vajadusel `notify` handler'eid

**Tüüpilised moodulid:**
- `package`/`apt` - pakettide installimine
- `service` - teenuste haldamine
- `file` - kaustade loomine
- `template` - template'ide kopeerimine
- `uri` - HTTP testid
- `ufw` - firewall reeglid

** Küsimus:** Millises järjekorras task'id käivitada? Miks?

---

### Ülesanne 5.2: Handlers ja error handling

**Probleem:** Playbook peab olema robust ja käsitlema vigu.

**Nõuded:**
1. **Handlers** - Apache ja MySQL taaskäivitamise jaoks
2. **Error handling** - kasutage `failed_when`, `ignore_errors`, `retries`
3. **Valideerimised** - kontrollige teenuste olekut ja HTTP vastuseid
4. **Conditional tasks** - näiteks ainult Debian/Ubuntu süsteemides

** Näited error handling'ust:**
```yaml
- name: Test HTTP
  uri:
    url: http://localhost
  retries: 3
  delay: 10
  register: http_test
  failed_when: http_test.status != 200
```

** Mõelge:** Millal kasutada `ignore_errors: yes` ja millal mitte?

---

## Task 7: Testimine ja debugimine

### Ülesanne 6.1: Systematic testimine

**Probleem:** Kuidas te veendute, et teie playbook töötab?

**Teie testiplaan:**
1. **Syntax check** - ?
2. **Dry run** - ?  
3. **Tegelik käivitamine** - ?
4. **Manuaalne testimine** - ?
5. **Idempotency test** - ?

**Täitke küsimärgid ja tehke iga test!**

** Nõuanne:** Iga testi järel dokumenteerige tulemused

** Debugimise küsimused:**
- Kui Apache ei käivitu, kuidas te viga otsite?
- Kui MySQL ühendus ei tööta, millised logid vaatate?
- Kui template ei genereeru, kuidas te seda debugite?

---

### Ülesanne 6.2: Vigade parandamine

**Antud on levinud vead. Kas tunnete neid ära?**

**Viga 1:**
```
TASK [Install PHP] ****
fatal: [localhost]: FAILED! => {"msg": "No package matching 'php' found"}
```
**Küsimus:** Mis probleem? Kuidas parandada?

**Viga 2:**
```
TASK [Test MySQL connection] ****
fatal: [localhost]: FAILED! => {"msg": "unable to connect to database"}
```
**Küsimus:** Võimalikud põhjused? Kuidas debugida?

**Viga 3:**
```
TASK [Generate index.html] ****
fatal: [localhost]: FAILED! => {"msg": "template not found"}
```
**Küsimus:** Mida kontrollida?

**Ülesanne:** Kirjutage README.md'sse troubleshooting sektsioon nende vigade jaoks!

---

## Task 8: Dokumenteerimine

### Ülesanne 7.1: README.md loomine

**Probleem:** Keegi teine peab teie projekti kasutama. Mis infot ta vajab?

**Nõutavad sektsioonid:**
1. **Projekt kirjeldus** - mis see teeb?
2. **Eeltingimused** - mida vaja installimisel?
3. **Kasutamise juhend** - sammhaaval käivitamine
4. **Konfiguratsioon** - kuidas muutujaid muuta?
5. **Testimine** - kuidas kontrollida, et töötab?
6. **Troubleshooting** - levinud probleemid ja lahendused
7. **Projekti struktuur** - failide selgitus

** Test:** Andke README.md kolleegile - kas ta saab projekti käivitada?

---

### Ülesanne 7.2: Koodikommentaarid

**Probleem:** Teie playbook peab olema loetav ja mõistetav.

**Nõuded:**
- Iga task vajab selget `name` välja
- Keerulised osad vajavad kommentaare
- Muutujad vajavad selgitusi
- Template'id vajavad dokumenteerimist

**Näide heast kommentaarist:**
```yaml
# MySQL root parooli seadistamine on keeruline, sest:
## Task 9: Pärast installimist pole parool seatud
## Kasutame unix_socket autentimist
## Task 10: Seejärel määrame parooli ja lülitume password auth'ile
- name: "Seadista MySQL root parool (esimene kord)"
  mysql_user:
    # ... resto kood
```

---

 

---

## Task 11: Esitamine

### Repository link
Esitage **GitHub repository link** kursuse süsteemi järgmiste nõuetega:

**Repository peab sisaldama:**
- Täielikku funktsionaalset Ansible projekti
- README.md täieliku dokumentatsiooniga  
- Screenshot'e või video tõendusmaterjali
- Deployment logisid

**Repository peab olema:**
- Public (et õppejõud saaks üle vaadata)
- Korrektselt nimetatud (`ansible-lamp-practice` või sarnane)
- Professionaalselt organiseeritud

**Peab olema võimalik:**
- Repository kloonida
- Juhendite järgi setup teha
- Playbook edukalt käivitada
- Tulemust valideerida

 **Tähtaeg:** Nädal 13 esimese loengu alguseks

---

## Task 12: Õnnestumise nipid

### Alustamise strateegia
1. **Alustage väikselt** - tehke esmalt Apache töötama
2. **Testige sageli** - iga komponendi järel kontrollige
3. **Kasutage lab'i materjale** - sealtsed näited aitavad
4. **Uurige dokumentatsiooni** - `ansible-doc <module_name>`
5. **Debugige süstemaatiliselt** - `-v` flag ja logide kontroll

### Kui midagi ei tööta
1. **Kontrollige süntaksit** - `--syntax-check`
2. **Kasutage verbose mode'i** - `-v`, `-vv`, `-vvv`
3. **Vaadake teenuste logisid** - `journalctl -u apache2`
4. **Kontrollige failide õiguseid** - `ls -la`
5. **Testige käsitsi** - tehke samme käsitsi läbi

### Ajakasutus
- **1. päev:** Projekti setup ja Apache
- **2. päev:** MySQL ja PHP
- **3. päev:** Template'id ja testimine
- **4. päev:** Dokumenteerimine ja viimistlus

