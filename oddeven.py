number = [4, 13, 15, 70, 51, 23, 38, 9, 12, 5]
even = []
odd = []

i = 0
while i < len(number):
    if number[i] % 2 == 0:
        even.append(number[i])
    else:
        odd.append(number[i])
    i += 1

even.sort()
odd.sort()

print('짝수 리스트 =', even)
print('홀수 리스트 =', odd)
