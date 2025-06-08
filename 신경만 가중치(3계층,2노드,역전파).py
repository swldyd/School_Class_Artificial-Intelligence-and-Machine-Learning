import math

# ─── 사용자 설정 부분 ────────────────────────────────────────────
# 1) 가중치 행렬 정의
#    W1: 입력층 → 은닉층 (은닉노드 수 × 입력노드 수)
W1 = [
    [2.0, 1.0],   # 은닉1 ← [입력1, 입력2]
    [3.0, 7.0],   # 은닉2 ← [입력1, 입력2]
]

#    W2: 은닉층 → 출력층 (출력노드 수 × 은닉노드 수)
W2 = [
    [2.0, 6.0],  # 출력1 ← [은닉1, 은닉2]
    [1.0, 4.0],  # 출력2 ← [은닉1, 은닉2]
]

# 3) 출력층에서 주어진 오차 (예시)
output_errors = [8, 5]  # e_output1, e_output2
# ──────────────────────────────────────────────────────────────

# 활성화 함수 및 유틸
def sigmoid(x): 
    return 1 / (1 + math.exp(-x))

# 은닉층 오차 계산 (역전파)
# hidden_errors[j] = sum_i ( output_errors[i] * W2[i][j] )
hidden_errors = [
    sum(output_errors[i] * W2[i][j] for i in range(len(W2)))
    for j in range(len(W1))
]

# 입력층 오차 계산 (역전파)
# input_errors[k] = sum_j ( hidden_errors[j] * W1[j][k] )
input_errors = [
    sum(hidden_errors[j] * W1[j][k] for j in range(len(W1)))
    for k in range(len(W1[0]))
]
# 은닉층 오차 계산 (역전파)
hidden_errors = [
    sum(output_errors[i] * (W2[i][j] / sum(W2[i])) for i in range(len(W2)))
    for j in range(len(W1))
]

# 입력층 오차 계산 (역전파)
input_errors = [
    sum(hidden_errors[j] * (W1[j][k] / sum(W1[j])) for j in range(len(W1)))
    for k in range(len(W1[0]))
]

# 결과 출력 (소숫점 3자리)
print("▶ 출력층 오차:",      [f"{e:.3f}" for e in output_errors])
print("▶ 은닉층 오차:",      [f"{e:.3f}" for e in hidden_errors])
print("▶ 입력층 오차:",      [f"{e:.3f}" for e in input_errors])