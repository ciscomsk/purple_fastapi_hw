@a_default:
    just --list

@dev:
    uv run fastapi dev src/purple_fastapi_hw/main.py

@lint:
    uv run ruff check --fix

@format:
    uv run ruff format