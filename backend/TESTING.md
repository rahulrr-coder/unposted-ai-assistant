# API Testing Guide

## 🎯 Standard Practice Explained

### RESTful API Structure
```
GET    /api/todos          - List all todos (with optional filters)
GET    /api/todos/{id}     - Get single todo by ID
POST   /api/todos          - Create new todo
PUT    /api/todos/{id}     - Update existing todo
DELETE /api/todos/{id}     - Delete todo
```

### Authentication Flow
All `/api/todos` endpoints require authentication:
1. First register/login to get a JWT token
2. Include token in Authorization header for all requests

---

## 📝 Testing with Bruno

### Step 1: Register a User
**Endpoint:** `POST http://localhost:8000/auth/register`

**Body (JSON):**
```json
{
  "email": "test@example.com",
  "password": "TestPass123!",
  "full_name": "Test User"
}
```

**Expected Response (200):**
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "uuid-here",
    "email": "test@example.com"
  }
}
```

**Copy the `access_token`!** You'll need it for all todo requests.

---

### Step 2: Create a Todo
**Endpoint:** `POST http://localhost:8000/api/todos`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "title": "Test from API",
  "description": "Testing the backend",
  "status": "pending",
  "priority": "high"
}
```

**Expected Response (201):**
```json
{
  "id": 1,
  "user_id": "uuid-here",
  "title": "Test from API",
  "description": "Testing the backend",
  "status": "pending",
  "priority": "high",
  "created_at": "2025-11-01T11:00:00Z",
  "updated_at": "2025-11-01T11:00:00Z"
}
```

---

### Step 3: Get All Todos
**Endpoint:** `GET http://localhost:8000/api/todos`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Optional Query Parameters:**
- `?status=pending` - Filter by status
- `?priority=high` - Filter by priority
- `?status=pending&priority=high` - Combine filters

**Expected Response (200):**
```json
[
  {
    "id": 1,
    "user_id": "uuid-here",
    "title": "Test from API",
    "description": "Testing the backend",
    "status": "pending",
    "priority": "high",
    "created_at": "2025-11-01T11:00:00Z",
    "updated_at": "2025-11-01T11:00:00Z"
  }
]
```

---

### Step 4: Get Single Todo
**Endpoint:** `GET http://localhost:8000/api/todos/1`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Expected Response (200):**
```json
{
  "id": 1,
  "user_id": "uuid-here",
  "title": "Test from API",
  "description": "Testing the backend",
  "status": "pending",
  "priority": "high",
  "created_at": "2025-11-01T11:00:00Z",
  "updated_at": "2025-11-01T11:00:00Z"
}
```

---

### Step 5: Update Todo
**Endpoint:** `PUT http://localhost:8000/api/todos/1`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
Content-Type: application/json
```

**Body (JSON) - All fields optional:**
```json
{
  "status": "completed",
  "priority": "medium"
}
```

**Expected Response (200):**
```json
{
  "id": 1,
  "user_id": "uuid-here",
  "title": "Test from API",
  "description": "Testing the backend",
  "status": "completed",
  "priority": "medium",
  "created_at": "2025-11-01T11:00:00Z",
  "updated_at": "2025-11-01T11:05:00Z"
}
```

---

### Step 6: Delete Todo
**Endpoint:** `DELETE http://localhost:8000/api/todos/1`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Expected Response (204):**
No content - successful deletion

---

## 📋 Allowed Values

### Status Options:
- `pending` (default)
- `in_progress`
- `completed`
- `archived`

### Priority Options:
- `low`
- `medium` (default)
- `high`
- `urgent`

---

## 🔍 Common Errors

### 401 Unauthorized
**Cause:** Missing or invalid token
**Fix:** Include valid Bearer token in Authorization header

### 404 Not Found (Todo)
**Cause:** Todo doesn't exist or doesn't belong to you
**Fix:** Check the todo ID and ensure you're authenticated as the correct user

### 422 Validation Error
**Cause:** Invalid data (e.g., wrong status value)
**Fix:** Check allowed values for status/priority

### 500 Server Error
**Cause:** Database connection issue
**Fix:** Check Supabase connection and ensure migration is run

---

## 🎨 Standard Practice Summary

### 1. **Data Validation (Pydantic Models)**
- `TodoCreate` - For POST requests (required fields)
- `TodoUpdate` - For PUT requests (all optional)
- `TodoResponse` - For responses (includes ID, timestamps)

### 2. **Authentication & Authorization**
- JWT tokens via Supabase Auth
- All endpoints check `current_user`
- Users can only access their own todos

### 3. **RESTful Conventions**
- Proper HTTP methods (GET, POST, PUT, DELETE)
- Correct status codes (200, 201, 204, 404, 422, 500)
- Resource-based URLs (`/api/todos`, `/api/todos/{id}`)

### 4. **Error Handling**
- Try-catch blocks in all endpoints
- Specific error messages
- Logging for debugging

### 5. **Database Operations**
- Use Supabase client for all queries
- Filter by `user_id` for security
- Validate existence before update/delete

---

## 🚀 Interactive API Docs

Visit: http://localhost:8000/docs

Features:
- ✅ Try all endpoints
- ✅ See request/response schemas
- ✅ Authorize with token (click lock icon)
- ✅ Auto-generated from code
