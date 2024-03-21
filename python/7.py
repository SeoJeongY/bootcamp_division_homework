"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    month = int(input("월(1부터 12까지의 정수): "))

    if month == 2:
        print("해당하는 달의 날 수는 28일 또는 29일")
    elif month in [4,6,9,11]:
        print("해당하는 달의 날 수는 30일")
    else:
        print("해당하는 달의 날 수는 31일")


    return


if __name__ == '__main__':
    main()
