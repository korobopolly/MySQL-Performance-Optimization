import pymysql
import time
import threading

# 데이터베이스 설정
host = 'localhost'
port = 3306
user = 'root'
password = '1234'
database = 'test'

# 데이터베이스 연결 설정
def get_db_connection():
    return pymysql.connect(host=host, user=user, password=password, db=database)

# Bulk Insert 쿼리 실행 함수
def insert_orders():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            query = """
            INSERT INTO shopping_orders (user_id, product_id, quantity, order_date)
            SELECT user_id, product_id, quantity, NOW()
            FROM shopping_cart
            WHERE cart_added_date > '2021-01-01 00:00:00' AND cart_added_date <= NOW();
            """
            cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


# 병렬 실행을 위한 스레드 생성 및 실행
def run_parallel_inserts(num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=insert_orders)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# 스레드 수 설정 및 실행
num_threads = 10  # 동시에 실행할 스레드 수
start_time = time.perf_counter()
run_parallel_inserts(num_threads)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
