from fastapi import FastAPI, UploadFile, File
import shutil
import os

from inference import predict_image

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "AI service running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    label, confidence = predict_image(file_path)

    return {
        "prediction": label,
        "confidence": round(confidence, 3)
    }
    if not file.content_type.startswith("image/"):
     return {"error": "Invalid file type"}
