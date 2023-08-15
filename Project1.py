import numpy as np

def activation_function(net_input):
    return 1 if net_input >= 0 else 0

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

w = np.random.rand(2)
b = np.random.rand()

num = 10
learning_rate = 0.1

for _ in range(num):
    for inputs, target in zip(X, y):
        net_input = np.dot(inputs, weights) + bias
        prediction = activation_function(net_input)
        error = target - prediction
        weights += learning_rate * error * inputs
        bias += learning_rate * error

test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for data in test_data:
    net_input = np.dot(data, weights) + bias
    result = activation_function(net_input)
    print(f"Input: {data}, Output: {result}")

