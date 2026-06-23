<div align="center">

```
██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗     ██╗     ███████╗
██║ ██╔╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║     ██║     ██╔════╝
█████╔╝ ██║   ██║██████╔╝█████╗  ██████╔╝██║   ██║██║     ██║     ███████╗
██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██║     ██║     ╚════██║
██║  ██╗╚██████╔╝██████╔╝███████╗██║     ╚██████╔╝███████╗███████╗███████║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

### Real-time polling — cloud-native, containerized, production-ready

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io)

<br/>

[![Gunicorn](https://img.shields.io/badge/Gunicorn-23.0-499848?style=flat-square&logo=gunicorn&logoColor=white)](https://gunicorn.org)
[![NGINX](https://img.shields.io/badge/Ingress-NGINX-009639?style=flat-square&logo=nginx&logoColor=white)](https://kubernetes.github.io/ingress-nginx/)
[![Docker Hub](https://img.shields.io/badge/Image-mahar628%2Fkubepolls%3Alatest-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/mahar628/kubepolls)
[![CI](https://img.shields.io/github/actions/workflow/status/Maharavan/kubePolls/workflow.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white&label=CI)](https://github.com/Maharavan/kubePolls/actions)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [CI/CD Pipeline](#cicd-pipeline)
- [User Flow](#user-flow)
- [Data Model](#data-model)
- [Architecture](#architecture)
  - [Docker Compose](#docker-compose-architecture)
  - [Kubernetes](#kubernetes-architecture)
- [Request Lifecycle](#request-lifecycle)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Environment Variables](#environment-variables)
- [Cleanup](#cleanup)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**KubePolls** is a full-stack polling application built with **Django 5.2** and designed from the ground up for containerized environments. Create polls in seconds, gather votes in real time, and visualize results with animated percentage-fill bars — all running inside Docker or a Kubernetes cluster.

The project ships with a pre-built Docker image (`mahar628/kubepolls:latest`) and a PostgreSQL backend, so you can be up and running with a single command — no build step required for local development.

---

## Features

| | Feature | Description |
|---|---|---|
| ⚙️ | **Poll Creation** | Build polls with 2–5 custom choices via a clean form UI |
| ⚡ | **Live Voting** | Instant vote submission with client-side validation |
| 📊 | **Animated Results** | Smooth gradient fill-bars per choice with live percentages |
| 🧭 | **In-page Navigation** | Fixed back / forward / home buttons on every page |
| 🎨 | **Modern UI** | Glassmorphism dark theme — emerald & amber gradients, Inter font |
| 🐘 | **PostgreSQL Backend** | Production-grade relational database with persistent volume |
| 🐳 | **Docker Compose** | Two-service stack (app + db) with health-check orchestration |
| ☸️ | **Kubernetes Native** | ClusterIP Service + NGINX Ingress manifests included |
| 🔄 | **CI/CD** | GitHub Actions auto-builds and pushes Docker image on every push to `main` |

---

## Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Language | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) Python | 3.11 |
| Framework | ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white) Django | 5.2 |
| Database | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) PostgreSQL | 16 (Alpine) |
| App Server | ![Gunicorn](https://img.shields.io/badge/-Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white) Gunicorn | 23.0 |
| Static Files | ![WhiteNoise](https://img.shields.io/badge/-WhiteNoise-333?style=flat-square) WhiteNoise | 6.1 |
| Container | ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white) Docker + Compose | latest |
| Orchestration | ![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) Kubernetes | Minikube |
| Ingress | ![NGINX](https://img.shields.io/badge/-NGINX-009639?style=flat-square&logo=nginx&logoColor=white) NGINX Ingress | — |
| Frontend | Django Templates + Custom CSS (glassmorphism) | — |

---

## CI/CD Pipeline

Every push to `main` triggers a GitHub Actions workflow that builds and publishes the Docker image to Docker Hub automatically — no manual steps required.

```mermaid
flowchart LR
    Push(["📤 git push\nmain"])
    Checkout["⬇️ actions/checkout@v4"]
    Login["🔐 Docker Login\nDOCKER_USERNAME\nDOCKER_PASSWORD"]
    Build["🔨 docker build\nkubepolls:latest"]
    Tag["🏷️ docker tag\nUSERNAME/kubepolls:latest"]
    Push2["🚀 docker push\nDocker Hub"]

    Push --> Checkout --> Login --> Build --> Tag --> Push2

    style Push fill:#0b1e14,stroke:#f59e0b,color:#e8f5ee
    style Checkout fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Login fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Build fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Tag fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Push2 fill:#0b1e14,stroke:#2496ED,color:#e8f5ee
```

**Required repository secrets:**

| Secret | Description |
|---|---|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password or access token |

> Set these under **Settings → Secrets and variables → Actions** in your GitHub repository.

---

## User Flow

```mermaid
flowchart TD
    A([🏠 Home Page\n/]) --> B([📝 Create Poll\n/create-polls/])
    A --> C([📋 View Polls\n/poll-list/])
    B -->|POST → redirect| C
    C --> D([🗳️ Cast Vote\n/live-polls/?id=])
    D -->|POST → redirect| E([📊 Results\n/poll-results/?question_id=])
    E -->|Back button| C

    style A fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style B fill:#0b1e14,stroke:#f59e0b,color:#e8f5ee
    style C fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style D fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style E fill:#0b1e14,stroke:#22c55e,color:#e8f5ee
```

---

## Data Model

```mermaid
erDiagram
    VoteQuestions {
        int     id          PK
        string  question
        datetime date
    }

    Choices {
        int     id          PK
        int     question_id FK
        string  choice
        int     vote
    }

    VoteQuestions ||--o{ Choices : "has"
```

---

## Architecture

### Docker Compose Architecture

```mermaid
graph LR
    Browser(["🌐 Browser\nlocalhost:8000"])

    subgraph compose["Docker Compose Stack"]
        direction TB
        App["🐍 kubePolls\nDjango + Gunicorn\n:8000"]
        DB[("🐘 db\nPostgreSQL 16\n:5432")]
        Vol[/"📦 postgres_data\nnamed volume"/]

        App -->|"psycopg2\nDB_HOST=db"| DB
        DB --- Vol
    end

    Browser -->|"HTTP :8000"| App

    style compose fill:#071510,stroke:#10b981,stroke-width:1.5px,color:#e8f5ee
    style App fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style DB fill:#0b1e14,stroke:#4169E1,color:#e8f5ee
    style Vol fill:#0b1e14,stroke:#f59e0b,color:#e8f5ee
    style Browser fill:#030d07,stroke:#8ab59a,color:#e8f5ee
```

### Kubernetes Architecture

```mermaid
graph TD
    Browser(["🌐 Browser\nhttp://myapp.local"])

    subgraph cluster["Kubernetes Cluster (Minikube)"]
        Ingress["🔀 NGINX Ingress\nhost: myapp.local\npath: /"]
        Service["⚙️ ClusterIP Service\ndjango-service\nport: 8000"]

        subgraph pod["Pod — mahar628/kubepolls:latest"]
            Gunicorn["🐍 Django + Gunicorn\n0.0.0.0:8000"]
        end

        Ingress --> Service
        Service --> pod
    end

    Browser -->|"HTTP (minikube tunnel)"| Ingress

    style cluster fill:#071510,stroke:#326CE5,stroke-width:1.5px,color:#e8f5ee
    style pod fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Ingress fill:#0b1e14,stroke:#009639,color:#e8f5ee
    style Service fill:#0b1e14,stroke:#10b981,color:#e8f5ee
    style Gunicorn fill:#030d07,stroke:#f59e0b,color:#e8f5ee
    style Browser fill:#030d07,stroke:#8ab59a,color:#e8f5ee
```

---

## Request Lifecycle

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant Gunicorn
    participant Django
    participant PostgreSQL

    User->>Browser: Open /poll-list/
    Browser->>Gunicorn: GET /poll-list/
    Gunicorn->>Django: poll_list(request)
    Django->>PostgreSQL: VoteQuestions.objects.all()
    PostgreSQL-->>Django: QuerySet [q1, q2, ...]
    Django-->>Browser: Render viewPolls.html

    User->>Browser: Click poll → /live-polls/?id=2
    Browser->>Gunicorn: GET /live-polls/?id=2
    Django->>PostgreSQL: Choices.objects.filter(question_id=2)
    PostgreSQL-->>Django: [choice1, choice2]
    Django-->>Browser: Render livePolls.html

    User->>Browser: Select choice & submit
    Browser->>Gunicorn: POST /live-polls/
    Django->>PostgreSQL: selected_choice.vote += 1 · save()
    Django-->>Browser: 302 → /poll-results/?question_id=2
    Browser->>Gunicorn: GET /poll-results/?question_id=2
    Django->>PostgreSQL: Choices.objects.filter(question_id=2)
    PostgreSQL-->>Django: choices with vote counts
    Django-->>Browser: Render pollResults.html
```

---

## Project Structure

<details>
<summary><strong>Click to expand</strong></summary>

```
kubePolls/
├── django/
│   ├── members/                        # Core Django app
│   │   ├── migrations/                 # Database schema migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_votequestions_date.py
│   │   │   └── 0003_choices.py
│   │   ├── static/
│   │   │   └── css/
│   │   │       ├── style.css           # Global theme (index, viewPolls, askPolls)
│   │   │       ├── livePoll.css        # Vote page styles
│   │   │       └── pollResult.css      # Results page styles
│   │   ├── templates/
│   │   │   ├── index.html              # Home — Create / View buttons
│   │   │   ├── askPolls.html           # Poll creation form
│   │   │   ├── viewPolls.html          # Poll list
│   │   │   ├── livePolls.html          # Voting form
│   │   │   └── pollResults.html        # Animated results bars
│   │   ├── models.py                   # VoteQuestions · Choices
│   │   ├── views.py                    # All view logic
│   │   └── urls.py                     # App URL routes
│   ├── votesystem/
│   │   ├── settings.py                 # Django settings (env-var driven DB config)
│   │   ├── urls.py                     # Root URL conf
│   │   └── wsgi.py
│   ├── manage.py
│   ├── requirements.txt                # gunicorn · whitenoise · django · psycopg2-binary
│   └── Dockerfile
├── k8s/
│   ├── django-app.yml                  # Deployment (1 replica, resource limits) + ClusterIP Service
│   └── django-ingress.yml              # NGINX Ingress — host: myapp.local
├── .github/
│   └── workflow.yml                    # CI — build & push Docker image on push to main
├── docker-compose.yml                  # App + PostgreSQL with health-check
└── README.md
```

</details>

---

## Quick Start

### Option A — Docker Compose (recommended for local dev)

```bash
# 1. Clone the repo
git clone https://github.com/Maharavan/kubePolls.git
cd kubePolls

# 2. Start the stack (app + PostgreSQL)
docker compose up --build

# 3. Open in browser
open http://localhost:8000
```

> On first start the app container waits for PostgreSQL to pass its health check, then runs `manage.py migrate` automatically before gunicorn starts.

```bash
# Stop and remove containers (data volume is preserved)
docker compose down

# Remove containers AND the database volume
docker compose down -v
```

---

## Kubernetes Deployment

### Step 1 — Start the cluster

```bash
minikube start --driver=docker
minikube addons enable ingress
```

### Step 2 — Apply manifests

```bash
kubectl apply -f k8s/django-app.yml
kubectl apply -f k8s/django-ingress.yml
```

Verify everything is running:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

### Step 3 — Configure local DNS

Get the Minikube IP:

```bash
minikube ip
```

Add to your hosts file:

| OS | Path |
|---|---|
| Linux / macOS | `/etc/hosts` |
| Windows | `C:\Windows\System32\drivers\etc\hosts` |

```
<minikube-ip>  myapp.local
```

### Step 4 — Open a tunnel

```bash
# Keep this terminal open — routes traffic to the Ingress controller
minikube tunnel
```

Then navigate to **http://myapp.local**.

> **WSL users:** `minikube service django-service` is a simpler alternative to tunnel + Ingress.

---

## Environment Variables

The Django settings are fully driven by environment variables (with sensible defaults that match the Compose file):

| Variable | Default | Description |
|---|---|---|
| `DB_NAME` | `kubepolls` | PostgreSQL database name |
| `DB_USER` | `kubepolls` | PostgreSQL user |
| `DB_PASSWORD` | `kubepolls` | PostgreSQL password |
| `DB_HOST` | `localhost` | Database hostname (`db` in Compose) |
| `DB_PORT` | `5432` | Database port |

---

## Cleanup

### Docker Compose

```bash
docker compose down -v   # stop containers + remove data volume
```

### Kubernetes

```bash
kubectl delete -f k8s/django-ingress.yml
kubectl delete -f k8s/django-app.yml
minikube stop
minikube delete          # optional — removes the VM entirely
```

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ☕ and Kubernetes by [Maharavan](https://github.com/Maharavan)

[![Star on GitHub](https://img.shields.io/github/stars/Maharavan/kubePolls?style=social)](https://github.com/Maharavan/kubePolls)

</div>
