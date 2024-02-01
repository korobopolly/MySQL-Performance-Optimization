import csv
import random
import string

# CSV 파일명
filename = "test_data.csv"

# 데이터 생성
num_rows = 10000000

def generate_random_string(length=100):
    """ 100 글자의 랜덤 문자열 생성 """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1, num_rows + 1):
        id = i
        value = generate_random_string()
        writer.writerow([id, value])

print(f"{num_rows}개의 테스트 데이터가 {filename}에 저장되었습니다.")
