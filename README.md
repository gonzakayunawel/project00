# Company DB Server

This project is a FastMCP server application that provides tools to interact with a company's employee database. It allows for listing and adding employees through a simple tool-based API.

## Features

*   **List Employees:** Fetch a paginated list of employees from the database.
*   **Add Employee:** Add a new employee to the database with validation for required fields.

## Technologies Used

*   **Python 3.13+**
*   **FastMCP:** The core framework for creating the tool server.
*   **PostgreSQL:** The database used to store employee data.
*   **Psycopg2:** The PostgreSQL adapter for Python.

## Getting Started

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

You can set these in your shell or use a `.env` file.

### Database Schema

The application expects an `employees` table with the following structure:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    department VARCHAR(255),
    salary NUMERIC(10, 2),
    hire_date DATE
);
```

### Running the Application

To start the FastMCP server, run the following command in your terminal:

```bash
# TODO: Confirm the exact run command for a FastMCP server.
# It might be something like this:
fastmcp run
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
