# Insurance Premium Prediction API

A FastAPI-based REST API for predicting insurance premiums based on user input features. This project demonstrates how to build, containerize, and deploy a machine learning model as a web service.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Running the API Locally](#running-the-api-locally)
- [API Endpoints](#api-endpoints)
- [Dockerization](#dockerization)
  - [Docker Commands](#docker-commands)
  - [Pushing to Docker Hub](#pushing-to-docker-hub)
- [Extending the API](#extending-the-api)
- [References](#references)

---

## Project Overview

This API predicts insurance premiums using a trained machine learning model. It exposes endpoints for health checks and predictions, making it suitable for integration with web or mobile applications.

---

## Features

- **/predict**: Predict insurance premium from user input.
- **/health**: Health check endpoint for monitoring.
- **/ (root)**: Welcome message.
- **Dockerized**: Easily build and deploy as a container.
- **OpenAPI docs**: Interactive API docs at `/docs`.

---

## Project Structure

```
.
├── app.py                      # Main FastAPI application
├── Dockerfile                  # Docker build instructions
├── requirements.txt            # Python dependencies
├── config/
│   └── city_tier.py            # City tier configuration
├── models/
│   ├── model.pkl               # Trained ML model
│   └── predict.py              # Prediction logic
├── schema/
│   ├── user_input.py           # Pydantic model for input
│   └── prediction_response.py  # Pydantic model for output
└── ...
```

---

## Setup & Installation

### 1. Clone the Repository

```sh
git clone https://github.com/M-MuneebAlam/insurance-premium-prediction-api.git
cd insurance-premium-prediction-api
```

### 2. Create a Virtual Environment

```sh
python -m venv myenv
source myenv/Scripts/activate  # On Windows
# or
source myenv/bin/activate      # On Linux/Mac
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

---

## Running the API Locally

```sh
uvicorn app:app --reload
```

- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

---

## API Endpoints

### `GET /`
- **Description:** Welcome message.

### `GET /health`
- **Description:** Health check for API and model status.
- **Response Example:**
  ```json
  {
    "status": "ok",
    "message": "API is running smoothly",
    "model_version": "1.0.0",
    "model_loaded": true
  }
  ```

### `POST /predict`
- **Description:** Predict insurance premium.
- **Request Body Example:**
  ```json
  {
    "bmi": 24.5,
    "age_group": "30-40",
    "lifestyle_risk": "low",
    "city_tier": "tier_1",
    "income_lpa": 12,
    "occupation": "engineer"
  }
  ```
- **Response Example:**
  ```json
  {
    "predicted_premium": 12345.67
  }
  ```

---

## Dockerization

### 1. Build Docker Image

Make sure you have Docker installed. Then run:

```sh
docker build -t insurance-premium-api:latest .
```

### 2. Run Docker Container

```sh
docker run -d -p 8000:8000 --name insurance_api insurance-premium-api:latest
```

- The API will be available at [http://localhost:8000](http://localhost:8000).

### 3. Stop & Remove Container

```sh
docker stop insurance_api
docker rm insurance_api
```

---

### Docker Commands

| Command | Description |
| ------- | ----------- |
| `docker build -t <image_name>:<tag> .` | Build Docker image from Dockerfile |
| `docker images` | List all Docker images |
| `docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>:<tag>` | Run container in detached mode |
| `docker ps` | List running containers |
| `docker stop <container_name>` | Stop a running container |
| `docker rm <container_name>` | Remove a stopped container |
| `docker rmi <image_name>:<tag>` | Remove a Docker image |

---

### Pushing to Docker Hub

1. **Login to Docker Hub**

   ```sh
   docker login
   ```

2. **Tag Your Image**

   ```sh
   docker tag insurance-premium-api:latest yourdockerhubusername/insurance-premium-api:latest
   ```

3. **Push Image**

   ```sh
   docker push yourdockerhubusername/insurance-premium-api:latest
   ```

4. **Pull Image (on another machine/server)**

   ```sh
   docker pull yourdockerhubusername/insurance-premium-api:latest
   ```

---

## Extending the API

- Add new features by editing [`app.py`](app.py).
- Update input/output schemas in [`schema/user_input.py`](schema/user_input.py) and [`schema/prediction_response.py`](schema/prediction_response.py).
- Update prediction logic in [`models/predict.py`](models/predict.py).
- Retrain and replace the model in [`models/model.pkl`](models/model.pkl) as needed.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Happy Learning & Shipping!**