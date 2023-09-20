"""ex02_02.py"""
import numpy as np

def creat_data(n):
    return np.random.standard_normal(n) # 백만개의 난수를 반환

def calc_mean_val_std(data):
    return (np.mean(data), np.var(data), np.std(data)) # 평균, 분산, 표준편차를 계산해 f-string 출력

def main():
    data = creat_data(1_000_000)
    mean, var, std = calc_mean_val_std(data)
    print(f"|{mean = }|{var = :>30}|{std = :^10.2f}|") 
    # 따옴표를 활용해 문자열 반환
    # ":" 폭을 지정할 수 있음
    # "^" 가운데 정렬
    # 

if __name__ == "__main__":
    main()

# 문자열 스트링
# f-string : 쉽게 문자열 타입을 만들 수 있음