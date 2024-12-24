def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vector dimensions must be the same")
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    
    return result

# 두 벡터 입력 받기
vector1 = [2, 3, 4]
vector2 = [5, 6, 7]

# 내적 계산
result = dot_product(vector1, vector2)

# 결과 출력
print("두 벡터의 내적:", result)