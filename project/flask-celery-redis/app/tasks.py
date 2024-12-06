import random, time
from celery import Celery

# Celery uygulaması
celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task
def add(x, y):
    y = random.randint(0,2)
    if y == 1:
        return x + y
    else:
        print("sleep")
        time.sleep(15)
        return x + y

