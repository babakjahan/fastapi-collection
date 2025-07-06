# Sample FastAPI application for deployment in the production

## 📋 Requirements

- Python 3.13+
- FastAPI
- uv (optional, for faster workflows)

## Create and activate virtual environment

- first install UV in your machine

- then create an environment

```
uv venv

source .venv/bin/activate
```


## Sync the project's dependencies with the environment

```
uv sync
```

## Freeze the project's dependencies in requirements.txt file

```
uv pip freeze > requirements.txt
```

## Run the app

### Run the app with unicorn command in development mode

```
uvicorn app:app --reload
```

### Run the app with UV command in development mode

```
uv run fastapi dev
```

### Run server directly

```
python3 server.py
```

#### Production Mode

```
fastapi run
```

## Build docker file

```
docker build -t fastapi-production-app .
```

## Run docker container

```
docker run -p 8080:8080 fastapi-production-app
```