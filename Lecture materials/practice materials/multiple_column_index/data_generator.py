import csv
import random
from datetime import datetime, timedelta

# 데이터 생성 함수
def generate_order_data(record_count):
    statuses = ['배송 중', '배송 완료', '주문 취소']
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    for order_id in range(1, record_count + 1):
        customer_id = random.randint(1, 10000)
        order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        product_id = random.randint(1, 1000)
        quantity = random.randint(1, 10)
        status = random.choice(statuses)

        yield [customer_id, order_date.strftime('%Y-%m-%d'), product_id, quantity, status]

# CSV 파일 저장
def save_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['customer_id', 'order_date', 'product_id', 'quantity', 'status'])
        writer.writerows(data)

# 메인 실행
if __name__ == "__main__":
    record_count = 1000000  # 100만 건
    filename = 'orders_data.csv'
    data = generate_order_data(record_count)
    save_to_csv(filename, data)
    print(f"{filename}에 {record_count}건의 데이터가 저장되었습니다.")