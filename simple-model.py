from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

class Perceptron:
    def __init__(self):
        self.weights = np.array([0.1, 0.2])  # Example weights
        self.bias = 0.3

    def predict(self, X):
        net_input = np.dot(X, self.weights) + self.bias
        return np.where(net_input >= 0, 1, 0)

model = Perceptron()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = np.array([data['age'], data['fare']])
    prediction = model.predict(X.reshape(1, -1))
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
