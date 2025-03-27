# Perceptron API for Titanic Survival Prediction

## Overview
This project implements a perceptron model to predict Titanic passenger survival using Age and Fare features. The model is deployed as a production-ready API using Flask and hosted on AWS Elastic Beanstalk, demonstrating end-to-end ML deployment skills.

## Features
- **Perceptron Model:** A simple neural network built from scratch to classify survival (0 or 1).
- **Flask API:** Serves predictions via a `/predict` endpoint, accepting JSON input (`age`, `fare`).
- **AWS Deployment:** Deployed on AWS Elastic Beanstalk for scalability and real-world application.

## How It Works
1. The perceptron model uses pre-trained weights and bias to compute a net input (`dot(X, weights) + bias`).
2. A step function predicts survival: 1 if net input >= 0, else 0.
3. The Flask API accepts POST requests with `age` and `fare`, returning a JSON prediction.

## Usage
- **Local Setup:**
  1. Clone the repo: `git clone <repo-url>`
  2. Install dependencies: `pip install flask numpy`
  3. Run the app: `python app.py`
  4. Send a POST request to `http://localhost:5000/predict`:
     ```json
     {"age": 30, "fare": 50}
     ```
- **AWS Endpoint:** Access the deployed API at `<your-elastic-beanstalk-url>/predict`.

## Deployment
- Deployed on AWS Elastic Beanstalk using Docker for containerization.
- Steps:
  1. Created a `Dockerfile` and `.ebextensions` for Elastic Beanstalk.
  2. Pushed to AWS using the EB CLI: `eb deploy`.

## Future Improvements
- Add model training endpoint.
- Integrate with Databricks for large-scale data processing.

## Author
A Python developer with 5+ years of full-stack experience, passionate about ML and AI.
