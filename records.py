from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
RECORDS = [
       {
          "description": "chou zhu's fav",
          "id": 1,
          "artistname": "Kate Bush",
          "damage": "",
          "cover_image": "https://tubbs-on-aws.s3.eu-central-1.amazonaws.com/Katebushhoundsoflove_wiki.png",
          "year": 1985,
          "name": "Hounds of Love",
          "title": "",
          "worth": "100 Pound",
          "serial_nr": ""
        },
        {
          "description": "my fav",
          "id": 2,
          "artistname": "Kate Bush",
          "damage": "",
          "cover_image": "https://tubbs-on-aws.s3.eu-central-1.amazonaws.com/The_Kick_Inside_(Album_Artwork).png",
          "year": 1978,
          "name": "The Kick Inside",
          "title": "",
          "worth": "500 Pound",
          "serial_nr": ""
        }
]

@app.get("/records")
async def read_all_records():
    return RECORDS

