FROM python:3.12.3-slim-bookworm

RUN apt-get update && apt-get install --no-install-recommends -y curl

# Python settings
ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # PIP settings
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry settings
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VENV_PATH="/priscillafx/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -

# Copy project files
RUN mkdir /priscillafx
WORKDIR /priscillafx
COPY . .

# Install dependencies
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# Expose
EXPOSE 8000

# Startup
WORKDIR src
CMD ["poetry", "run", "gunicorn", "--config=gunicorn_conf.py", "main:app"]