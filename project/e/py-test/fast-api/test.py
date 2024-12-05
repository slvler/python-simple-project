
from fastapi import FastAPI, Query, Path
from router.product_router import product_api_router

app = FastAPI()


app.include_router(product_api_router)



