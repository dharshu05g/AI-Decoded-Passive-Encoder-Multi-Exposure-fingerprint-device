from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_data import router as data_router
from app.api.routes_model import router as model_router
from app.api.routes_prediction import router as prediction_router
from app.api.routes_simulation import router as simulation_router

app = FastAPI(
    title="Passive Physical Event Decoder API",
    description="AI-Based Decoding of Nonlinear Physical Event Signatures Using a Passive Multistate Encoder",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(data_router, prefix="/api/data", tags=["data"])
app.include_router(model_router, prefix="/api/model", tags=["model"])
app.include_router(prediction_router, prefix="/api/prediction", tags=["prediction"])
app.include_router(simulation_router, prefix="/api/simulation", tags=["simulation"])

@app.get("/")
async def root():
    return {
        "message": "Passive Physical Event Decoder API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "passive-event-decoder"}
