def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input()
        m = int(input())
        b = input()
        c = input()
        for i in range(len(c)):
            if c[i] == 'D':
                a = a + b[i]
            else:
                a = b[i] + a
    
        print(a)


solution()