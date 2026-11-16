FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uv run --no-sync python manage.py migrate --noinput && uv run --no-sync python manage.py collectstatic --noinput && exec uv run --no-sync gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
