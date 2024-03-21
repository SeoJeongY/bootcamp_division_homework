"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n = int(input("양의 정수 n을 입력하세요: "))

    total_sum = sum(range(1, n+1))
    print("1부터 {}까지의 합: {}".format(n, total_sum))

    return


if __name__ == '__main__':
    main()
