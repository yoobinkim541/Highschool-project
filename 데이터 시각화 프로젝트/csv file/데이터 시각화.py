import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(csv_file):
    # CSV 파일을 분석하고 막대 그래프로 시각화하는 함수
    try:
        data = pd.read_csv(csv_file)  # CSV 파일 불러오기

        # AGE_G 이상의 데이터 추출
        data_over_age_g = data[data['AGE_G'] >= 20]

        # 각 항목별 데이터 변화를 막대 그래프로 표현
        plt.figure(figsize=(10, 6))
        for column in data_over_age_g.columns[1:]:  # 첫 번째 열은 'AGE_G'이므로 제외
            plt.bar(data_over_age_g['AGE_G'], data_over_age_g[column], label=column)

        plt.title('Changes in Data Over AGE_G')
        plt.xlabel('AGE_G')
        plt.ylabel('Values')
        plt.legend()
        plt.grid(True)
        plt.show()

        print("CSV 파일 분석 및 막대 그래프 시각화가 완료되었습니다.")
    except Exception as e:
        print("에러 발생:", e)

# CSV 파일 경로 설정
csv_file_path = 'eye sight 20+.csv'

# 변환된 CSV 파일 분석 및 막대 그래프 시각화
analyze_csv(csv_file_path)
