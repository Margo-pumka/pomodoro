import os

from dotenv import load_dotenv

bind = "0.0.0.0:8000"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
env = os.path.join(os.getcwd(), ".local.env")
load_dotenv(env)