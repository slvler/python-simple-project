from controller.productController import controllerIndex
from models.productModel import prodIndex
from views.prod import testFunc

def routeIndex():
    prodIndex()
    controllerIndex()
    testFunc()

    print("route - index")
    print("1")