from fastapi import FastAPI

app = FastAPI()


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

