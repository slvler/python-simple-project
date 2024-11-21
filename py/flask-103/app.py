from flask import Flask
from src.routes.product import productBp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(productBp, url_prefix='/product')

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)