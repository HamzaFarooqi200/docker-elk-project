# Phase 2 - Dockerized Frontend and Backend

## Overview

This project is the second phase of our multi-phase application deployment setup. It includes:

- **Frontend:** Static web files served by Nginx.
- **Backend:** API service (e.g., Flask/Node.js) running on a separate container.
- **Reverse Proxy:** Nginx acts as a reverse proxy for the backend APIs.
- **Docker Compose:** Orchestrates frontend, backend, and network configuration.

---

## Folder Structure

```
phase2/
│
├── frontend/                  # Frontend code (HTML, CSS, JS)
│   └── index.html
│
├── backend/                   # Backend service
│   ├── app.py                 # Example Flask app
│   └── requirements.txt
│
├── nginx/
│   └── nginx.conf             # Nginx configuration
│
├── docker-compose.yml
└── README.md
```

---

## Prerequisites

- Docker installed on your machine
- Docker Compose installed
- Basic knowledge of terminal/command line

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <repository-url>
cd phase2
```

2. **Build and start the containers:**

```bash
docker-compose up --build
```

3. **Access the application:**

- Frontend: [http://localhost](http://localhost)
- Backend API: [http://localhost/api](http://localhost/api) (proxied via Nginx)

---

## Docker Compose Configuration

**Key Points:**

- **Frontend volume mount:**  

```yaml
- ./frontend:/usr/share/nginx/html
```

  Maps your local frontend folder to the Nginx container. Any changes to `./frontend` reflect immediately in the container.

- **Backend service:**  

```yaml
depends_on:
  - backend
```

  Ensures Nginx starts after the backend is ready.

- **Network:**  

```yaml
networks:
  - appnet
```

  Allows containers to communicate internally.

- **Restart policy:**  

```yaml
restart: unless-stopped
```

  Automatically restarts containers if they crash.

---

## Nginx Configuration

- Serves frontend static files from `/usr/share/nginx/html`.
- Proxies requests with `/api/` prefix to the backend service.

---

## Notes

- Make sure your backend is running on the port defined in `nginx.conf`.
- Any changes in `frontend/` folder are automatically reflected in the running container.
- Stop the services with:

```bash
docker-compose down
```

---

## Author

**Hamza Farooqi**