from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import Response

app = FastAPI()

@app.post("/transform")
async def transform_image(style: str = Form(...), image: UploadFile = File(...)):
    content = await image.read()
    return Response(content, media_type="image/jpeg")
