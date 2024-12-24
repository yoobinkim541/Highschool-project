import numpy as np
import matplotlib.pyplot as plt

def plot_vector(vector, color, label):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

# 두 벡터 입력 받기
vector1 = np.array([2, 7.897987])
vector2 = np.array([8.65879, -1])

# 내적 계산
dot_product = np.dot(vector1, vector2)

# 벡터를 그래프로 시각화
plt.figure(figsize=(8, 6))
plot_vector(vector1, color='blue', label='Vector 1')
plot_vector(vector2, color='red', label='Vector 2')

# 내적 값 출력
plt.text(0, -3, f"Dot Product: {dot_product}", fontsize=12, color='green')

plt.title('Inner Product of Vectors')
plt.show()