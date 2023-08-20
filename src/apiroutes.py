from fastapi import FastAPI, status, Depends
from orm import SessionLocal
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "this is our homepage"}


@app.get("/catalogue")
async def get_all_items():
    ...


@app.get("/men")
async def get_item_men():
    ...


@app.get("/women")
async def get_item_women():
    ...

@app.get("/kids")
async def get_item_kids():
    ...

