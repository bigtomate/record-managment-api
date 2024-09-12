from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status

import models
from models import Artists
from models import Records
from database import engine, SessionLocal
from typing import Annotated
# why sqlaclchemy, anyother orm? version 
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4202",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# sessionLocal ?
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

# basemodel is the model view (DTO)
class RecordRequest(BaseModel):
    name: str
    title: str
    description: str
    year: int
    artistname : str
    # field lenght not restriction
    worth : str
    damage:str
    serial_nr:str
    cover_image:str

@app.get("/artists")
def read_all_artists(db: db_dependency):
    return db.query(Artists).all()

@app.get("/records")
def read_all_records(db: db_dependency):
    return db.query(Records).all()

@app.get("/records/{record_id}", status_code=status.HTTP_200_OK)
def read_recordById(db: db_dependency, record_id: int = Path(gt = 0)):
    record_model = db.query(Records).filter(Records.id == record_id).first()
    if record_model is not None:
        return record_model
    raise HTTPException(status_code = 404, detail ='record_not_found');

# query parameter
@app.get("/records/{id}", status_code=status.HTTP_200_OK)
def read_recordById_queryParam(db: db_dependency, id: int):
    record_model = db.query(Records).filter(Records.id == record_id).first()
    if record_model is not None:
        return record_model
    raise HTTPException(status_code = 404, detail ='record_not_found');

@app.post("/records", status_code=status.HTTP_201_CREATED)
def createRecord(db: db_dependency, record_request: RecordRequest):
    record_model = Records(**record_request.dict())
    db.add(record_model)
    db.commit()
    return record_request
  
 # path varibale must as the last !!
@app.put("/records/{record_id}", status_code=status.HTTP_200_OK)
def updateRecord(db: db_dependency, 
                       record_request: RecordRequest,
                       record_id: int = Path(gt = 0) 
                       ):
  record_model = db.query(Records).filter(Records.id == record_id).first()
  if record_model is None:
   raise HTTPException(status_code = 404, detail ='record_not_found')
  record_model.name = record_request.name
  record_model.title = record_request.title
  record_model.description = record_request.description
  record_model.year = record_request.year
  record_model.artistname = record_request.artistname
  record_model.worth = record_request.worth
  record_model.damage = record_request.damage
  record_model.serial_nr = record_request.serial_nr
  record_model.cover_image = record_request.cover_image
  db.commit()
  return record_request

@app.delete("/records/delete/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteRecord(db: db_dependency, record_id: int):
      record_model = db.query(Records).filter(Records.id == record_id).first()
      if record_model is None:
       raise HTTPException(status_code = 404, detail ='record_not_found')
      db.query(Records).filter(Records.id == record_id).delete()
      db.commit()
