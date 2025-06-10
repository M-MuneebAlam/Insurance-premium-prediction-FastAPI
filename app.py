from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from models.predict import predict_output, model, MODEL_VERSION
from schema.prediction_response import PredictionResponse

app = FastAPI()


#human readable description of the API
@app.get("/")
def home():
     return {'message': 'Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions.'}


#machine readable description of the API. Some services of AWS like kubernetes and elastic load balancer require this endpoint to be present. 
#When we deploy the API on AWS, they will force us to create it.
@app.get("/health")
def health_check():
    """Health check endpoint to verify if the API is running."""
    return {
        'status': 'ok',
        'message': 'API is running smoothly',
        'model_version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post("/predict", response_model = PredictionResponse)
def predict_premium(data: UserInput):
    """Predict insurance premium based on user input."""
    
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output([user_input])

        return JSONResponse(status_code=200, content={'predicted_premium': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content =  str(e))