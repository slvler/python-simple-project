from flask import Blueprint
from src.controllers.productContoller import index


productBp = Blueprint('product', __name__)

productBp.route('/', methods=["GET"])(index)
