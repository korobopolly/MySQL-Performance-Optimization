import pymysql
import random
import time

from datetime import datetime, timedelta

# 데이터베이스 설정
host = 'localhost'
port = 3306
user = 'root'
password = '1234'
database = 'test'

# 데이터베이스 연결
connection = pymysql.connect(host=host, port=port, user=user, password=password, db=database)

def insert_multiple_values(data):
    with connection.cursor() as cursor:
        query = "INSERT INTO user_activity_logs (user_id, activity_type, activity_timestamp, additional_info) VALUES (%s, %s, %s, %s)"
        cursor.executemany(query, data)
    connection.commit()

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        user_id = random.randint(1, 10000)
        activity_type = random.choice(['login', 'logout', 'click', 'view'])
        activity_timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
        additional_info = 'Sample info'
        data.append((user_id, activity_type, activity_timestamp, additional_info))
    return data

# 데이터 생성 및 INSERT 실행
num_records = 100000  # 예: 10만 건의 레코드
data_to_insert = generate_data(num_records)

start_time = time.perf_counter()
insert_multiple_values(data_to_insert)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

# 연결 닫기
connection.close()
