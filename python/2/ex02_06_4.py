"""ex02_06_4.py"""
import mini.ex02_06_1
from mini.ex02_06_1 import foo

# 부모 모듈과 하위 모듈을 하나의 경로로 표현할 때는 인터넷 도메인 이름처럼 점(.)으로 연결

def main():
    nkm.ex02_06_1.foo()
    foo()

if __name__ == "__main__":
    main()