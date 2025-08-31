def time_spell(number_t: str):
    if number_t.isdigit():
        number_t = int(number_t)
        hh = number_t // 3600
        mm = (number_t % 3600) // 60
        ss = number_t % 60

        return f'{hh:02d}:{mm:02d}:{ss:02d}'
    
    else:
        data = number_t.split(':')
        hh = data[0]
        mm = data[1]
        ss = data[2]
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

def solution():
    t = (input())
    answer = time_spell(t)
    print(answer)

if __name__ == '__main__':
    solution()