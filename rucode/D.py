def solution():
    x, y, r = map(int, input().split())

    if x == 0 and y == 0:
        return 5
    
    elif x > 0 and y > 0:
        count = 1
        if x - r <= 0 or y - r <= 0:
            count += 1
        if x - r < 0:
            count += 1
        if y - r < 0:
            count += 1
        if x ** 2 + y ** 2 < r ** 2:
            count += 1
        return count
    
    elif x < 0 and y > 0:
        count = 1
        if x + r >= 0 or y - r <= 0:
            count += 1
        if x + r > 0:
            count += 1
        if y - r < 0:
            count += 1
        if x ** 2 + y ** 2 < r ** 2:
            count += 1
        return count
    
    elif x < 0 and y < 0:
        count = 1
        if x + r >= 0 or y + r >= 0:
            count += 1
        if x + r > 0:
            count += 1
        if y + r > 0:
            count += 1
        if x ** 2 + y ** 2 < r ** 2:
            count += 1
        return count
        
    elif x > 0 and y < 0:
        count = 1
        if x - r <= 0 or y + r >= 0:
            count += 1
        if x - r < 0:
            count += 1
        if y + r > 0:
            count += 1
        if x ** 2 + y ** 2 < r ** 2:
            count += 1
        return count
    

if __name__ == '__main__':
    answer = solution()
    print(answer)