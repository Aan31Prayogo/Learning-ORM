from fastapi import FastAPI, HTTPException, Depends
from models.model import RequestModel
from database.database import get_db, check_table
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "world"}


if __name__ == '__main__':
    check_table()
    uvicorn.run(app,host='0.0.0.0', port = 5000)