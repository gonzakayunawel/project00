# Company DB Server

This project is a FastMCP server application that provides tools to interact with a company's employee database. It allows for listing and adding employees through a simple tool-based API.

## Features

*   **List Employees:** Fetch a paginated list of employees from the database.
*   **Add Employee:** Add a new employee to the database with validation for required fields.

## Technologies Used

*   **Python 3.13+**
*   **Docker & Docker Compose**
*   **FastMCP:** The core framework for creating the tool server.
*   **PostgreSQL:** The database used to store employee data.
*   **Psycopg2:** The PostgreSQL adapter for Python.

## Local Deployment with Docker (Recommended)

This is the easiest way to get the entire environment, including the database and the application, up and running.

### Prerequisites

*   Docker
*   Docker Compose

### Running the Application

1.  **Start the services:**
    From the root of the project, run the following command:
    ```bash
    docker-compose up --build
    ```
    This command will:
    *   Build the Docker image for the FastMCP application.
    *   Start a PostgreSQL database container.
    *   Start the FastMCP server container.
    *   Initialize the database with the schema and sample data from `init.sql`.

2.  **Access the server:**
    The FastMCP server will be running and accessible. The API will be available on port `3000`. The PostgreSQL database will be available on port `5432` on your local machine.

### Stopping the Application

To stop all the running containers, press `Ctrl+C` in the terminal where `docker-compose` is running, or run the following command from another terminal:
```bash
docker-compose down
```

## Manual Local Setup

If you prefer to run the application without Docker, you can follow these steps.

### Prerequisites

*   Python 3.13 or higher
*   An accessible PostgreSQL database instance.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd project00
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management. Install the required packages from `pyproject.toml`:
    ```bash
    uv pip install -e .
    ```

### Configuration

The application requires the following environment variables to be set for the database connection:

*   `DB_HOST`: The hostname of your PostgreSQL server.
*   `DB_PORT`: The port of the database server (e.g., `5432`).
*   `DB_USER`: The username for the database connection.
*   `DB_PASSWORD`: The password for the database connection.
*   `DB_NAME`: The name of the database to connect to.

### Running the Application

To start the FastMCP server, run the following command in your terminal:

```bash
fastmcp run main.py:app
```

## Available Tools

### `list_employees(limit: int = 5)`

Lists the employees from the database.

*   **Parameters:**
    *   `limit` (optional): The maximum number of employees to return. Defaults to `5`.
*   **Returns:**
    *   A list of employee objects on success.
    *   A dictionary with an `error` key on failure.

### `add_employees(name: str, position: str, department: str, salary: float, hire_date: Optional[str] = None)`

Adds a new employee to the database.

*   **Parameters:**
    *   `name`: The full name of the employee.
    *   `position`: The employee's job position.
    *   `department`: The department the employee belongs to.
    *   `salary`: The employee's salary.
    *   `hire_date` (optional): The hiring date in `YYYY-MM-DD` format. Defaults to the current date if not provided.
*   **Returns:**
    *   A dictionary with a `success` key and the new employee's data.
    *   A dictionary with an `error` key on failure.
