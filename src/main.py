from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from classifier.classifier import NSFWJSClassifier

classifier = NSFWJSClassifier(model_path="models/nsfw_model.tflite")

app = FastAPI()


@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = classifier.classify(image_bytes)
        return JSONResponse(content=result.to_dict())
    except ValueError as ve:
        return JSONResponse(status_code=400, content={"error": str(ve)})
    except Exception:
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
