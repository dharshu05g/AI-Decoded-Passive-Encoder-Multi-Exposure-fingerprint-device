# AI-Based Passive Physical Event Decoder Dashboard

**Final-Year Project: AI-Based Decoding of Nonlinear Physical Event Signatures Using a Passive Multistate Encoder**

## Project Overview

This project demonstrates a complete software prototype for decoding physical event signatures using a passive mechanical encoder and machine learning. The system uses a 4-channel binary encoder to physically retain the signature of physical events such as shock, impact, or abnormal vibration.

### System Architecture

```
Physical Event → Passive Mechanical Encoder → Sensors → Feature Extraction → AI Classification → Event Output
```

### Key Components

- **Passive Multistate Mechanical Encoder**: 4-channel binary encoder (S1-S4) that physically retains event signatures
- **Sensor Data Processing**: Acceleration, RMS, peak-to-peak, and other motion features
- **Machine Learning**: Random Forest classifier for event classification
- **Web Dashboard**: Real-time monitoring, prediction, and historical analysis

## Event Classes

- **NORMAL**: Low acceleration, stable encoder states
- **MODERATE_SHOCK**: Medium acceleration, some state changes
- **SEVERE_SHOCK**: High acceleration, significant state changes

## Software Architecture

### Backend (Python + FastAPI)

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # REST API routes
│   │   ├── routes_data.py
│   │   ├── routes_model.py
│   │   ├── routes_prediction.py
│   │   └── routes_simulation.py
│   ├── ml/                  # Machine learning pipeline
│   │   ├── preprocessing.py
│   │   ├── feature_engineering.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   ├── simulation/          # Synthetic data generator
│   │   └── generator.py
│   ├── database/            # SQLite database
│   │   └── database.py
│   └── schemas/             # Pydantic models
│       └── models.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
├── models/                  # Trained ML models
├── requirements.txt
└── README.md
```

### Frontend (React + TypeScript)

```
frontend/
├── src/
│   ├── components/          # React components
│   ├── pages/               # Dashboard pages
│   ├── services/            # API client
│   ├── types/               # TypeScript types
│   └── utils/
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

## Installation

### Prerequisites

- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows:**
```bash
powershell
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python -c "from app.database.database import init_db; init_db()"
```

6. Run the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend dashboard will be available at `http://localhost:3000`

## How to Use

### 1. Train the Model

1. Open the dashboard at `http://localhost:3000`
2. Navigate to the **Dataset** page
3. Click **Train Model** to train on synthetic data (or upload your own CSV)
4. Wait for training to complete
5. Navigate to **Model Performance** to see metrics

### 2. Generate Simulated Events

1. Navigate to **Live Monitoring** or **AI Prediction**
2. Click one of the event generation buttons:
   - **NORMAL EVENT**
   - **MODERATE SHOCK**
   - **SEVERE SHOCK**
3. View the encoder state, sensor features, and AI prediction
4. Check the confidence and probability distribution

### 3. View Event History

1. Navigate to **Event History**
2. Filter by event type if needed
3. View all recorded events with timestamps and predictions

### 4. Monitor Encoder State

1. Navigate to **Encoder State**
2. View the current 4-channel binary state
3. See state transition history and statistics

## Dataset Format

For CSV upload, use the following column names:

- `encoder_s1`, `encoder_s2`, `encoder_s3`, `encoder_s4` (0 or 1)
- `acceleration_x`, `acceleration_y`, `acceleration_z` (float)
- `max_acceleration` (float)
- `rms_acceleration` (float)
- `event_duration` (float)
- `predicted_class` (NORMAL, MODERATE_SHOCK, SEVERE_SHOCK)

## API Endpoints

### Health
- `GET /api/health` - Health check

### Data
- `GET /api/data/events` - Get recent events
- `POST /api/data/dataset/upload` - Upload CSV dataset
- `GET /api/data/events/history` - Get event history

### Model
- `GET /api/model/status` - Get model status
- `POST /api/model/train` - Train model
- `GET /api/model/metrics` - Get model metrics

### Prediction
- `POST /api/prediction/predict` - Make prediction

### Simulation
- `POST /api/simulation/generate` - Generate simulated event

## Simulation Mode

The dashboard currently operates in **SIMULATION MODE**. All data is synthetically generated to demonstrate the system architecture. The simulation generates realistic class-dependent distributions:

- **NORMAL**: Low acceleration (0.1-0.5g), low RMS, stable encoder states
- **MODERATE_SHOCK**: Medium acceleration (2-5g), medium RMS, some state changes
- **SEVERE_SHOCK**: High acceleration (8-15g), high RMS, significant state changes

## Future ESP32 Integration

The software architecture is designed to accept real sensor data from ESP32 microcontrollers. The integration will follow this pattern:

```
ESP32 → Serial/HTTP/WebSocket → Backend → Same ML Pipeline → Dashboard
```

To integrate real hardware:

1. Implement the data source interface in `backend/app/api/`
2. Add WebSocket support for real-time streaming
3. Configure ESP32 to send sensor data in the expected format
4. Update the dashboard to show "LIVE ESP32 DATA" status

## Important Notes

### Research Integrity

- **Simulated data is NOT experimental hardware data**
- All metrics are from actual model training on synthetic data
- No fabricated accuracy or sensor measurements
- Clear labels distinguish between SIMULATION, DATASET, and LIVE data

### Limitations

- Current data is synthetic/simulated
- No real hardware integration yet
- Model trained on synthetic distributions
- Predictions may not reflect real-world performance

### Future Improvements

- Real ESP32 sensor data integration
- Additional event classes (REPEATED_VIBRATION, SUDDEN_IMPACT, ABNORMAL_VIBRATION)
- WebSocket real-time streaming
- Model comparison (Decision Tree, SVM, KNN)
- Advanced feature engineering
- Time-series analysis
- Anomaly detection

## Dashboard Pages

1. **Overview**: System status and architecture visualization
2. **Live Monitoring**: Real-time event stream and prediction
3. **Encoder State**: Visual representation of 4-channel encoder
4. **AI Prediction**: Classification results and probability distribution
5. **Dataset**: CSV upload and model training
6. **Model Performance**: Accuracy, confusion matrix, classification report
7. **Event History**: Historical events with filtering

## Troubleshooting

### Backend Issues

- If the model is not trained, train it first via the Dataset page
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify the database is initialized

### Frontend Issues

- Ensure the backend is running on port 8000
- Check that npm dependencies are installed: `npm install`
- Clear browser cache if needed

## Development

### Running Tests

```bash
# Backend tests (to be implemented)
cd backend
pytest

# Frontend tests (to be implemented)
cd frontend
npm test
```

### Building for Production

```bash
# Frontend
cd frontend
npm run build

# Backend (use gunicorn or similar)
cd backend
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## License

This is a final-year academic project. All code is provided as-is for educational purposes.

## Contact

For questions about the project architecture or implementation, please refer to the inline documentation and code comments.

---

**Disclaimer**: This software is a prototype for demonstration purposes. Simulated data should not be used for any real-world safety-critical applications. Real hardware integration is required for actual event detection and classification.
