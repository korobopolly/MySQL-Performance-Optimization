import csv
import random
from datetime import datetime, timedelta

# 랜덤 데이터 생성 함수
def generate_random_data(filename, num_records):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'product_id', 'quantity', 'cart_added_date'])  # 컬럼 헤더

        for _ in range(num_records):
            user_id = random.randint(1, 1000)  # 사용자 ID: 1부터 1000 사이
            product_id = random.randint(1, 500)  # 상품 ID: 1부터 500 사이
            quantity = random.randint(1, 10)  # 수량: 1부터 10 사이
            days_ago = random.randint(1, 60)  # 최대 60일 전
            cart_added_date = datetime.now() - timedelta(days=days_ago)
            cart_added_date_str = cart_added_date.strftime('%Y-%m-%d %H:%M:%S')  # 날짜 형식 문자열

            writer.writerow([user_id, product_id, quantity, cart_added_date_str])

# 데이터 생성 및 CSV 파일 저장
filename = 'shopping_cart_data.csv'
num_records = 100000  # 10000건의 데이터
generate_random_data(filename, num_records)
