from fastapi import FastAPI

from app.routers import ask, health  

app = FastAPI(
    title="Balabank AI API",
    description="API для поиска и ответа на вопросы по финансовым книгам",
    version="1.0.0"
)

app.include_router(ask.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Balabank AI API is running!"}
