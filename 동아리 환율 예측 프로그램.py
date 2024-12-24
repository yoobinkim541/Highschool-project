import numpy as np

# 시그모이드 함수와 그 도함수 (4-6 줄)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 예제 데이터: 날짜별 원달러 환율 (7-9 줄)
inputs = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # 6월 1일~10일
outputs = np.array([[1383], [1380], [1379], [1375], [1374], [1372], [1371], [1370], [1369], [1368]])  # 환율

# 입력 데이터와 출력 데이터를 정규화 (11-12 줄)
inputs = inputs / np.max(inputs)
outputs = outputs / 1383  # 최대값을 기준으로 정규화

# 신경망의 가중치 초기화 (14-17 줄)
input_layer_neurons = 1
hidden_layer_neurons = 3
output_neurons = 1

hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# 학습률 (19 줄)과 에폭 (20 줄)
learning_rate = 0.1
epochs = 10000

# 역전파 알고리즘을 사용한 학습 과정 (22-40 줄)
for epoch in range(epochs):
    # 순전파 (24-26 줄)
    hidden_layer_input = np.dot(inputs, hidden_weights) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, output_weights) + output_bias
    predicted_output = sigmoid(output_layer_input)
    
    # 오차 계산 (28 줄)
    error = outputs - predicted_output
    
    # 역전파 (30-34 줄)
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    
    # 가중치와 편향 업데이트 (36-40 줄)
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# 결과 출력 (42-44 줄)
predicted_output = predicted_output * 1383  # 정규화 되돌리기
print("예측 결과 (원달러 환율):")
print(predicted_output)
