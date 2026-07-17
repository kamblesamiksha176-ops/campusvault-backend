# CampusVault API Documentation

## Base URL

```
http://localhost:8000/api
```

## Authentication

All endpoints except `/auth/register` and `/auth/login` require a Bearer token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

---

## Auth Endpoints

### Register
```
POST /auth/register
Content-Type: application/json

{
  "name": "Amit Kumar",
  "email": "amit@example.com",
  "password": "password123",
  "phone": "9876543210",
  "college": "XYZ Institute",
  "branch": "Computer Science",
  "semester": 4
}

Response: 200 OK
{
  "access_token": "jwt_token",
  "token_type": "bearer",
  "user": {
    "uid": "user_id",
    "name": "Amit Kumar",
    "email": "amit@example.com",
    "role": "student",
    "subscription": false,
    "emailVerified": false,
    "createdAt": "2024-01-15T10:30:00"
  }
}
```

### Login
```
POST /auth/login
Content-Type: application/json

{
  "email": "amit@example.com",
  "password": "password123"
}

Response: 200 OK
{
  "access_token": "jwt_token",
  "token_type": "bearer",
  "user": {...}
}
```

### Verify Token
```
GET /auth/verify-token
Authorization: Bearer <token>

Response: 200 OK
{
  "email": "amit@example.com",
  "valid": true
}
```

### Forgot Password
```
POST /auth/forgot-password
Content-Type: application/json

{
  "email": "amit@example.com"
}

Response: 200 OK
{
  "message": "Password reset link sent to email"
}
```

### Logout
```
POST /auth/logout
Authorization: Bearer <token>

Response: 200 OK
{
  "message": "Logged out successfully"
}
```

---

## Resource Endpoints

### Get All Resources
```
GET /resources/all?skip=0&limit=10
Authorization: Bearer <token>

Response: 200 OK
{
  "resources": [
    {
      "documentId": "resource_id",
      "title": "Data Structures",
      "description": "Complete guide to data structures",
      "subject": "Computer Science",
      "branch": "CSE",
      "semester": 4,
      "type": "notes",
      "fileUrl": "https://...",
      "uploadedBy": "Prof. John",
      "premium": false,
      "downloads": 45,
      "views": 120,
      "createdAt": "2024-01-15T10:30:00"
    }
  ],
  "total": 150,
  "skip": 0,
  "limit": 10
}
```

### Search Resources
```
GET /resources/search?subject=DataStructures&branch=CSE&semester=4&search_term=sorting
Authorization: Bearer <token>

Response: 200 OK
{
  "resources": [...]
}
```

### Get Resource by ID
```
GET /resources/{resource_id}
Authorization: Bearer <token>

Response: 200 OK
{
  "documentId": "resource_id",
  ...
}
```

### Upload Resource
```
POST /resources/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

Form Data:
- title: "Advanced Algorithms"
- description: "Complete guide to algorithms"
- subject: "Computer Science"
- branch: "CSE"
- semester: 4
- resource_type: "notes"
- premium: false
- file: <binary_file>

Response: 201 Created
{
  "message": "File uploaded successfully",
  "resourceId": "new_resource_id"
}
```

### Delete Resource
```
DELETE /resources/{resource_id}
Authorization: Bearer <token>

Response: 200 OK
{
  "message": "Resource deleted"
}
```

### Update Resource
```
PUT /resources/{resource_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated description",
  ...
}

Response: 200 OK
{
  "message": "Resource updated"
}
```

---

## AI Endpoints

### Chat with AI
```
POST /ai/chat
Authorization: Bearer <token>
Content-Type: application/json

{
  "message": "What is binary search?",
  "context": "Optional context"
}

Response: 200 OK
{
  "response": "Binary search is an efficient algorithm...",
  "timestamp": "2024-01-15T10:30:00"
}
```

### Generate Quiz
```
POST /ai/generate-quiz
Authorization: Bearer <token>
Content-Type: application/json

{
  "topic": "Data Structures",
  "number_of_questions": 10
}

Response: 200 OK
{
  "message": "Quiz generated",
  "topic": "Data Structures",
  "questions": [...]
}
```

### Explain Topic
```
POST /ai/explain
Authorization: Bearer <token>
Content-Type: application/json

{
  "topic": "Binary Search Tree"
}

Response: 200 OK
{
  "topic": "Binary Search Tree",
  "explanation": "A binary search tree is a tree where..."
}
```

### Summarize PDF
```
POST /ai/summarize
Authorization: Bearer <token>
Content-Type: application/json

{
  "file_url": "https://..."
}

Response: 200 OK
{
  "message": "Summarization in progress",
  "fileUrl": "https://..."
}
```

### Generate Learning Roadmap
```
POST /ai/roadmap
Authorization: Bearer <token>
Content-Type: application/json

{
  "topic": "Web Development"
}

Response: 200 OK
{
  "topic": "Web Development",
  "roadmap": ["Learn HTML", "Learn CSS", "Learn JavaScript", ...]
}
```

### Get Code Help
```
POST /ai/code-help
Authorization: Bearer <token>
Content-Type: application/json

{
  "code": "def sort(arr):\n    return arr",
  "language": "python"
}

Response: 200 OK
{
  "help": "This function needs to implement a sorting algorithm..."
}
```

### Get Exam Tips
```
POST /ai/exam-tips
Authorization: Bearer <token>
Content-Type: application/json

{
  "subject": "Data Structures"
}

Response: 200 OK
{
  "subject": "Data Structures",
  "tips": "1. Practice coding problems...\n2. Understand complexity analysis..."
}
```

---

## Admin Endpoints

### Get All Users
```
GET /admin/users?skip=0&limit=10
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "users": [...],
  "total": 250
}
```

### Delete User
```
DELETE /admin/users/{user_id}
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "message": "User deleted"
}
```

### Deactivate User
```
PUT /admin/users/{user_id}/deactivate
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "message": "User deactivated"
}
```

### Activate User
```
PUT /admin/users/{user_id}/activate
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "message": "User activated"
}
```

### Get Analytics
```
GET /admin/analytics
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "totalStudents": 2145,
  "totalTeachers": 89,
  "premiumUsers": 456,
  "totalResources": 1234,
  "totalDownloads": 5678
}
```

### Get Subscriptions
```
GET /admin/subscriptions
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "subscriptions": [...]
}
```

### Update Settings
```
PUT /admin/settings
Authorization: Bearer <admin_token>
Content-Type: application/json

{
  "aiEnabled": true,
  "maintenanceMode": false,
  ...
}

Response: 200 OK
{
  "message": "Settings updated"
}
```

---

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Invalid token or token expired"
}
```

### 403 Forbidden
```json
{
  "detail": "You don't have permission for this action"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Rate Limiting

- 100 requests per minute per user
- 10 uploads per hour
- 50 AI requests per hour (premium users: unlimited)

---

## Pagination

Default limit: 10 items per page
Maximum limit: 100 items per page

```
GET /resources/all?skip=0&limit=20

skip: Number of items to skip
limit: Number of items to return
```

---

## Interactive API Documentation

Visit `/docs` for interactive Swagger UI
Visit `/redoc` for ReDoc documentation
