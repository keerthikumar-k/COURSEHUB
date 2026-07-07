# CourseHub - Web-Based Course Registration & Management System

A full-stack web application with React + Node.js + MongoDB + Python ML recommendations.

## Project Structure

```
FSD/
├── client/          → React + Vite + Tailwind frontend
├── server/          → Node.js + Express + MongoDB backend
└── ml/              → Python FastAPI ML recommendation service
```

## Quick Start

### Prerequisites
- Node.js v18+
- MongoDB running on port 27017
- Python 3.9+ (optional, for ML service)

### 1. Backend Setup

```bash
cd server
npm install
npm run seed      # Seeds demo data + accounts
npm run dev       # Starts on http://localhost:5000
```

### 2. Frontend Setup

```bash
cd client
npm install
npm run dev       # Starts on http://localhost:5173
```

### 3. ML Service (Optional)

```bash
cd ml
pip install -r requirements.txt
python train.py           # Train the model
uvicorn app:app --reload --port 8000
```

## Demo Accounts

| Role    | Email              | Password |
|---------|--------------------|----------|
| Admin   | admin@demo.com     | demo123  |
| Student | student@demo.com   | demo123  |

## Features

### Student
- Browse & search courses with filters
- Enroll/unenroll from courses
- Track learning progress
- AI-powered course recommendations
- Dashboard with charts

### Admin
- Full course CRUD management
- View all students
- Monitor all enrollments
- Analytics dashboard with charts

## API Endpoints

| Method | Endpoint                        | Access  |
|--------|---------------------------------|---------|
| POST   | /api/auth/register              | Public  |
| POST   | /api/auth/login                 | Public  |
| GET    | /api/courses                    | Auth    |
| POST   | /api/courses                    | Admin   |
| PUT    | /api/courses/:id                | Admin   |
| DELETE | /api/courses/:id                | Admin   |
| POST   | /api/enrollments                | Student |
| GET    | /api/enrollments/my             | Student |
| DELETE | /api/enrollments/:courseId      | Student |
| PUT    | /api/enrollments/:courseId/progress | Student |
| GET    | /api/admin/stats                | Admin   |
| GET    | /api/admin/students             | Admin   |
| GET    | /api/admin/enrollments          | Admin   |
| GET    | /api/recommendations            | Auth    |
