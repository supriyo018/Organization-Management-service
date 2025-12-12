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

```md
```mermaid
graph TD
    Client -->|REST + JWT| FastAPI
    FastAPI --> Auth[Auth Module]
    FastAPI --> Org[Organization Service]
    Org --> MasterDB[Master DB]
    Org --> TenantDB[Tenant Collections]
