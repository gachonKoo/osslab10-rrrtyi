import sys

number = int(sys.argv[1])  # 사용자 입력으로 받은 숫자

# 약수를 찾기 위해 1부터 number-1까지 반복
for i in range(1, number):
    # number가 i로 나누어 떨어지면 (즉, i는 number의 약수)
    if number % i == 0:
        print(i, end=" ")  # 약수 출력

print()  # 마지막에 줄바꿈
