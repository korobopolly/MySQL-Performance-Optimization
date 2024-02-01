import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 랜덤 데이터 생성을 위한 설정
np.random.seed(0)
random.seed(0)

# 기본 설정
num_records = 1000000  # 100만개의 레코드
names = [f'Product_{i}' for i in range(1, 1001)]  # 예시 상품명
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 1, 1)
date_range = (end_date - start_date).days

# 랜덤 데이터 생성
data = {
    "name": np.random.choice(names, num_records),
    "price": np.round(np.random.uniform(10.0, 5000.0, num_records), 2),
    "created_at": [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(num_records)]
}

# 데이터 프레임 생성
df_products = pd.DataFrame(data)

# CSV 파일로 저장
file_path = 'products_1M.csv'
df_products.to_csv(file_path, index=False)
