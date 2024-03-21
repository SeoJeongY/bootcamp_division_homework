"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n = int(input())
    total_sum = calculate_sum(n)
    factorial = calculate_factorial(n)
    print("1부터 {}까지의 정수의 합: {}".format(n, total_sum))
    print("{} 팩토리얼: {}".format(n, factorial))
    def calculate_sum(n):
        total_sum = sum(range(1, n+1))
    return total_sum

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial



    return


if __name__ == '__main__':
    main()
