import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def update_weights(t_k, o_k, weights, o_j, learning_rate):

    error = -(t_k - o_k)
    # Sigma operation: sum over j of w_jk * o_j
    weighted_sum = sum(w * o for w, o in zip(weights, o_j))

    sigmoid_output = sigmoid(weighted_sum)
    sigmoid_derivative = sigmoid_output * (1 - sigmoid_output)

    grad = error * sigmoid_derivative * o_j

    # Apply learning rate to update weights
    new_weights = weights - learning_rate * grad

    return new_weights
    """

    weights: 가중치 배열 (출력 계층으로 가는 가중치)
    o_j: 은닉 계층에서 나온 출력값
    learning_rate: 학습률 (alpha)
    """

# 변수 정의

t_k=0.8 #t_k: 목표값 (target)
o_k=0 #o_k: 실제 출력값
#출력층 에러(e1)이 0.8이라면, t_k=0.8, o_k=0
alpha = 0.1 # 학습률
weights = np.array([2.0, 3.0]) # 은닉층에서 출력층으로 가는 가중치 (w_1,1, w_2,1)
outputs_hidden_layer = np.array([0.4, 0.5]) # 은닉층의 출력 (o_1, o_2)


new_w = update_weights(t_k,o_k, weights=weights, o_j=outputs_hidden_layer, learning_rate=alpha)
print(new_w)
