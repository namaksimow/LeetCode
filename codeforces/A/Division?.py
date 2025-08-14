def define_division(number):
    if number < 1400:
        print('Division 4')

    elif number < 1600:
        print('Division 3')

    elif number < 1900:
        print('Division 2')

    else:
        print('Division 1')

def solution(number):
    for i in range(number):
        rating = int(input())
        define_division(rating)

if __name__ == '__main__':
    t = int(input())
    solution(t)