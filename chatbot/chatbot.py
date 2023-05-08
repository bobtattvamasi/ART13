import os
from redis import Redis
from time import sleep
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_db = int(os.getenv("REDIS_DB", 0))

redis = Redis(host=redis_host, port=redis_port, db=redis_db)

while True:
    # logic for chatbot service
    sleep(10)