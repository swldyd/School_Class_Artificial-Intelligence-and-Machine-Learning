#1) 데이터 및 목표값 아래 세개에 값 입력
x_data    = [3.0, 1.0, 3.0]               # 폭(cm)
y_data    = [1.0, 3.0, 0.9]              # 길이(cm)
labels    = ['무당벌레', '애벌레','무당벌레']     # 실제 클래스
# 어지간해서는 안건들임( 값 기준 위로 0.1, 아래로 -0.1), 오차율 구할 때 값이 달라지면 변경
offset   = 0.1                            # 강의 예시 목표값 오프셋

learning_rate = 0.5          #** 학습률 설정필요
A = 1  # ** 초기 기울기 설정필요

# y_data 와 labels 에서 각 샘플의 목표 t 자동 생성
targets  = [(yi + offset) if ci == labels[0] else (yi - offset)
            for yi, ci in zip(y_data, labels)]


for xi, t in zip(x_data, targets):
    error = t - A * xi
    A += learning_rate * (error / xi)

print(f"학습된 기울기 A = {A:.4f}")

for xi, yi, ci in zip(x_data, y_data, labels):
    pred = '위쪽(positive)' if yi > A * xi else '아래쪽(negative)'
    print(f"샘플 ({xi},{yi}) 실제={ci} → 예측영역={pred}")