# Project Overview

This is a Python project that uses the FastMCP framework to create a server application. The application connects to a PostgreSQL database to manage and retrieve employee data.

**Key Technologies:**

*   **Python:** The core programming language.
*   **FastMCP:** A framework for building and running server applications with tools.
*   **Psycopg2:** A PostgreSQL adapter for Python, used for database interaction.

**Architecture:**

*   `main.py`: The main application file, which initializes the FastMCP app and defines the `list_employees` tool.
*   `pyproject.toml`: Defines project metadata and dependencies.
*   **Database:** The application connects to a PostgreSQL database, which is expected to have an `employees` table.

# Building and Running

## Installation

The project's dependencies are listed in the `pyproject.toml` file. You can install them using a Python package manager like `pip` or `uv`.

```bash
# Using pip
pip install -e .

# Using uv
uv pip install -e .
```

## Configuration

The database connection is configured using the following environment variables:

*   `DB_HOST`: The hostname of the database server.
*   `DB_PORT`: The port of the database server.
*   `DB_USER`: The username for the database connection.
*   `DB_PASSWORD`: The password for the database connection.
*   `DB_NAME`: The name of the database.

You can set these variables in your shell or using a `.env` file.

## Running the Application

To run the FastMCP server, use the following command:

```bash
# TODO: Verify the exact run command for FastMCP
fastmcp run
```

# Development Conventions

*   **Dependency Management:** Dependencies are managed using `pyproject.toml`. Any new dependencies should be added to this file.
*   **Type Hinting:** The code uses type hints for function signatures. Please use type hints in new code.
*   **Tools:** New functionality should be exposed as tools using the `@app.tool` decorator from the FastMCP framework.
