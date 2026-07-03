# Architecture Guide

## System Overview

This document describes the architecture of the modern Object Detection Platform.

## High-Level Design

```
┌──────────────────────────────────────────────────────────────┐
│                     Client Layer                             │
│  ┌─────────────────┐  ┌──────────────────┐                   │
│  │  React SPA      │  │  WebRTC Stream   │                   │
│  │  (Browser)      │  │  (Video/Audio)   │                   │
│  └────────┬────────┘  └────────┬─────────┘                   │
└───────────┼────────────────────┼──────────────────────────────┘
            │ HTTP/WebSocket     │ Media Stream
┌───────────▼──────────────────────▼──────────────────────────────┐
│                    API Gateway / FastAPI                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  /api/v1/detection   /api/v1/upload   /ws/stream        │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────────────────────┐
│                  Service Layer                                  │
│  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │ Detection       │  │ Training         │  │ User         │  │
│  │ Service         │  │ Service          │  │ Service      │  │
│  └─────────────────┘  └──────────────────┘  └──────────────┘  │
└────────────┬────────────────────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────────────────────┐
│                    ML Inference Layer                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ONNX Runtime  │  Preprocessing  │  Postprocessing      │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────────────────────┐
│                  Data Layer                                     │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────────────┐  │
│  │ PostgreSQL   │  │ Redis Cache │  │ S3/MinIO Storage     │  │
│  │ (Metadata)   │  │ (Hot Data)  │  │ (Models, Images)     │  │
│  └──────────────┘  └─────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Backend Architecture

### FastAPI Application Structure

```
app/
├── main.py                 # FastAPI app initialization
├── api/
│   ├── v1/
│   │   ├── detection.py    # Detection endpoints
│   │   ├── training.py     # Training endpoints
│   │   └── models.py       # Model management
│   └── dependencies.py     # Shared dependencies
├── core/
│   ├── config.py           # Pydantic settings
│   ├── security.py         # Auth & permissions
│   └── logging.py          # Structured logging
├── ml/
│   ├── inference.py        # ONNX inference engine
│   ├── preprocessing.py    # Image preprocessing
│   └── postprocessing.py   # Result formatting
├── db/
│   ├── base.py             # Database base config
│   ├── models.py           # SQLAlchemy models
│   └── crud.py             # CRUD operations
└── schemas/
    ├── detection.py        # Pydantic schemas
    └── training.py
```

## Frontend Architecture

### React Component Hierarchy

```
App
├── Layout
│   ├── Header
│   └── Sidebar
├── Router
│   ├── /live      (Live detection)
│   ├── /upload    (Image upload)
│   ├── /history   (Results history)
│   └── /training  (Model training)
└── Providers
    ├── AuthProvider
    └── ThemeProvider
```

## Data Flow

### Image Upload Flow

1. User selects image in UI
2. Frontend validates file size/type
3. Frontend sends HTTP POST to `/api/v1/detection/upload`
4. Backend stores image, queues inference
5. Backend runs ONNX inference
6. Backend saves results to PostgreSQL
7. Frontend polls `/api/v1/detection/{result_id}` for results
8. Frontend renders detections on canvas

### Real-Time Video Flow

1. User clicks "Start" in Live tab
2. Frontend initiates WebRTC connection
3. Backend receives media stream
4. Backend processes frames at ~30 FPS
5. Backend runs ONNX inference per frame
6. Backend sends detections back via WebRTC
7. Frontend renders bounding boxes on canvas

## Scalability Considerations

### Horizontal Scaling

- **Stateless backend**: Each instance can handle any request
- **Redis session store**: Sessions shared across instances
- **Load balancer**: Distributes requests (nginx/HAProxy)

### Performance Optimization

- **ONNX Runtime**: Faster inference than PyTorch (~3-5x)
- **Batch processing**: Group multiple images for inference
- **Model quantization**: INT8 quantized models for faster inference
- **Caching**: Redis cache for repeated queries
- **CDN**: Serve static assets from CDN

## Security

### Authentication

- JWT tokens with 15-minute expiry
- Refresh tokens stored in HTTP-only cookies
- Role-based access control (RBAC)

### Data Protection

- Input validation with Pydantic
- CORS policy for frontend origin
- Rate limiting per user/IP
- HTTPS/TLS for all communications

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for production deployment guides.
