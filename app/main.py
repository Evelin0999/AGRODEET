from fastapi import FastAPI
from . import models, database
from .routers import posts, users, comments, interactions, reports, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AGRODEET API")

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(comments.router)
app.include_router(interactions.router)
app.include_router(reports.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"msg": "Bienvenido a la API de AGRODEET 🌱"}
