import random

# 시뮬레이션 횟수
trials = 100000
# 총합이 30 이상인 경우의 수
success = 0

for _ in range(trials):
    # 주사위가 랜덤으로 나올 경우
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # 주사위 1과 2가 같은 경우
    if dice1==dice2:
        success += 1

# 확률 계산
probability = success / trials
print(f"주사위가 같을 확률은 {probability:.4f} 입니다.")