from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.model import RequestModel
from database.database import get_db, check_table
from sqlalchemy.orm import Session
from service.crud import create_user, get_user
from service.helper import create_response
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "world"}

@app.get("/user/getuser/{user_name}")
def get_user_by_name(user_name:str, db: Session= Depends(get_db)):
    try:
        result = get_user(db,user_name)
        if not result:
            return create_response(status= False, data= "User Not Found",  status_code=404 )
        return create_response(status=True, data=result)
    except Exception as e:
        print(f"error")
        return create_response(
            status = False,
            data = str(e),
            status_code=500
        )
            
@app.post("/user/newuser/")
def mew_user(payload:RequestModel, db:Session = Depends(get_db)):
    
    result = False
    try:
        dict_payload = payload.model_dump()
        result = create_user(db,dict_payload)
        
        if result:
            return create_response(
                status= True,
                data = dict_payload
            )
        else:
            return create_response(
                status= False,
                status_code=500,
                data = [result]
            )
        
    except Exception as e:
        return create_response(
            status= False,
            status_code=500,
            data = str(e)
        )
            


if __name__ == '__main__':
    check_table()
    uvicorn.run(app,host='0.0.0.0', port = 5000)