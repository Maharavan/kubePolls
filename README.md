# 🗳️ kubePolls – Django Voting App on Kubernetes

A **Django-based voting application** using **SQLite3** as the database. This project demonstrates running a full-stack app on **Kubernetes** or locally via **Docker Compose**, using a pre-built Docker image: `mahar628/kubepolls:v1`.

---

## ✨ Features

- 📝 Create and vote on polls
- 💾 SQLite3 database for lightweight storage
- 🐳 Fully containerized for **Kubernetes** or **Docker Compose**
- 🌐 Supports **ClusterIP + Ingress** in Minikube or local Kubernetes clusters
- 🔑 Optional NodePort for local access on WSL/Windows

---

## 🛠️ Prerequisites

- 🐳 [Docker](https://docs.docker.com/get-docker/)
- 📦 [Docker Compose](https://docs.docker.com/compose/)
- 🏗️ [Minikube](https://minikube.sigs.k8s.io/docs/) (for Kubernetes deployment)
- ⚓ [kubectl](https://kubernetes.io/docs/tasks/tools/) CLI

---

## 🚀 Running Locally with Docker Compose

1. **Clone the repository**
```bash
git clone https://github.com/Maharavan/kubePolls.git
cd kubePolls
```

2. **Use the updated Docker image**
- Ensure `docker-compose.yml` references `mahar628/kubepolls:v1`.

3. **Start the application**
```bash
docker-compose up -d
```

4. **Access the app**
- Open your browser at `http://localhost:8000` 🌐

5. **Stop the application**
```bash
docker-compose down
```

---

## ☸️ Running on Minikube (Kubernetes)

1. **Start Minikube**
```bash
minikube start --driver=docker
```

2. **Enable Ingress addon**
```bash
minikube addons enable ingress
```

3. **Apply Deployment & Service YAML**
```bash
kubectl apply -f django-app.yml
```

4. **Apply Ingress YAML**
```bash
kubectl apply -f django-ingress.yml
```

5. **Add hostname mapping**
- Edit your `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows) and add:
```
<minikube-ip> myapp.local
```
- Get Minikube IP:
```bash
minikube ip
```

6. **Start Minikube tunnel**
```bash
minikube tunnel
```
- Keep this terminal open to route traffic to Ingress 🔄

7. **Access the app**
- Open your browser at `http://myapp.local` 🌐
- Or test with curl:
```bash
curl http://myapp.local
```

---

## 📝 Notes

- If using **WSL**, `minikube service django-service` is the easiest way to test access ✅
- ClusterIP + Ingress is preferred for production-like setups 🏗️
- NodePort can be used for simpler local testing ⚡

---

## 🧹 Cleanup

```bash
kubectl delete -f django-ingress.yml
kubectl delete -f django-app.yml
minikube stop
```