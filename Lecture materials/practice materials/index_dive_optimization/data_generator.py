import csv
import random
from datetime import datetime, timedelta

def create_test_data(filename, num_records=1000000):
    # 기본 설정
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 31)
    date_range = (end_date - start_date).days
    max_customer_id = 1000
    max_total_amount = 10000.00

    # CSV 파일 생성
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # CSV 헤더 작성
        writer.writerow(['customer_id', 'order_date', 'total_amount'])

        for i in range(1, num_records + 1):
            # 데이터 생성
            customer_id = random.randint(1, max_customer_id)
            random_days = random.randint(0, date_range)
            order_date = start_date + timedelta(days=random_days)
            total_amount = round(random.uniform(0.01, max_total_amount), 2)

            # CSV에 데이터 작성
            writer.writerow([customer_id, order_date.strftime('%Y-%m-%d'), total_amount])

# 파일 이름 지정
filename = 'orders_test_data.csv'

# 테스트 데이터 생성
create_test_data(filename)

