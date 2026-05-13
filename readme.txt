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
📡 API Endpoints
🔗 Create Short URL
POST /api/shorten/
Request
{
  "original_url": "https://google.com"
}
Response
{
  "data": {
    "short_code": "abc123",
    "short_url": "https://your-domain/api/abc123"
  }
}
↪️ Redirect URL
GET /api/<short_code>/

Redirects the user to the original URL.

📊 URL Analytics
GET /api/analytics/<short_code>/

Returns:

Total clicks
Original URL
Creation date
🏆 Top URLs
GET /api/analytics/top-urls/

Returns the top most-clicked URLs.

⚙️ Engineering Concepts Implemented
⚡ Redis Caching

Implemented read-through caching to reduce database load and improve redirect performance.

Flow
Request
   ↓
Redis Cache
   ↓ (cache miss)
Database
   ↓
Redis Cache Updated
Benefits
Faster redirects
Reduced DB pressure
Improved scalability
🛡️ Rate Limiting

Implemented IP-based rate limiting using Redis counters and TTL expiration.

Prevents
Abuse
Bot traffic
Excessive API usage
🔄 Asynchronous Processing

Used Celery with Redis to offload analytics processing from the Django request cycle.

Why?
Non-blocking redirects
Better scalability
Faster response times
✅ Idempotent Tasks

Background tasks are designed to be idempotent using unique request identifiers.

Prevents
Duplicate analytics events
Retry inconsistencies
♻️ Retry Mechanism

Implemented retry support with exponential backoff for transient failures.

Retry Strategy
2s → 4s → 8s

Improves reliability during:

DB outages
Worker crashes
Temporary network issues
