from flask import Flask
from app.tasks import add
from . import connection

app = Flask(__name__)


@app.route('/')
def index():
    cursor = connection.cursor()
    posts_query = "SELECT * FROM post"
    cursor.execute(posts_query)
    post_result = cursor.fetchall()
    return post_result


@app.route('/test-mail')
def test_mail():
    add.delay(12,33)
    return "test-mail"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)