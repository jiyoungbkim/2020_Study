# 비트연산 기본 2
# 시프트 연산 : 비트 값(열)을 지시한 만큼 왼쪽이나 오른쪽으로 이동시키는 연산자
# Right Shift(>>) : 오른쪽으로 특정 비트 수 만큼 이동하고 
# 빈자리는 양수 일때는 0, 음수 일때는 1로 채운다.
# Left Shift(<<) : 왼쪽으로 특정 비트 수 만큼 이동하고 빈자리는 0으로 채운다.
a, b = map(int, input().split())
print(a>>b)
print(a<<b)