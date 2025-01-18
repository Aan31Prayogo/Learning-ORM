from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.model import RequestModel, ResponseModel
from database.database import get_db, check_table
from sqlalchemy.orm import Session
from service.crud import create_user
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "world"}

@app.post("/user/newuser/")
def mew_user(payload:RequestModel, db:Session = Depends(get_db)):
    result = False
    try:
        dict_payload = payload.model_dump()
        result = create_user(db,dict_payload)
        
        if result:
            return JSONResponse(
                status_code=200,
                content= ResponseModel(
                    status= True,
                    data =  [dict_payload]
                ).model_dump()
            )
        else:
            return JSONResponse(
                status_code=500,
                content= ResponseModel(
                    status= False,
                    data =  [dict_payload]
                ).model_dump()
            )
            
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content= ResponseModel(
                status= False,
                data = [{"message" : str(e)}]
            ).model_dump()
        )
            


if __name__ == '__main__':
    check_table()
    uvicorn.run(app,host='0.0.0.0', port = 5000)