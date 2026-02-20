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
        host=os.environ.get("DB_HOST"),
        port=int(db_port),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        cursor_factory=RealDictCursor,
    )
    return conn


@app.tool
def list_employees(limit: int = 5) -> List[Dict[str, Any]] | Dict:
    """
    Devuelve una lista de diccionarios de los empleados con 5 elementos, la
    cual es la cantidad por defecto, o la cantidad especificada mediante el
    parámetro 'limit'.
    Si hay un error se devuelve un diccionario con el error.
    """
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
            (limit,),
        )
        rows: List[RealDictRow] = cast(List[RealDictRow], cursor.fetchall())
        employees = []

        for row in rows:
            employees.append(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "position": row["position"],
                    "department": row["department"],
                    "salary": float(row["salary"]),
                    "hire_date": str(row["hire_date"]),
                }
            )
        cursor.close()
        conn.close()
        return employees

    except Exception as e:
        return {"error": f"Error al obtener los empleados {str(e)}"}


@app.tool
def add_employees(
    name: str,
    position: str,
    department: str,
    salary: float,
    hire_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Agrega un nuevo empleado a la base de datos
    """
    try:
        if not name.strip():
            return {"error": "El nombre es un campo requerido."}

        if salary <= 0:
            return {"error": "El salario debe ser mayor a 0."}

        if not hire_date:
            hire_date = datetime.now().strftime("%Y-%m-%d")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO employees (
                name,
                position,
                department,
                salary,
                hire_date
                )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, name, position, department, salary, hire_date
            """,
            (name.strip(), position.strip(), department.strip(), salary, hire_date),
        )
        new_employee: RealDictRow | None = cast(RealDictRow | None, cursor.fetchone())
        conn.commit()

        cursor.close()
        conn.close()

        if new_employee:
            return {
                "success": True,
                "employee": {
                    "id": new_employee["id"],
                    "name": new_employee["name"],
                    "position": new_employee["position"],
                    "department": new_employee["department"],
                    "salary": float(new_employee["salary"]),
                    "hire_date": str(new_employee["hire_date"]),
                },
            }

        return {"error": "Error al crear al nuevo empleado."}

    except Exception as e:
        return {"error": f"Error al agregar al empleado {str(e)}"}
