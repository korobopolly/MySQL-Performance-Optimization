import pymysql
import time
import random
from pymysql.err import MySQLError
from concurrent.futures import ThreadPoolExecutor

def execute_query(conn_params, query):
    try:
        conn = pymysql.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except MySQLError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def create_query():
    return f"UPDATE dead_lock_detect_test SET value = now() WHERE id 1"

# MySQL 연결 설정
conn_params = {
    'host': 'localhost',
    'database': 'test',
    'user': 'root',
    'password': '1234',
    'connect_timeout': 3000
}

# 병렬 실행을 위한 스레드 풀 크기
pool_sizes = [16, 100]

for pool_size in pool_sizes:
    print(f"병렬 수준 {pool_size}으로 쿼리 실행 중...")

    start_time = time.time()  # 작업 시작 시간 기록

    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        for _ in range(1000):
            futures = [executor.submit(execute_query, conn_params, create_query()) for _ in range(pool_size)]
            for future in futures:
                future.result()

    end_time = time.time()  # 작업 종료 시간 기록R
    elapsed_time = end_time - start_time  # 총 소요 시간 계산

    print(f"병렬 수준 {pool_size}에서 쿼리 실행 완료, 소요 시간: {elapsed_time:.2f}초")

print("모든 병렬 쿼리 실행 완료")
