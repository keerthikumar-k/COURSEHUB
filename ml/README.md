# ML Recommendation Module

## Setup

```bash
cd ml
pip install -r requirements.txt
```

## Train the Model

Make sure MongoDB is running and has course data (run seed.js first), then:

```bash
python train.py
```

## Run the API

```bash
uvicorn app:app --reload --port 8000
```

API runs at: http://localhost:8000

## Endpoints

- `POST /recommend` - Get course recommendations
- `GET /health` - Check service health
