# Gunicorn configs
import multiprocessing


bind: str = "0.0.0.0:8080" #! change to your desired host and port
workers: int = multiprocessing.cpu_count() * 2 + 1
# worker_class: str = "uvicorn.workers.UvicornWorker" #! legacy import
worker_class: str = "uvicorn_worker.UvicornH11Worker"
keepalive = 24 * 60 * 60
