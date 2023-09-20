"""ex02_06_2.py"""
import sys
import ex02_06_1

# 앞서 정의한 모듈을 import해서 foor() 함수 호출


def boo():
    print(f"__name__ is {__name__}")

def main():
    boo()
    ex02_06_1.foo()
    print(sys.path)

if __name__ == "__main__":
    main()