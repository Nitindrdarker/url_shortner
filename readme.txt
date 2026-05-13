🚀 Scalable URL Shortener

A production-style URL shortener backend built using Django, Redis, Celery, PostgreSQL, and Docker.

This project focuses on real backend engineering concepts such as:

⚡ Caching
🔄 Asynchronous task processing
🛡️ Rate limiting
📊 Analytics
♻️ Retry mechanisms
✅ Idempotency
🐳 Containerized deployment
✨ Features
🔗 URL shortening using Base62 encoding
⚡ Fast redirection system
🧠 Redis-based caching layer
🛡️ IP-based rate limiting
📊 Click tracking & analytics APIs
🔄 Asynchronous analytics processing with Celery
✅ Idempotent background tasks
♻️ Retry mechanism with exponential backoff
🐳 Dockerized infrastructure
☁️ Cloud deployment ready
🏗️ Tech Stack
Backend
Django
Django REST Framework
Database
PostgreSQL
Cache / Message Broker
Redis
Async Task Queue
Celery
Containerization
Docker
Docker Compose
Deployment
Railway
Supabase PostgreSQL
Upstash Redis
🧠 System Architecture
                ┌─────────────┐
                │   Client    │
                └──────┬──────┘
                       │
                       ▼
            ┌────────────────────┐
            │  Django REST API   │
            └──────┬──────┬──────┘
                   │      │
         Cache Hit │      │ Async Tasks
                   ▼      ▼
            ┌────────┐   ┌──────────────┐
            │ Redis  │   │ Celery Worker│
            └────┬───┘   └──────┬───────┘
                 │              │
                 ▼              ▼
            ┌────────────────────────┐
            │     PostgreSQL DB      │
            └────────────────────────┘
