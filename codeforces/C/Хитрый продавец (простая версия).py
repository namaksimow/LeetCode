def find_melon_number(number_n):
    if number_n < 3:
        return number_n * 3
    
    devider = 1
    x = 0
    answer_number = 0

    while number_n >= 3:
        if devider * 3 > number_n:
            answer_number += 3 ** (x + 1) + x * 3 ** (x - 1)
            number_n -= devider
            x = 0
            devider = 1
        else:
            x += 1
            devider *= 3

    return answer_number + find_melon_number(number_n)

def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = find_melon_number(n)
        print(ans)

solution()