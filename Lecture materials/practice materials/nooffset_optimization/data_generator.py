import csv
import random
from datetime import datetime, timedelta

def create_csv_file(file_name, num_records):
    # CSV 파일 생성
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(num_records):
            user_id = random.randint(1, 10000)
            activity_type = random.choice(['login', 'logout', 'click', 'view'])
            activity_timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
            additional_info = 'Sample info'
            writer.writerow([user_id, activity_type, activity_timestamp, additional_info])


# CSV 파일 생성 및 데이터 로드
csv_file_name = 'user_activity_logs.csv'
num_records = 100000  # 예: 10만 건의

create_csv_file(csv_file_name, num_records)