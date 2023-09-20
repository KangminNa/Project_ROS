"""ex02_06_3.py"""
from sys import path
from ex02_06_1 import foo

# from ~ import 문을 사용하면 이름 공간을 생략하고 직접 해당 이름에 접근 가능

def boo():
    print(f"__name__ is {__name__}")

def main():
    boo()
    foo()
    print(path)

if __name__ == "__main__":
    main()