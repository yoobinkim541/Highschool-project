import random

# 시뮬레이션 횟수
trials = 100000
# 총합이 30 이상인 경우의 수
success = 0

for _ in range(trials):
    # 5번 돌린 결과의 총합
    total = sum(random.randint(1, 12) for _ in range(5))
    # 총합이 30 이상인 경우
    if total >= 30:
        success += 1

# 확률 계산
probability = success / trials
print(f"총합이 30 이상일 확률은 대략 {probability:.4f} 입니다.")
