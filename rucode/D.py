def solution():
    x, y, r = map(int, input().split())

    colors = set()
    
    if abs(x) <= r or abs(y) <= r:
        colors.add('black')
    
    dots = [
        [x + r, y],
        [x - r, y],
        [x, y + r],
        [x, y - r],
        [x + r/2*(2**0.5), y + r/2*(2**0.5)],
        [x + r/2*(2**0.5), y - r/2*(2**0.5)],
        [x - r/2*(2**0.5), y + r/2*(2**0.5)],
        [x - r/2*(2**0.5), y - r/2*(2**0.5)]
    ]

    for i in range(len(dots)):
        points = dots[i]
        x_p = points[0]
        y_p = points[1]
        if x_p > 0 and y_p > 0:
            colors.add('gold')
        
        if x_p < 0 and y_p > 0:
            colors.add('white')

        if x_p < 0 and y_p < 0:
            colors.add('blue')

        if x_p > 0 and y_p < 0:
            colors.add('red')
        
    return len(colors)


if __name__ == '__main__':
    answer = solution()
    print(answer)