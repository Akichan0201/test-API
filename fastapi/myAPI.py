from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "This is first API"}

@app.get('/hello')
async def hello():
    return {'name': 'Adzkia',
            'birthday': '02-01-2006',
            'age': 19,
            'hobby': 'playing guitar, drawing, dancing, listening to music'}

@app.get('/hello/major')
async def major():
    return {'major 1': 'Social',
            'major 2': 'english',
            'major 3': 'progamming and Coding'}

@app.get('/hello/{me}')
async def hello(me):
    return {'message': f'hello {me}'}