# CI/CD Advanced Lab: Täielik Automatiseerimine
*ITS-24 DevOps Automatiseerimine | Praktiline lõppprojekt*

## Lab'i eesmärk

**Täna teeme LÕPPPROJEKTI!** Kasutame KÕIKI oskusi, mida õppisime:

- **Git** (Nädal 9) → Version control ja collaboration
- **Ansible** (Nädal 11-15) → Server configuration
- **Docker** (Nädal 19-21) → Containerization
- **Terraform** (Nädal 23) → Infrastructure as Code
- **CI/CD** (Nädal 25) → Automated deployment
- **Monitoring** → Production visibility

---

## 🏢 Projekt: "TechShop" E-commerce Automatiseerimine

**Klient:** Väike e-commerce startup "TechShop"

**Probleem:** 
- Käsitsi deployment võtab 2 tundi
- Tihti vigu (30% failure rate)
- Aeglane rollback (1+ tund)
- Arendajad stressis

**Lahendus:** Täielik automatiseerimine kõigi õpitud oskustega!

---

## 🛠 Ettevalmistus

### Vajalikud tööriistad

**Kontrollige, et teil on:**
```bash
# Versioonide kontroll
git --version           # 2.30+
docker --version        # 20.10+
python3 --version       # 3.9+
ansible --version       # 2.10+
terraform --version     # 1.0+
```

**Vajalikud kontod:**
- GitLab konto (tasuta)
- Docker Hub konto (valikuline)

---

## Osa 1: Infrastructure as Code (Terraform)

### 1.1 Projekti struktuur

```bash
# Loo projekt
mkdir techshop-automation
cd techshop-automation

# Loo Terraform kaust
mkdir -p terraform/templates
cd terraform
```

### 1.2 Terraform konfiguratsioon

**`variables.tf`:**
```hcl
variable "project_name" {
  description = "Project name"
  type        = string
  default     = "techshop"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "app_port" {
  description = "Application port"
  type        = number
  default     = 5000
}

variable "region" {
  description = "Deploy region"
  type        = string
  default     = "local"
}
```

**`main.tf`:**
```hcl
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }
}

# Create project structure
resource "local_file" "project_config" {
  content = jsonencode({
    project     = var.project_name
    environment = var.environment
    port        = var.app_port
    created_at  = timestamp()
  })
  filename = "${path.module}/config.json"
}

# Create docker-compose from template
resource "local_file" "docker_compose" {
  content = templatefile("${path.module}/templates/docker-compose.yml.tpl", {
    project_name = var.project_name
    environment  = var.environment
    app_port     = var.app_port
  })
  filename = "${path.module}/../docker-compose.yml"
}

# Create nginx config from template
resource "local_file" "nginx_config" {
  content = templatefile("${path.module}/templates/nginx.conf.tpl", {
    project_name = var.project_name
    app_port     = var.app_port
    server_name  = "localhost"
  })
  filename = "${path.module}/../nginx/nginx.conf"
}

# Null resource for local setup
resource "null_resource" "local_setup" {
  triggers = {
    always_run = timestamp()
  }
  
  provisioner "local-exec" {
    command = "echo '✅ Infrastructure ready for ${var.project_name}'"
  }
}
```

**`templates/docker-compose.yml.tpl`:**
```yaml
version: '3.8'

services:
  app:
    image: ${project_name}:latest
    container_name: ${project_name}-app
    ports:
      - "${app_port}:${app_port}"
    environment:
      - ENVIRONMENT=${environment}
      - PORT=${app_port}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:${app_port}/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - ${project_name}-network

  nginx:
    image: nginx:alpine
    container_name: ${project_name}-nginx
    ports:
      - "80:80"
    volumes:
      - ../nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - app
    networks:
      - ${project_name}-network

networks:
  ${project_name}-network:
    driver: bridge
```

**`templates/nginx.conf.tpl`:**
```nginx
upstream ${project_name}_backend {
    server app:${app_port};
}

server {
    listen 80;
    server_name ${server_name};
    
    location / {
        proxy_pass http://${project_name}_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /health {
        proxy_pass http://${project_name}_backend/health;
        access_log off;
    }
}
```

**`outputs.tf`:**
```hcl
output "project_name" {
  description = "Project name"
  value       = var.project_name
}

output "environment" {
  description = "Environment"
  value       = var.environment
}

output "app_url" {
  description = "Application URL"
  value       = "http://localhost:${var.app_port}"
}

output "config_file" {
  description = "Configuration file path"
  value       = local_file.project_config.filename
}
```

### 1.3 Deploy infrastruktuur

```bash
# Initsialiseeri Terraform
terraform init

# Vaata muudatusi
terraform plan

# Deploy
terraform apply -auto-approve

# Salvesta väljundid
terraform output -json > outputs.json
```

---

## Osa 2: Server Configuration (Ansible)

### 2.1 Ansible struktuur

```bash
# Mine projekti juurkausta
cd ..

# Loo Ansible struktuur
mkdir -p ansible/roles/webserver/{tasks,handlers,templates,defaults}
cd ansible
```

### 2.2 Inventory konfiguratsioon

**`inventory.yml`:**
```yaml
all:
  children:
    local:
      hosts:
        localhost:
          ansible_connection: local
          ansible_python_interpreter: /usr/bin/python3
    webservers:
      hosts:
        localhost:
          ansible_connection: local
      vars:
        app_name: techshop
        app_port: 5000
        docker_network: techshop-network
```

### 2.3 Webserver role

**`roles/webserver/defaults/main.yml`:**
```yaml
---
app_name: techshop
app_port: 5000
app_user: appuser
app_dir: /opt/{{ app_name }}
docker_compose_version: "2.21.0"
```

**`roles/webserver/tasks/main.yml`:**
```yaml
---
- name: Install system packages
  become: yes
  package:
    name:
      - python3
      - python3-pip
      - docker.io
      - curl
      - git
    state: present
    update_cache: yes

- name: Install Docker Compose
  become: yes
  get_url:
    url: "https://github.com/docker/compose/releases/download/v{{ docker_compose_version }}/docker-compose-linux-x86_64"
    dest: /usr/local/bin/docker-compose
    mode: '0755'

- name: Ensure Docker service is running
  become: yes
  systemd:
    name: docker
    state: started
    enabled: yes
    daemon_reload: yes

- name: Add current user to docker group
  become: yes
  user:
    name: "{{ ansible_user_id }}"
    groups: docker
    append: yes

- name: Create application directory
  become: yes
  file:
    path: "{{ app_dir }}"
    state: directory
    owner: "{{ ansible_user_id }}"
    group: "{{ ansible_user_id }}"
    mode: '0755'

- name: Copy docker-compose file
  copy:
    src: "../docker-compose.yml"
    dest: "{{ app_dir }}/docker-compose.yml"
    mode: '0644'

- name: Create nginx config directory
  file:
    path: "{{ app_dir }}/nginx"
    state: directory
    mode: '0755'

- name: Copy nginx configuration
  copy:
    src: "../nginx/nginx.conf"
    dest: "{{ app_dir }}/nginx/nginx.conf"
    mode: '0644'
```

**`roles/webserver/handlers/main.yml`:**
```yaml
---
- name: restart docker
  become: yes
  systemd:
    name: docker
    state: restarted

- name: reload nginx
  docker_container:
    name: techshop-nginx
    restart: yes
```

### 2.4 Main playbook

**`playbook.yml`:**
```yaml
---
- name: Configure TechShop infrastructure
  hosts: local
  gather_facts: yes
  
  pre_tasks:
    - name: Display setup information
      debug:
        msg: "Setting up {{ app_name }} on {{ ansible_hostname }}"
  
  roles:
    - webserver
  
  post_tasks:
    - name: Verify Docker installation
      command: docker --version
      register: docker_version
      
    - name: Display Docker version
      debug:
        msg: "Docker version: {{ docker_version.stdout }}"
```

### 2.5 Käivita Ansible

```bash
# Kontrolli süntaksi
ansible-playbook --syntax-check playbook.yml

# Käivita playbook
ansible-playbook -i inventory.yml playbook.yml

# Kontrolli tulemust
ansible all -i inventory.yml -m ping
```

---

## Osa 3: Application Development (Docker)

### 3.1 Rakenduse struktuur

```bash
# Mine projekti juurkausta
cd ..

# Loo rakenduse kaust
mkdir -p app/tests
cd app
```

### 3.2 Flask rakendus

**`app.py`:**
```python
#!/usr/bin/env python3
"""TechShop E-commerce API"""

from flask import Flask, jsonify, request
import os
import logging
from datetime import datetime
import psutil

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# In-memory database (for demo)
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99, 'stock': 10},
    {'id': 2, 'name': 'Phone', 'price': 599.99, 'stock': 25},
    {'id': 3, 'name': 'Tablet', 'price': 399.99, 'stock': 15},
    {'id': 4, 'name': 'Monitor', 'price': 299.99, 'stock': 20},
    {'id': 5, 'name': 'Keyboard', 'price': 79.99, 'stock': 50}
]

ORDERS = []

@app.route('/')
def home():
    """Home endpoint"""
    logger.info("Home endpoint accessed")
    return jsonify({
        'service': 'TechShop E-commerce API',
        'version': '1.0.0',
        'status': 'running',
        'timestamp': datetime.now().isoformat(),
        'endpoints': {
            'health': '/health',
            'metrics': '/metrics',
            'products': '/products',
            'orders': '/orders'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'techshop-api',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/metrics')
def metrics():
    """System metrics endpoint"""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return jsonify({
        'system': {
            'cpu_percent': cpu_percent,
            'memory_percent': memory.percent,
            'memory_available_gb': round(memory.available / (1024**3), 2),
            'disk_percent': disk.percent,
            'disk_free_gb': round(disk.free / (1024**3), 2)
        },
        'application': {
            'total_products': len(PRODUCTS),
            'total_orders': len(ORDERS)
        },
        'timestamp': datetime.now().isoformat()
    })

@app.route('/products')
def get_products():
    """Get all products"""
    logger.info("Products endpoint accessed")
    return jsonify({
        'products': PRODUCTS,
        'count': len(PRODUCTS),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/products/<int:product_id>')
def get_product(product_id):
    """Get single product"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/orders', methods=['GET', 'POST'])
def handle_orders():
    """Handle orders"""
    if request.method == 'GET':
        return jsonify({
            'orders': ORDERS,
            'count': len(ORDERS),
            'timestamp': datetime.now().isoformat()
        })
    
    # POST - create new order
    data = request.get_json()
    if not data or 'product_id' not in data:
        return jsonify({'error': 'Product ID required'}), 400
    
    product = next((p for p in PRODUCTS if p['id'] == data['product_id']), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    if product['stock'] < data.get('quantity', 1):
        return jsonify({'error': 'Insufficient stock'}), 400
    
    # Create order
    order = {
        'id': len(ORDERS) + 1,
        'product_id': product['id'],
        'product_name': product['name'],
        'quantity': data.get('quantity', 1),
        'total': product['price'] * data.get('quantity', 1),
        'created_at': datetime.now().isoformat()
    }
    
    # Update stock
    product['stock'] -= order['quantity']
    ORDERS.append(order)
    
    logger.info(f"Order created: {order['id']}")
    return jsonify(order), 201

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

**`requirements.txt`:**
```
Flask==2.3.3
gunicorn==21.2.0
psutil==5.9.5
requests==2.31.0
pytest==7.4.2
```

### 3.3 Dockerfile

**`Dockerfile`:**
```dockerfile
# Multi-stage build
FROM python:3.9-slim as builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.9-slim

WORKDIR /app

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Add user's local bin to PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:5000/health')"

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "30", "app:app"]
```

### 3.4 Local testing

```bash
# Build image
docker build -t techshop:latest .

# Run container
docker run -d --name techshop-test -p 5000:5000 techshop:latest

# Test endpoints
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/metrics
curl http://localhost:5000/products

# Create order
curl -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 2}'

# Cleanup
docker stop techshop-test
docker rm techshop-test
```

---

## Osa 4: CI/CD Pipeline (GitLab CI)

### 4.1 Git repository setup

```bash
# Mine projekti juurkausta
cd ..

# Initialize Git
git init

# Create .gitignore
cat > .gitignore << EOF
# Terraform
*.tfstate
*.tfstate.*
.terraform/
terraform.tfvars

# Python
__pycache__/
*.pyc
.pytest_cache/
venv/
.env

# Docker
.dockerignore

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
EOF

# Add files
git add .
git commit -m "Initial commit: TechShop automation project"

# Add remote (replace with your URL)
git remote add origin https://gitlab.com/your-username/techshop-automation.git
git push -u origin main
```

### 4.2 GitLab CI pipeline

**`.gitlab-ci.yml`:**
```yaml
# Define stages
stages:
  - validate
  - test
  - build
  - deploy

# Global variables
variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: ""
  IMAGE_NAME: $CI_REGISTRY_IMAGE/techshop
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA

# Cache configuration
cache:
  paths:
    - .terraform/

# Stage 1: Validate
validate:terraform:
  stage: validate
  image: hashicorp/terraform:1.5
  script:
    - cd terraform
    - terraform init -backend=false
    - terraform fmt -check=true
    - terraform validate
  only:
    - merge_requests
    - main

validate:ansible:
  stage: validate
  image: ansible/ansible:latest
  script:
    - cd ansible
    - ansible-playbook --syntax-check playbook.yml
  only:
    - merge_requests
    - main

# Stage 2: Test
test:python:
  stage: test
  image: python:3.9
  before_script:
    - cd app
    - pip install -r requirements.txt
  script:
    - python -m pytest tests/ -v
    - python -m flake8 app.py --max-line-length=100
  coverage: '/TOTAL.*\s+(\d+%)$/'
  only:
    - merge_requests
    - main

test:docker:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - cd app
    - docker build -t test-image .
    - docker run --rm test-image python -c "import app; print('✅ Import successful')"
  only:
    - merge_requests
    - main

# Stage 3: Build
build:docker:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - cd app
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
    - docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
    - docker push $IMAGE_NAME:$IMAGE_TAG
    - docker push $IMAGE_NAME:latest
    - echo "✅ Image pushed: $IMAGE_NAME:$IMAGE_TAG"
  only:
    - main

# Stage 4: Deploy
deploy:staging:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache curl docker-cli
  script:
    - echo "🚀 Deploying to staging..."
    - docker pull $IMAGE_NAME:$IMAGE_TAG
    - docker stop techshop-staging || true
    - docker rm techshop-staging || true
    - |
      docker run -d \
        --name techshop-staging \
        -p 5001:5000 \
        --restart unless-stopped \
        $IMAGE_NAME:$IMAGE_TAG
    - sleep 10
    - curl -f http://localhost:5001/health || exit 1
    - echo "✅ Staging deployment successful!"
  environment:
    name: staging
    url: http://localhost:5001
  only:
    - main

deploy:production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache curl docker-cli ansible
  script:
    - echo "🚀 Deploying to production..."
    - cd ansible
    - ansible-playbook -i inventory.yml deploy.yml
    - curl -f http://localhost/health || exit 1
    - echo "✅ Production deployment successful!"
  environment:
    name: production
    url: http://localhost
  when: manual
  only:
    - main
```

### 4.3 GitLab configuration

```bash
# Set GitLab CI/CD variables
# Go to: Settings → CI/CD → Variables

# Add these variables:
CI_REGISTRY_USER: your-gitlab-username
CI_REGISTRY_PASSWORD: your-gitlab-token
DOCKER_HOST: tcp://docker:2375
```

---

## Osa 5: Monitoring ja Observability

### 5.1 Monitoring stack

**`monitoring/docker-compose.yml`:**
```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    ports:
      - "9090:9090"
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    ports:
      - "3000:3000"
    networks:
      - monitoring

  node_exporter:
    image: prom/node-exporter:latest
    container_name: node_exporter
    ports:
      - "9100:9100"
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
    driver: bridge
```

**`monitoring/prometheus.yml`:**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node'
    static_configs:
      - targets: ['node_exporter:9100']
  
  - job_name: 'techshop'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['host.docker.internal:5000']
```

### 5.2 Application metrics

Lisage `app.py` faili Prometheus metrics:

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest

# Metrics
request_count = Counter('app_requests_total', 'Total requests', ['method', 'endpoint'])
request_duration = Histogram('app_request_duration_seconds', 'Request duration')
active_orders = Gauge('app_active_orders', 'Number of active orders')

@app.route('/metrics')
def metrics_prometheus():
    """Prometheus metrics endpoint"""
    # Update gauges
    active_orders.set(len(ORDERS))
    
    # Return metrics
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}
```

---

## Osa 6: Documentation

### 6.1 README.md

```markdown
# TechShop E-commerce Automation

## 📋 Overview

Complete DevOps automation project demonstrating modern CI/CD practices.

## 🏗 Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   GitLab    │────▶│   CI/CD      │────▶│  Deployment  │
│   Repo      │     │   Pipeline   │     │  Environment │
└─────────────┘     └──────────────┘     └──────────────┘
       │                    │                     │
       ▼                    ▼                     ▼
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  Terraform  │     │   Docker     │     │   Ansible    │
│    IaC      │     │  Container   │     │   Config     │
└─────────────┘     └──────────────┘     └──────────────┘
```

## 🚀 Quick Start

### Local Development
```bash
# Clone repository
git clone https://gitlab.com/username/techshop-automation.git
cd techshop-automation

# Run locally
cd app
docker build -t techshop:latest .
docker run -p 5000:5000 techshop:latest

# Test
curl http://localhost:5000/health
```

### Production Deployment
1. Push code to GitLab
2. Pipeline runs automatically
3. Manual approval for production

## 📊 Monitoring

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Application: http://localhost:5000

## 🛠 Technologies

- **Infrastructure**: Terraform
- **Configuration**: Ansible
- **Containerization**: Docker
- **CI/CD**: GitLab CI
- **Monitoring**: Prometheus + Grafana
- **Application**: Python Flask

## 📚 Documentation

- [API Documentation](docs/api.md)
- [Deployment Guide](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

## 📈 Metrics

- Deployment time: 2 hours → 5 minutes
- Error rate: 30% → 2%
- Rollback time: 1 hour → 2 minutes
```

---

## Lab'i kokkuvõte

### ✅ Saavutatud tulemused

1. **Täielik automatiseerimine** - nullist production'ini
2. **Kõik oskused kasutatud** - Git, Ansible, Docker, Terraform, CI/CD
3. **Production-ready lahendus** - monitoring, health checks, logging
4. **Dokumenteeritud projekt** - README, API docs, troubleshooting

### 📊 Mõõdetavad tulemused

| Metric | Enne | Pärast | Improvement |
|--------|------|--------|------------|
| Deployment aeg | 2 tundi | 5 minutit | 96% ↓ |
| Vigade arv | 30% | 2% | 93% ↓ |
| Rollback aeg | 1 tund | 2 minutit | 97% ↓ |
| Arendaja stress | Kõrge | Madal | 100% ↓ |

### 🎯 Järgmised sammud

- [ ] Lisa Kubernetes orchestration
- [ ] Implementeeri blue-green deployment
- [ ] Lisa security scanning (SAST/DAST)
- [ ] Automatiseeri load testing
- [ ] Lisa disaster recovery

### 🎉 Õnnitleme!

Olete edukalt lõpetanud DevOps automatiseerimise kursuse lõppprojekti! See projekt demonstreerib kõiki olulisi DevOps praktikaid ja on valmis kasutamiseks päris projektides.

**Portfolio väärtus:** See projekt on suurepärane lisand teie portfolio'sse ja demonstreerib oskusi, mida tööandjad otsivad!