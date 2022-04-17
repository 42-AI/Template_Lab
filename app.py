from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# from inference_onnx import ColaONNXPredictor
app = FastAPI(title="MLOps Basics App")

# predictor = ColaONNXPredictor("./models/model.onnx")


@app.get("/", response_class=HTMLResponse)
async def home_page():
    return """
    <html>
        <h2>
            Sample prediction API
        </h2>
    </html>
    """


@app.get("/predict")
async def get_prediction(text: str):
    result = text[::-1]
    return result
