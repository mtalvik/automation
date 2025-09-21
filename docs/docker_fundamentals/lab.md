# Docker Fundamentals Lab: Docker & Podman Põhilised Kogemused
## Eesmärk: "Feel the difference" - Container fundamentals hands-on (2h)

Täna õpite konteinerite alused **praktikas**. Fookus on **mõistmisel**, mitte süntaksil.

---

## Lab'i eesmärgid

**Pärast seda lab'i teate:**
- **Miks konteinerid on kiired** (kogesite ise)
- **Kuidas ehitada lihtsat rakendust** (käed-küljes)
- **Docker vs Podman erinevusi** (side-by-side)
- **Põhilisi troubleshooting'u oskusi** (õppinud vigadest)

---

## Task 1: Container Speed Experience

### Ülesanne 1.1: "Feel the Speed"

**Võrdle VM vs Container startup aegu:**

```bash
## Testi container kiirus
time docker run hello-world
# Märkige aeg: _____ sekundit

## Testi teist container'it  
time docker run alpine echo "Hello from container"
# Märkige aeg: _____ sekundit

## Task 2: Võrdle VM'iga (kui teil on access)
# Käivitage VM - märkige aeg: _____utit
```

** Mida märkasite?**
- Container startup: ___ sekundit
- VM startup: ___utit  
- Erinevus: ___x kiirem

### Ülesanne 1.2: Resource Usage Comparison

```bash
## Vaadake Docker daemon resource kasutust
ps aux | grep docker
# Märkige RAM kasutus: _____ MB

## Task 3: Käivitage lihtne web server
docker run -d --name test-web -p 8080:80 nginx

## Task 4: Kontrollige container'i resource kasutust
docker stats test-web --no-stream
# Märkige CPU ja RAM: CPU: ___% RAM: ___MB

## Testiga ühendust
curl http://localhost:8080
# Kas töötab? ✅/❌
```

**🧹 Cleanup:**
```bash
docker stop test-web && docker rm test-web
```

### Ülesanne 1.3: Basic Commands Discovery

**Avastage käske ja vaadake, mis juhtub:**

```bash
# Millised image'id teil on?
docker images

# Millised containers töötavad?
docker ps
docker ps -a  # Mis erinevus?

# Palju ruumi võtab Docker?
docker system df

# Küsimus: Miks "hello-world" image on endiselt olemas?
# Vastus: _______________________
```

---

## Task 5: 📦 **Samm 2: Build Your First App ()**

### Ülesanne 2.1: Prepare Simple Web App

**Looge töökaust:**
```bash
mkdir ~/docker-fundamentals-lab && cd ~/docker-fundamentals-lab
```

**Looge lihtne HTML fail:**
```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Container App</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 100px; }
        .container { background: #f0f0f0; padding: 20px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1> My First Container App!</h1>
        <p>Server: <span id="hostname">Loading...</span></p>
        <p>Time: <span id="time"></span></p>
        <script>
            document.getElementById('time').innerText = new Date();
            fetch('/hostname').then(r => r.text()).then(h => 
                document.getElementById('hostname').innerText = h
            ).catch(() => 
                document.getElementById('hostname').innerText = 'Container ID: Unknown'
            );
        </script>
    </div>
</body>
</html>
```

### Ülesanne 2.2: Write Your First Dockerfile

**Template (täitke lüngad):**
```dockerfile
# TODO: Vali base image (nginx:alpine)
FROM ______

# TODO: Kopeeri HTML fail õigesse kohta 
# Nginx serveerib faile kaustast: /usr/share/nginx/html/
COPY ______ ______

# TODO: Avage port 80
EXPOSE ______

# CMD juba defined base image'is!
```

**Vastused (pärast katsetamist):**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```

### Ülesanne 2.3: Build and Test

```bash
## Task 6: Build image
docker build -t my-web-app .

# Kas build õnnestus? ✅/❌
# Kui ei, siis vaadake error message'i ja parandage

## Task 7: Run container
docker run -d --name my-app -p 8080:80 my-web-app

## Test
curl http://localhost:8080
# Või avage brauseris: http://localhost:8080

# Kas näete oma HTML'i? ✅/❌
```

### Ülesanne 2.4: Modify and Rebuild

**Muutke HTML faili:**
```html
<!-- Lisa midagi uut, näiteks: -->
<p>Version: 2.0 - Updated!</p>
<p>Student: [Your Name]</p>
```

**Rebuild ja test:**
```bash
# Build uus versioon
docker build -t my-web-app:v2 .

# Stop vana container
docker stop my-app && docker rm my-app

# Start uus container
docker run -d --name my-app-v2 -p 8080:80 my-web-app:v2

# Test
curl http://localhost:8080
# Kas näete muudatusi? ✅/❌
```

**🧹 Cleanup:**
```bash
docker stop my-app-v2 && docker rm my-app-v2
```

---

## Docker vs Podman Side-by-Side ()**

### Ülesanne 3.1: Install Podman (if needed)

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y podman

# Test installation
podman --version
```

### Ülesanne 3.2: Same Commands, Different Tools

**Käivitage SAMA rakendus mõlemas süsteemis:**

**Docker versio:**
```bash
# Terminal 1: Docker
docker run -d --name web-docker -p 8081:80 my-web-app:v2
```

**Podman versio:**
```bash
# Terminal 2: Podman  
podman run -d --name web-podman -p 8082:80 my-web-app:v2
```

**Teste mõlemat:**
```bash
# Docker test
curl http://localhost:8081

# Podman test  
curl http://localhost:8082

# Mõlemad töötavad? ✅/❌
```

### Ülesanne 3.3: Observe the Differences

**Resource usage:**
```bash
# Docker daemon
ps aux | grep dockerd
# Märkige RAM kasutus: _____ MB

# Podman (no daemon!)
ps aux | grep podman
# Märkige RAM kasutus: _____ MB
```

**User permissions:**
```bash
# Docker (check groups)
groups $USER
# Kas "docker" on listis? ✅/❌

# Podman (no special groups needed)
podman run --rm alpine id
# Container sees: uid=0 (root)

whoami
# Host sees: [your username]
```

**Commands:**
```bash
# Proovige sama käsku
docker ps
podman ps

# Kas output on sarnane? ✅/❌
```

**🧹 Cleanup:**
```bash
docker stop web-docker && docker rm web-docker
podman stop web-podman && podman rm web-podman
```

---

## Task 8: 🐛 **Samm 4: Troubleshooting & Networks ()**

### Ülesanne 4.1: Fix Broken Container

**Antakse teile "broken" Dockerfile:**
```dockerfile
FROM nginx:alpine
COPY index.html /wrong/path/
EXPOSE 80
```

**Proovige ehitada:**
```bash
docker build -t broken-app .
docker run -d --name broken -p 8083:80 broken-app
curl http://localhost:8083
```

**Diagnoosimine:**
```bash
# Vaadake loge
docker logs broken

# Minge sisse ja uurige
docker exec -it broken sh
ls /usr/share/nginx/html/  # Kas index.html on siin?
exit
```

** Küsimus:** Miks ei tööta?  
**Vastus:** ________________

**Parandage ja teste uuesti:**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```

### Ülesanne 4.2: Simple Network Test

```bash
# Käivitage 2 container'it custom network'is
docker network create test-network

docker run -d --name app1 --network test-network nginx:alpine
docker run -d --name app2 --network test-network nginx:alpine

# Test connectivity
docker exec app1 ping app2
# Kas töötab? ✅/❌

# Cleanup
docker stop app1 app2 && docker rm app1 app2
docker network rm test-network
```

---

## Task 9: Volume Persistence Test ()**

### Ülesanne 5.1: Data Persistence Challenge

**Create persistent web content:**
```bash
## Task 10: Create volume
docker volume create web-content

## Task 11: Run container with volume
docker run -d --name web-persistent \
    -p 8084:80 \
    -v web-content:/usr/share/nginx/html \
    nginx:alpine

## Task 12: Add custom content
docker exec web-persistent sh -c 'echo "<h1>Persistent Data!</h1>" > /usr/share/nginx/html/index.html'

## Test
curl http://localhost:8084
# Kas näete custom content'i? ✅/❌

## Destroy container (but keep volume!)
docker stop web-persistent && docker rm web-persistent

## Task 13: Create NEW container with SAME volume
docker run -d --name web-new \
    -p 8084:80 \
    -v web-content:/usr/share/nginx/html \
    nginx:alpine

## Test again
curl http://localhost:8084
# Kas andmed on alles? ✅/❌
```

** Küsimus:** Miks andmed jäid alles?  
**Vastus:** ________________

### Ülesanne 5.2: Development Workflow

```bash
# Mount current directory
docker run -it --rm \
    -v $(pwd):/workspace \
    -w /workspace \
    alpine sh

# Inside container:
echo "Container can modify host files" > test.txt
exit

# Check on host:
cat test.txt
# Kas fail on host'is? ✅/❌

# Cleanup
rm test.txt
```

---

## Lab Summary & Reflection**

### Mida te kogesite:

**Container Speed:**
- Container startup: ___ sekundit vs VM: ___utit
- Resource efficiency: Vähem overhead

**Building Apps:**
- Dockerfile = retsept rakenduse loomiseks
- Layer caching optimiseerib rebuild kiirust

**Docker vs Podman:**
- Docker: Daemon architecture, vajab special group
- Podman: Daemonless, rootless security

**Troubleshooting:**
- `docker logs` - esimene debug samm
- `docker exec` - konteiner investigation
- Volume'id säilitavad andmeid

 

### **Järgmised sammud:**

**Kodutöö:** Süvauurige Docker vs Podman võrdlust  
**Järgmine lab:** Docker Compose multi-container applications

---

## Task 14: **BOONUSÜLESANDED** (Docker'i oskajatele)

### Ülesanne Multi-stage Docker Builds

```dockerfile
# Optimized Node.js build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["npm", "start"]

# Build: docker build -t optimized-app .
```

### Ülesanne Docker Security ja Best Practices

```bash
# Non-root user
FROM alpine:latest
RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -s /bin/sh -D appuser
USER appuser

# Security scanning
docker scout cves myapp:latest
docker security scan myapp:latest

# Read-only filesystem
docker run --read-only --tmpfs /tmp myapp:latest

# Resource limits
docker run --memory=512m --cpus=1.5 myapp:latest
```

### Ülesanne Advanced Networking ja Storage

```bash
# Custom networks
docker network create --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  custom-network

# Named volumes with options
docker volume create --driver local \
  --opt type=bind \
  --opt device=/host/path \
  --opt o=bind \
  custom-volume

# Network debugging
docker exec container-name netstat -tulpn
docker exec container-name ss -tulpn
```

### Ülesanne Docker Performance Monitoring

```bash
# Container stats
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# System events
docker events --filter container=myapp

# Detailed inspection
docker inspect myapp | jq '.[].[0].State'

# Health checks
docker run --health-cmd='curl -f http://localhost:3000/health' \
           --health-interval=30s \
           --health-timeout=10s \
           --health-retries=3 \
           myapp:latest
```

### Ülesanne Docker Compose Advanced

```yaml
# docker-compose.advanced.yml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        - NODE_ENV=production
    deploy:
      replicas: 3
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    secrets:
      - db_password
    configs:
      - app_config

secrets:
  db_password:
    file: ./secrets/db_password.txt

configs:
  app_config:
    file: ./configs/app.conf
```

**Hästi tehtud!** Teil on nüüd nii põhi- kui ka ekspert-tasemel container kogemused! 
