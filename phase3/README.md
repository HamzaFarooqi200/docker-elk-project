# Phase 3: Full ELK Stack Deployment with Docker 🐳📊

This phase of the project focuses on deploying a **fully functional ELK (Elasticsearch, Logstash, Kibana) Stack** using Docker. The setup is designed to collect, process, and visualize logs from multiple containers efficiently.

## 🔹 Project Overview

In Phase 3, the goal was:
- Deploy the complete ELK stack using Docker containers.
- Collect logs from multiple application containers separately.
- Parse, transform, and visualize logs in Kibana dashboards.
- Ensure high availability with health checks and persistent storage.

This phase builds on Phase 2 by adding **advanced monitoring and observability** features, making it closer to a production-ready setup.

## 🔹 Key Achievements

1. **Container-specific log collection**: Each container’s logs are ingested separately via Logstash pipelines.
2. **Custom Logstash pipelines**: Logs are parsed, filtered, and transformed for better visualization and analysis.
3. **Kibana dashboards**: Real-time monitoring of application performance, errors, and metrics.
4. **Health checks and auto-restart**: ELK containers have health checks to ensure high availability.
5. **Persistent storage**: Docker volumes ensure Elasticsearch data persists across restarts.
6. **Optimized Docker Compose**: Multi-container orchestration allows easy deployment and scaling.

## 🔹 Technologies Used

- **Docker & Docker Compose** 🐳
- **Elasticsearch**
- **Logstash**
- **Kibana**
- **Linux (Ubuntu/any Debian-based system)**

## 🔹 Prerequisites

Before running the project, ensure you have:
- Docker installed: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose installed: [Install Docker Compose](https://docs.docker.com/compose/install/)
- Git installed to clone the repository

## 🔹 Running the Project

1. **Clone the repository**
```bash
git clone https://github.com/HamzaFarooqi200/docker-elk-project.git
cd docker-elk-project/phase3
```

2. **Start the ELK stack using Docker Compose**
```bash
docker-compose up -d
```

3. **Verify running containers**
```bash
docker ps
```
You should see containers for `elasticsearch`, `logstash`, `kibana`, and any application containers sending logs.

4. **Access Kibana Dashboard**
Open your browser and go to:
```
http://localhost:5601
```
Here, you can explore dashboards, visualizations, and logs.

5. **Stop the stack**
```bash
docker-compose down
```

## 🔹 Folder Structure

```
phase3/
│
├── docker-compose.yml       # Docker Compose configuration for ELK stack
├── logstash/
│   ├── pipelines/           # Logstash pipeline configurations
│   └── logstash.conf        # Main Logstash config
├── kibana/                  # Kibana configurations (if any custom settings)
└── README.md
```

## 🔹 Notes

- Make sure to configure your application containers to output logs to locations monitored by Logstash.
- Docker volumes are used to persist Elasticsearch data, so you don’t lose logs on container restart.
- Health checks are configured to ensure ELK containers automatically restart if they fail.
