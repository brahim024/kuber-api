# Kubernetes Test API

A simple FastAPI application for testing Kubernetes deployment.

## Features

- RESTful API with Swagger documentation
- Health check endpoint
- CRUD operations for items
- Ready for Kubernetes deployment

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `GET /items`: List all items
- `POST /items`: Create a new item
- `GET /items/{item_id}`: Get a specific item

## Example Usage

Create a new item:
```bash
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Item", "description": "This is a test item"}'
```

Get all items:
```bash
curl "http://localhost:8000/items"
``` # kuber-api
