import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.0):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = None
        self.bias = None

    def step_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        linear_output = np.dot(inputs, self.weights) + self.bias
        return self.step_function(linear_output)

    def train(self, X, y):
        num_features = X.shape[1]
        self.weights = np.zeros(num_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate


logic_gates = {
    "AND": np.array([0, 0, 0, 1]),
    "OR": np.array([0, 1, 1, 1]),
    "NAND": np.array([1, 1, 1, 0]),
    "XOR": np.array([0, 1, 1, 0])
}

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


for gate, labels in logic_gates.items():
    perceptron = Perceptron()
    perceptron.train(X, labels)

    print(f"Logic gate {gate}")
    for input_data, label in zip(X, labels):
        output = perceptron.predict(input_data)
        print(f"Input: {input_data}, Actual: {label}, Predicted: {output}")
    print("="*30)
