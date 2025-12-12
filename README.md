# Organization-Management-service
Multi-tenant Organization Management Service built with FastAPI and MongoDB
# Organization Management Service

## Overview
The **Organization Management Service** is a backend application built using **FastAPI** and **MongoDB** that enables creating and managing organizations using a **multi-tenant architecture**.

Each organization is provisioned with its own isolated MongoDB collection, while a **master database** maintains global metadata and admin user information. The service includes secure authentication using **JWT** and follows clean, modular backend design principles.

---

## Tech Stack
- **FastAPI** – Backend framework
- **MongoDB** – Database (Master DB + tenant collections)
- **PyMongo** – MongoDB client
- **JWT (JSON Web Tokens)** – Authentication
- **bcrypt** – Password hashing
- **Pydantic** – Request validation and schema definition

---

## Architecture Overview
The application uses a **multi-tenant design** with the following components:

### Master Database
Stores:
- Organization metadata
- Admin user credentials (hashed)
- Mapping between organizations and their tenant collections

### Tenant Collections
- Each organization has its own MongoDB collection
- Naming pattern: `org_<organization_name>`
- Ensures strong tenant isolation

---

## High-Level Architecture Diagram


    Client -->|REST + JWT| FastAPI
    FastAPI --> Auth[Auth Module]
    FastAPI --> Org[Organization Service]
    Org --> MasterDB[Master DB]
    Org --> TenantDB[Tenant Collections]


---

## API Endpoints

| Method | Endpoint       | Description                                   | Auth Required |
|------|------------------|-----------------------------------------------|---------------|
| POST | `/org/create`    | Create a new organization                     |  No           |
| GET  | `/org/get`       | Fetch organization details                    |  No           |
| PUT  | `/org/update`    | Update organization name & migrate data       |  Yes          |
| DELETE | `/org/delete`  | Delete organization and tenant collection     |  Yes          |
| POST | `/admin/login`   | Admin login and JWT token generation          |  No           |

---

## Authentication & Security
- Admin authentication uses **JWT**
- Passwords are hashed using **bcrypt**
- JWT tokens are required for protected endpoints
- Only the authenticated admin can update or delete their organization

---

## Design Choices & Rationale

### FastAPI
FastAPI was chosen for its high performance, built-in request validation, and automatic API documentation using Swagger/OpenAPI.

---

### Multi-Tenant Architecture
The system uses a **master database** for global metadata and **separate collections** for each organization to ensure data isolation and security.

---

### Dynamic Collection Creation
Tenant collections are created dynamically during organization onboarding, reflecting real-world SaaS multi-tenant systems.

---

### Modular Design
The application follows a clean separation of concerns:
- **Routes** – Handle HTTP requests
- **Services** – Business logic
- **Core** – Configuration, database, and security
- **Utils** – Helper utilities

This structure improves maintainability and testability.

---

### Scalability Considerations
Dynamic collections provide strong isolation but may become inefficient at very large scale.  
A shared collection model with `tenant_id` indexing and sharding could be a more scalable alternative in future iterations.

---

## Running the Application

### Prerequisites
- Python 3.9+
- MongoDB running locally or remotely

### Steps
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
