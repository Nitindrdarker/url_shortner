# Scalable URL Shortener

A production-style URL shortener backend built using Django, Django REST Framework, PostgreSQL, Redis, Celery, and Docker.

This project focuses on backend engineering concepts such as caching, asynchronous task processing, rate limiting, analytics, retries, idempotency, and containerized deployment.

---

# Features

- URL shortening using Base62 encoding
- Fast redirection system
- Redis-based caching layer
- Rate limiting using Redis
- Asynchronous analytics processing with Celery
- Click tracking and analytics APIs
- Idempotent background tasks
- Retry mechanisms with exponential backoff
- PostgreSQL database
- Dockerized infrastructure
- Production deployment ready

---

# Tech Stack

## Backend
- Django
- Django REST Framework

## Database
- PostgreSQL

## Caching / Message Broker
- Redis

## Async Task Queue
- Celery

## Containerization
- Docker
- Docker Compose

## Deployment
- Railway
- Supabase PostgreSQL
- Upstash Redis

---

# Architecture

```text
Client
   ↓
Django REST API
   ↓
Redis Cache
   ↓
PostgreSQL

Celery Workers
   ↓
Analytics Processing
