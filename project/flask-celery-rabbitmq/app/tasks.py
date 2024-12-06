import random, time
from celery import Celery
import uuid
from . import connection
from flask import jsonify


CELERY_BROKER_URL = 'pyamqp://flask:admin@rabbitmq'
CELERY_RESULT_BACKEND = 'db+mysql+pymysql://user:123456@db:3306/celery'

celery = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

@celery.task
def add(x, y):
    sql = "INSERT INTO `post` (`id`, `name`) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (
        1,
        str(uuid.uuid4()),
    ))
    connection.commit()

    if cursor.rowcount > 0:
        return jsonify({'success': 'Delete'})
    else:
        return jsonify({'error': 'Error'}), 404
