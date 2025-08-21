def find_melon_cost(number_n, number_k):
    if number_n <= number_k:
        return number_n * 3
    
    devider = 1
    x = 0
    answer_number = 0
    
    while number_k > 0 or number_n > 0:
        if devider * 3 > number_n:
            answer_number += 3 ** (x + 1) + x * (3 ** (x - 1))
            number_k -= 1
            number_n -= devider
            if number_n == 0:
                break
            x = 0
            devider = 1
        else:
            x += 1
            devider *= 3

    
    if number_n != 0:
        return -1
    
    return answer_number

def solution():
    t = int(input())
    for i in range(t):
        n, k = input().split()
        answer = find_melon_cost(int(n), int(k))
        print(answer)

solution()

# не решена