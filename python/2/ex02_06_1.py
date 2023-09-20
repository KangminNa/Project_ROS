"""ex02_06_1.py"""
# 한 모듈에서 다른 모듈 접근
# foo() 함수 정의가 포함된 모듈 정의
def foo():
    print(f"__name__ is {__name__}")