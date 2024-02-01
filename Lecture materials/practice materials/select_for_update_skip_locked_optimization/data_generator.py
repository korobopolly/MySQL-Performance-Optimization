import csv
from datetime import datetime, timedelta
import random

# 쿠폰 데이터 생성
coupons = []
statuses = ['available', 'assigned', 'used']  # 쿠폰 상태

for i in range(1, 10001):
    status = 'available'
    user_id = ''
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expires_at = (datetime.now() + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d %H:%M:%S')
    coupons.append([status, user_id, created_at, expires_at])

# CSV 파일에 저장
csv_filename = 'coupons.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['status', 'user_id', 'created_at', 'expires_at'])
    writer.writerows(coupons)

csv_filename