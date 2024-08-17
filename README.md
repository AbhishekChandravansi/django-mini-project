# Django Project with DRF - Client and Project Management

## Overview

This Django project provides an API to manage clients and projects. Each client can have multiple projects, and each project can be assigned to multiple users. 
The API restricts project visibility based on the client selected and provides detailed serialization for better API responses.

## Features

- **Clients Management**: Create and view clients.
- **Projects Management**: Create and view projects, with assignment to specific clients and users.
- **User Authentication**: Only authenticated users can access the API.
- **Dynamic API Responses**: Projects associated with a client are only shown when a specific client ID is provided.

## Endpoints

### Clients

- **GET `/clients/`**: Retrieve a list of clients. Projects are not included in the response.
- **GET `/clients/<id>/`**: Retrieve details of a specific client by ID. The client's projects are included in the response.
- **POST `/clients/`**: Create a new client.

### Projects

- **GET `/projects/`**: Retrieve a list of projects assigned to the logged-in user.
- **GET `/projects/<id>/`**: Retrieve details of a specific project by ID.
- **POST `/projects/`**: Create a new project.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework


### Models

#### `Client` Model

- `id`: Primary key.
- `client_name`: Name of the client.
- `created_at`: Timestamp when the client was created.
- `created_by`: User who created the client.
- `updated_at`: Timestamp when the client was last updated.
- `updated_by`: User who last updated the client.
- `projects`: Related projects (automatically handled by Django).

#### `Project` Model

- `id`: Primary key.
- `project_name`: Name of the project.
- `client`: ForeignKey to the `Client` model.
- `users`: ManyToManyField related to the `User` model.
- `created_at`: Timestamp when the project was created.
- `created_by`: User who created the project.

### Serializers

#### `ClientSerializer`

- Nested serializer for `projects` if a client ID is provided.
- Displays the `created_by` and `updated_by` as usernames.

#### `ProjectSerializer`

- Nested serializer for `users`.
- Dynamically includes or excludes fields (`users` and `assigned_to`) based on the request method.

### Custom Logic

- **Project Visibility**: Projects are only shown in the client details if a client ID is specified in the request.
- **User Details**: When creating a project, user details are shown with `id` and `username`.

### Security

- **Authentication**: The API requires authentication using Django's built-in authentication system. Only authenticated users can access the endpoints.

### Example API Requests

#### Create a Client

```bash
