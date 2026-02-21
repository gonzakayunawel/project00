FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app


COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-cache --no-dev

COPY main.py ./

# The following environment variables are required to run the application:
# DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
EXPOSE 3000

# Assumes `fastmcp run` is the correct command to start the server.
# This may need to be adjusted based on FastMCP's documentation.
CMD ["uv", "run", "fastmcp", "run", "main.py:app"]