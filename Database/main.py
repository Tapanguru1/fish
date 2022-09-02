from fastapi import FastAPI
from sqlalchemy.sql.functions import mode
from .import models
from .database import engine 

app= FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/')
def fun():
    return {"Running"} 