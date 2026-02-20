import os
from typing import List, Dict, Any, Optional, cast
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor, RealDictRow
from fastmcp import FastMCP

app = FastMCP("company-db-server")

def get_db_connection():
    db_port = os.environ.get("DB_PORT")
    if db_port is None:
        raise ValueError("DB_PORT environment variable not set")
    conn = psycopg2.connect(
        host = os.environ.get("DB_HOST"),
        port = int(db_port),
        user = os.environ.get("DB_USER"),
        password = os.environ.get("DB_PASSWORD"),
        database = os.environ.get("DB_NAME"),
        cursor_factory= RealDictCursor
    )
    return conn

@app.tool
def list_employees(limit: int = 5):
    """Listar los empleados"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, name, position, department, salary, hire_date
            FROM employees
            ORDER BY id
            LIMIT %s
            """,
            (limit, )
        )
        rows: List[RealDictRow] = cast(List[RealDictRow], cursor.fetchall())
        employees = []

        for row in rows:
            employees.append({
                "id": row['id'],
                "name": row['name'],
                "position": row['position'],
                "department": row['department'],
                "salary": float(row['salary']),
                "hire_date": str(row['hire_date'])
            })
        cursor.close()
        conn.close()
        return employees
    except Exception as e:
        return {
            "error": f"Error al obtener los "
        }


def main():
    print("Hello from project00!")


if __name__ == "__main__":
    main()
