def check(number_a, number_b):
    if number_a % number_b == 0:
        return 0
    
    return str(number_a / number_b)[2]

def solution():
    a = int(input())
    b = int(input())
    answer = check(a, b)
    print(answer)

if __name__ == '__main__':
    solution()