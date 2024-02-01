import threading
import pymysql
import queue
import time

def request_coupon(user_id, connection_pool):
    try:
        connection = connection_pool.get(True, 10)  # 연결 풀에서 연결을 가져옴

        with connection.cursor() as cursor:
            # 사용 가능한 쿠폰 선택
            cursor.execute("SELECT id FROM coupons WHERE status = 'available' ORDER BY id LIMIT 1 FOR UPDATE SKIP LOCKED;")
            result = cursor.fetchone()

            if result:
                coupon_id = result[0]
                # 쿠폰 상태 업데이트
                update_query = "UPDATE coupons SET status = 'assigned', user_id = %s WHERE id = %s;"
                cursor.execute(update_query, (user_id, coupon_id))
                connection.commit()
                print(f"User {user_id} received coupon {coupon_id}")
            else:
                print(f"No available coupons for user {user_id}")

    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        connection_pool.put(connection)  # 사용한 연결을 다시 연결 풀에 반환

def create_connection():
    return pymysql.connect(
        host='localhost',
        database='test',
        user='root',
        password='1234')

# 연결 풀 생성
connection_pool = queue.Queue()
for _ in range(10):  # 예를 들어 10개의 연결을 생성
    connection_pool.put(create_connection())


start_time = time.perf_counter()
threads = []
for _ in range(100):
    # 스레드 생성 및 실행
    for user_id in range(100):
        thread = threading.Thread(target=request_coupon, args=(user_id, connection_pool))
        thread.start()
        threads.append(thread)

    # 모든 스레드가 완료될 때까지 기다림
    for thread in threads:
        thread.join()

    threads.clear()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

# 연결 풀 내의 연결들을 종료
while not connection_pool.empty():
    connection = connection_pool.get()
    connection.close()
