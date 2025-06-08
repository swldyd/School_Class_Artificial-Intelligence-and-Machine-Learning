import math
# 필수 함수: 행렬-벡터 곱 및 시그모이드 함수
def mat_vec_mult(W, v):
    return [sum(w_ij * v_j for w_ij, v_j in zip(row, v)) for row in W]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# --- 시험용 입력 섹션: 여기만 바꿔서 사용하세요 ---
# --- 2노드 은닉층 + 2노드 출력층 네트워크 예시 ---
# 가중치 정의 (입력 → 은닉층)
# 입력 벡터 (2개 노드)
inputs_2 = [2, 1.5]  # 예시 입력값 두 개

raw_W1_2 = """
1 3
2 4
"""

# 가중치 정의 (은닉층 → 출력층)
raw_W2_2 = """
1 3
2 4
"""

# 문자열을 행렬로 파싱
W1_2 = [list(map(float, row.split())) for row in raw_W1_2.strip().splitlines()]
W2_2 = [list(map(float, row.split())) for row in raw_W2_2.strip().splitlines()]

hidden_in_2  = mat_vec_mult(W1_2, inputs_2)
hidden_out_2 = [sigmoid(u) for u in hidden_in_2]
output_in_2  = mat_vec_mult(W2_2, hidden_out_2)
output_out_2 = [sigmoid(u) for u in output_in_2]

# 결과 출력 (소숫점 3자리)
print("\n[3계층 2노드 네트워크]")
print("은닉층 입력값:",  [f"{u:.3f}" for u in hidden_in_2])
print("은닉층 출력값:",  [f"{u:.3f}" for u in hidden_out_2])
print("출력층 입력값:",  [f"{u:.3f}" for u in output_in_2])
print("최종 활성화 출력값:", [f"{u:.3f}" for u in output_out_2])

