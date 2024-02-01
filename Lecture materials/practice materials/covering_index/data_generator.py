import csv
import random
from datetime import datetime, timedelta

# 파일명 설정
filename = 'orders_test_data.csv'

# 100만 건의 데이터 생성
num_records = 1000000
start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 1, 1)
date_range = (end_date - start_date).days

# CSV 파일에 데이터 작성
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'order_date', 'total_amount'])

    for i in range(1, num_records + 1):
        customer_id = random.randint(1, 100000)  # 예시 고객 ID 범위
        order_date = start_date + timedelta(days=random.randint(0, date_range))
        total_amount = round(random.uniform(10.0, 1000.0), 2)  # 최소 10.0, 최대 1000.0 범위의 금액

        writer.writerow([customer_id, order_date.strftime('%Y-%m-%d'), total_amount])

print(f"100만 건의 데이터가 {filename} 파일에 저장되었습니다.")
