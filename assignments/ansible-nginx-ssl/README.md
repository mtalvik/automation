# 🔐 Ansible: NGINX with SSL & PostgreSQL

## 📋 Ülesande kirjeldus

Selles ülesandes automatiseerid NGINX veebiserveri ja PostgreSQL andmebaasi paigalduse Ansible'iga. Lisad HTTPS toe, virtuaalhostid ja andmebaasi seadistuse.

## 🎯 Nõuded

### 1. NGINX Roll (roles/nginx/)

**Põhifunktsioonid:**
- [ ] Paigalda NGINX
- [ ] Genereeri self-signed SSL sertifikaat (365 päeva)
- [ ] Seadista HTTPS (port 443)
- [ ] HTTP → HTTPS redirect
- [ ] Virtuaalhostide tugi

**SSL sertifikaadid:**
```yaml
ssl_cert_path: /etc/ssl/certs/nginx.crt
ssl_key_path: /etc/ssl/private/nginx.key
```

### 2. PostgreSQL Roll (roles/postgresql/)

**Põhifunktsioonid:**
- [ ] Paigalda PostgreSQL
- [ ] Loo andmebaas: `webapp_db`
- [ ] Loo kasutaja: `webapp_user`
- [ ] Loo tabel `users` (id, name, email)
- [ ] Anna õigused

### 3. Projektstruktuur

```
ansible/
├── inventory/
│   └── hosts
├── group_vars/
│   └── all.yml
├── roles/
│   ├── nginx/
│   │   ├── tasks/main.yml
│   │   ├── templates/
│   │   │   └── nginx.conf.j2
│   │   └── handlers/main.yml
│   └── postgresql/
│       ├── tasks/main.yml
│       └── templates/
└── site.yml
```

## 🧪 Testimine

### Automaatsed testid kontrollivad:

```bash
# 1. HTTPS töötab
curl -k https://localhost
# Peab tagastama veebilehe

# 2. HTTP redirect töötab
curl -I http://localhost
# Peab olema 301 redirect HTTPS-ile

# 3. Andmebaas töötab
sudo -u postgres psql -d webapp_db -c "\dt"
# Peab näitama users tabelit

# 4. Teenused on enabled
systemctl is-enabled nginx postgresql
# Mõlemad peavad olema enabled
```

## 📝 Starter Code

**site.yml:**
```yaml
---
- name: Configure web infrastructure
  hosts: webservers
  become: true
  
  roles:
    - nginx
    - postgresql
```

**roles/nginx/tasks/main.yml:**
```yaml
---
- name: Install NGINX
  package:
    name: nginx
    state: present

# TODO: Add SSL certificate generation
# TODO: Add NGINX configuration template
# TODO: Add virtual hosts support

- name: Start and enable NGINX
  service:
    name: nginx
    state: started
    enabled: true
```

**roles/postgresql/tasks/main.yml:**
```yaml
---
- name: Install PostgreSQL
  package:
    name: 
      - postgresql
      - postgresql-contrib
      - python3-psycopg2
    state: present

# TODO: Add database creation
# TODO: Add user creation
# TODO: Add table schema
```

## 💡 Vihjed

### SSL Sertifikaadi genereerimine:

```yaml
- name: Generate SSL private key
  openssl_privatekey:
    path: "{{ ssl_key_path }}"
    size: 2048
    mode: '0600'

- name: Generate SSL certificate
  openssl_certificate:
    path: "{{ ssl_cert_path }}"
    privatekey_path: "{{ ssl_key_path }}"
    provider: selfsigned
    days_valid: 365
```

### PostgreSQL andmebaasi loomine:

```yaml
- name: Create database
  postgresql_db:
    name: webapp_db
    state: present
  become_user: postgres

- name: Create database user
  postgresql_user:
    db: webapp_db
    name: webapp_user
    password: "{{ db_password }}"
    priv: ALL
  become_user: postgres
```

## 📊 Hindamine

| Kriteerium | Punkte | Kirjeldus |
|------------|--------|-----------|
| NGINX paigaldus | 15 | Teenus töötab ja on enabled |
| SSL sertifikaat | 20 | Genereeritud ja õiged õigused |
| HTTPS config | 20 | Port 443 töötab, redirect olemas |
| PostgreSQL | 15 | Andmebaas ja kasutaja loodud |
| Tabel ja õigused | 15 | Schema loodud, õigused antud |
| Idempotency | 10 | Korduvkäivitus on turvaline |
| Dokumentatsioon | 5 | README ja kommentaarid |

## 🚀 Lisaülesanded (bonus)

- [ ] Let's Encrypt sertifikaat (certbot)
- [ ] Backup strateegia PostgreSQL-ile
- [ ] Monitoring (node_exporter + postgres_exporter)
- [ ] Rate limiting NGINX-is
- [ ] Fail2ban integratsioon

## 📚 Ressursid

- [Ansible NGINX role näide](https://github.com/geerlingguy/ansible-role-nginx)
- [PostgreSQL Ansible moodulid](https://docs.ansible.com/ansible/latest/collections/community/postgresql/)
- [SSL sertifikaatide genereerimine](https://docs.ansible.com/ansible/latest/collections/community/crypto/)

## ✅ Submission

1. Push lahendus `main` branchi
2. GitHub Actions kontrollib automaatselt
3. Vaata tulemusi Actions tabist

---

**NB!** Kasuta muutujaid paroolide ja tundlike andmete jaoks. Ära hardcodeeri paroole!
