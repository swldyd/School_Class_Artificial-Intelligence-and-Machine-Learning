# filepath: /Users/simjiyong/Downloads/인지계 시험대비 연산/행렬계산기.py
# ─── 입력 섹션 (여기에만 숫자를 수정하세요) ─────────────────────
# 2×2 행렬 A2
raw_A2 = """
0.94 0.04
0.06 0.96
"""

# 2×1 벡터 v2
raw_v2 = "9432 1368"

# 3×3 행렬 A3
raw_A3 = """
1 0 -2
-3 1 4
2 -3 4
"""

# 3×3 행렬 B3
raw_B3 = """
8 4 0
10 5 0
3.5 2 0
"""

# 3×1 벡터 v3
raw_v3 = "0.7 0.6 0.5"

# ────────────────────────────────────────────────────────────────

# 파싱 함수
def parse_matrix(txt):
    return [list(map(float, row.split())) for row in txt.strip().splitlines()]

def parse_vector(txt):
    return list(map(float, txt.split()))

# 행렬·벡터 파싱
A2 = parse_matrix(raw_A2)
v2 = parse_vector(raw_v2)

A3 = parse_matrix(raw_A3)
B3 = parse_matrix(raw_B3)
v3 = parse_vector(raw_v3)

# 일반화된 행렬×벡터 곱
def mat_vec_mult(W, v):
    return [sum(w_ij * v_j for w_ij, v_j in zip(row, v)) for row in W]

# 3×3 행렬 곱
def mat_mult(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

# 결과 계산
res2 = mat_vec_mult(A2, v2)
res3 = mat_vec_mult(A3, v3)
res_mat_mult = mat_mult(A3, B3)

# 출력
print("2×2 × 2×1 =", res2)  # 예: [1*5+2*6, 3*5+4*6]
print("3×3 × 3×1 =", res3)  # 예: [1*0.7+0*0.6+0*0.5, …, 0*0.7+0*0.6+1*0.5]
print("3×3 × 3×3 =", res_mat_mult)  # 예: [[1*1+2*4+3*7, ...], ...]