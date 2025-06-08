import math

# 1) 입력 벡터 (3개 노드)
inputs = [0.9, 0.1, 0.8]  # 입력층 노드 값

# 2) 가중치 행렬 정의
#    - W1: 입력층→은닉층 (은닉 3개 × 입력 3개)
#    - W2: 은닉층→출력층 (출력 3개 × 은닉 3개)
W1 = [
    [0.1, 0.2, 0.3],   # 은닉노드1 ← [입력1, 입력2, 입력3]
    [0.4, 0.5, 0.6],   # 은닉노드2 ← [    ·     ·     · ]
    [0.7, 0.8, 0.9],   # 은닉노드3 ← [    ·     ·     · ]
]

W2 = [
    [0.9, 0.8, 0.7],   # 출력노드1 ← [은닉1, 은닉2, 은닉3]
    [0.6, 0.5, 0.4],   # 출력노드2 ← [   ·     ·     · ]
    [0.3, 0.2, 0.1],   # 출력노드3 ← [   ·     ·     · ]
]

# 3) 매트릭스-벡터 곱 함수
def mat_vec_mult(W, v):
    return [sum(w_ij * v_j for w_ij, v_j in zip(row, v)) for row in W]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# 4) 순전파 계산
#   은닉층 입력(가중합)
hidden_inputs  = mat_vec_mult(W1, inputs)

#   (원하면 활성화 함수 적용 가능, 예: 시그모이드)
hidden_outputs = [sigmoid(u) for u in hidden_inputs]

#   출력층 입력(가중합)
output_inputs  = mat_vec_mult(W2, hidden_outputs)

#   최종 출력 (활성화 적용)
outputs = [sigmoid(u) for u in output_inputs]

# 5) 결과 출력
print("은닉층 입력값들:", [f"{u:.3f}" for u in hidden_inputs])
print("은닉층 출력값들:", [f"{u:.3f}" for u in hidden_outputs])
print("출력층 입력값들:", [f"{u:.3f}" for u in output_inputs])
print("최종 활성화 출력값들:", [f"{u:.3f}" for u in outputs])