import pymysql

connection = pymysql.connect(
    host='db',
    user='user',
    password='123456',
    database='celery',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
