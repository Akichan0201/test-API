from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def items():
    return {'status' : 'lajang',
            'message1' : 'hello dunia tipu-tipu',
            'name' : 'adzkia',
            'message' : 'apa lo liat - liat?!'}

@app.get("/items/{new}")
async def items(new):   
    return {'new' : new}

@app.get("/items/books")
async def books():
    return {'book' : 'Harry Potter'}
