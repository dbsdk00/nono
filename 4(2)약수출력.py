n = int(input("숫자를 입력하세요 : "))

for i in range(1, n + 1):
    if n % i == 0 :
        print(i, end = '')