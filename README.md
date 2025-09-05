# Pest Disease Detection Backend

This repository contains the backend code for the Pest Disease Detection system. It includes the API for uploading crop images, running disease prediction models, and providing recommendations.

## Features

- Upload crop images and optional text descriptions.
- Predict plant disease using trained deep learning models.
- Provide advice, pesticides, fertilizers, and dosage information.
- Support multiple languages for recommendations.
- Text-to-speech audio output for recommendations.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip package manager

### Installation

1. Clone the repository:
git clone https://github.com/Nilkamal21/Pest-Disease-Backend.git
cd Pest-Disease-Backend/src

text

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. Install dependencies:
pip install -r requirements.txt

text

### Running the Backend Server

Start the backend API server by running:

uvicorn backend:app --host 0.0.0.0 --port 8001 --reload

text

The server will be accessible at:  
`http://localhost:8001`

### API Endpoints

- `/predict/` — POST endpoint to predict plant disease and get recommendations.

### Frontend

Frontend is excluded from this repository. You can run the frontend separately or integrate it as needed.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

MIT License
Git Commands to Push Your Local Code
Run these commands inside your project root folder where .git is initialized:

bash
git add .
git commit -m "Initial commit: Add backend source code and .gitignore"
git push -u origin main