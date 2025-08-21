def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        answer = []
        n_len = len(str(n)) - 1
        if n_len < 1:
            print(0)
        else:
            for i in range(n_len, 0, -1):
                var = 10 ** (i) + 1
                if n % var == 0:
                    answer.append(str(n // var))

            print(len(answer))

            if answer:
                print(' '.join(answer))
                
solution()
