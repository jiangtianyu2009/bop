from typing import List

from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}
