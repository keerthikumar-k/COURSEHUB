# Complete Setup Guide

## Step-by-Step Instructions

### 1. Install Prerequisites

- **Node.js**: Download from https://nodejs.org (v18 or higher)
- **MongoDB**: Download from https://www.mongodb.com/try/download/community
- **Python** (optional): Download from https://www.python.org (v3.9+)

### 2. Start MongoDB

Windows:
```bash
# MongoDB should auto-start as a service after installation
# Or manually start:
net start MongoDB
```

Mac/Linux:
```bash
mongod --dbpath /path/to/data
```

### 3. Backend Setup

```bash
# Navigate to server folder
cd server

# Install dependencies
npm install

# Seed database with demo data
npm run seed

# Start development server
npm run dev
```

Server will run at: **http://localhost:5000**

### 4. Frontend Setup

Open a new terminal:

```bash
# Navigate to client folder
cd client

# Install dependencies
npm install

# Start development server
npm run dev
```

App will run at: **http://localhost:5173**

### 5. ML Service Setup (Optional)

Open a new terminal:

```bash
# Navigate to ml folder
cd ml

# Install Python dependencies
pip install -r requirements.txt

# Train the recommendation model
python train.py

# Start FastAPI server
uvicorn app:app --reload --port 8000
```

ML API will run at: **http://localhost:8000**

## Access the Application

1. Open browser: **http://localhost:5173**
2. Login with demo accounts:
   - **Admin**: admin@demo.com / demo123
   - **Student**: student@demo.com / demo123

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running
- Check connection string in `server/.env`

### Port Already in Use
- Change PORT in `.env` files
- Or kill process using the port

### Module Not Found
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again

## Production Build

### Frontend
```bash
cd client
npm run build
# Output in client/dist
```

### Backend
```bash
cd server
npm start
```

## Environment Variables

### server/.env
```
PORT=5000
MONGO_URI=mongodb://localhost:27017/course_management
JWT_SECRET=your_super_secret_jwt_key_change_in_production
ML_API_URL=http://localhost:8000
```

### client/.env
```
VITE_API_URL=http://localhost:5000/api
```

### ml/.env
```
MONGO_URI=mongodb://localhost:27017/course_management
PORT=8000
```
