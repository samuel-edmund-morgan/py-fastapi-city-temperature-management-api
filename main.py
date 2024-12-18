from fastapi import FastAPI

import city.router

app = FastAPI()

app.include_router(city.router.router)

