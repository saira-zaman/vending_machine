# Vending Machine API

A FastAPI-based REST API for a vending machine system, ready for deployment on Vercel.

## Features

- ✅ FastAPI REST API
- ✅ Health check endpoint
- ✅ Items listing
- ✅ Purchase functionality
- ✅ CORS enabled
- ✅ Ready for Vercel deployment

## Local Setup

### Requirements
- Python 3.9+

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/items` - Get available items
- `POST /api/purchase` - Purchase an item

## Deployment on Vercel

### Prerequisites
- Vercel account
- Git repository

### Steps

1. Push your code to GitHub
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "New Project"
4. Select your GitHub repository
5. Vercel will automatically detect Python and configure the deployment
6. Click "Deploy"

The API will be live at `https://your-project.vercel.app`

## Environment Variables

Add in Vercel dashboard if needed. Currently no environment variables required.

## License

MIT
