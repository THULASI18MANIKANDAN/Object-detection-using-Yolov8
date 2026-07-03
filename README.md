# 🚀 Real-Time Object Detection Platform (v2 - Modern Tech Stack)

A production-ready object detection platform built with modern technologies. Supports real-time video streaming, image uploads, model training, and easy deployment.

## 🎯 Features

- **Real-Time Detection**: Live webcam streaming with WebRTC
- **Image Upload**: Process static images with YOLOv8
- **Model Training**: Fine-tune on custom datasets
- **REST API**: FastAPI backend with async/await
- **Modern UI**: React 18 with TypeScript and TailwindCSS
- **Production Ready**: Docker, K8s ready, monitoring included
- **Scalable**: Horizontal scaling with Redis caching

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     Frontend (React 18)                      │
│         Real-time UI + WebRTC Video Streaming               │
└──────────────────────┬───────────────────────────────────────┘
                       │ HTTP/WebSocket
┌──────────────────────▼───────────────────────────────────────┐
│                  Backend (FastAPI)                           │
│         REST API + WebSocket + Model Serving                │
├──────────────────────────────────────────────────────────────┤
│  Inference Engine (ONNX) │ Training Pipeline │ DB Layer     │
└──────────────────────┬───────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   PostgreSQL       Redis         MinIO/S3
   (Results)       (Cache)     (Model Storage)
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for local frontend development)

### Development Setup

```bash
# Clone and checkout the branch
git clone https://github.com/THULASI18MANIKANDAN/Object-detection-using-Yolov8.git
cd Object-detection-using-Yolov8
git checkout rebuild/modern-tech-stack

# Start services with Docker Compose
docker-compose up -d

# Wait for services to be ready
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development (Without Docker)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
.
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── main.py            # FastAPI app entry
│   │   ├── api/               # API routes
│   │   ├── core/              # Config, logging, security
│   │   ├── ml/                # Inference & preprocessing
│   │   └── db/                # Database models & CRUD
│   ├── training/              # PyTorch Lightning training
│   ├── tests/                 # Unit & integration tests
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/                   # React 18 application
│   ├── src/
│   │   ├── components/        # Reusable React components
│   │   ├── pages/             # Page components
│   │   ├── api/               # API client
│   │   ├── hooks/             # Custom React hooks
│   │   └── main.tsx
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml          # Multi-container setup
├── .github/workflows/          # CI/CD pipelines
└── docs/                       # Documentation
```

## 📚 Documentation

- [API Documentation](./docs/API.md)
- [Architecture Guide](./docs/ARCHITECTURE.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)

## 🔧 Technology Stack

### Backend
- **FastAPI** - Modern async Python web framework
- **PyTorch Lightning** - Streamlined ML training
- **ONNX Runtime** - Fast inference
- **SQLAlchemy** - ORM for database
- **Pydantic** - Data validation

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **WebRTC** - Real-time video

### Infrastructure
- **Docker & Docker Compose** - Containerization
- **PostgreSQL** - Primary database
- **Redis** - Caching layer
- **GitHub Actions** - CI/CD

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/

# Frontend tests
cd frontend
npm run test
```

## 📦 Deployment

See [DEPLOYMENT.md](./docs/DEPLOYMENT.md) for guides on:
- AWS ECS
- Kubernetes
- Docker Swarm
- GCP Cloud Run

## 🤝 Contributing

1. Create a feature branch from `develop`
2. Make your changes
3. Ensure tests pass
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🙋 Support

For issues and questions, please open a GitHub issue.
