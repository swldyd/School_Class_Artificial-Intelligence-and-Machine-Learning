# 1) 데이터 및 목표값 직접 입력
x_data   = [2.0, 1.0]               # 폭 (cm)
y_data   = [0.9, 2.9]               # 길이 (cm)
labels   = ['무당벌레', '애벌레']  # 실제 클래스
targets  = [1.0, 2.8]               # 강의자료 예시 목표값 (직접 입력)

# 2) 하이퍼파라미터
learning_rate = 0.4    # 학습률
A = 1               # 초기 기울기

# --- 목표값으로 A 학습 ---
for xi, t in zip(x_data, targets):
    error = t - A * xi
    A += learning_rate * (error / xi)

print(f"학습된 기울기 A = {A:.4f}")  # 강의 예시대로 약 1.6042

# --- 분류 예측: 각 샘플이 직선 y=A*x 위/아래 어느 쪽인지 ---
for xi, yi, ci in zip(x_data, y_data, labels):
    pred = '위쪽(positive)' if yi > A * xi else '아래쪽(negative)'
    print(f"샘플 ({xi:.1f}, {yi:.1f}) 실제={ci} → 예측영역={pred}")