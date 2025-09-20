import pandas as pd

data = pd.read_csv("Algorithms/Linera Regression/study_hours_scores.csv")

class LinearRegressionScratch:
    def __init__(self, learning_rate=0.001, epochs=1000):
        self.slope = 0
        self.intercept = 0
        self.learning_rate = learning_rate
        self.epochs = epochs

    def gradient_descent(self, data):
        slope_gradient = 0
        intercept_gradient = 0
        n = len(data)

        for i in range(n):
            x = data.iloc[i].study_hours
            y = data.iloc[i].score

            slope_gradient += -(2/n) * x * (y - (self.slope * x + self.intercept))
            intercept_gradient += -(2/n) * (y - (self.slope * x + self.intercept))
        
        # Update parameters
        self.slope -= self.learning_rate * slope_gradient
        self.intercept -= self.learning_rate * intercept_gradient

    def train(self, data):
        for _ in range(self.epochs):
            self.gradient_descent(data)

    def predict(self, study_hours):
        return self.slope * study_hours + self.intercept

model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
model.train(data)

print(model.predict(24))