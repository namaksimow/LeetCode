def solution():
    n = int(input())
    if n == 0:
        return 0
    
    MOD = 10**9 + 7
    dp0 = 10  
    dp1 = 20  
    dp2 = 1   
    dp3 = 0

    for i in range(1, n):
        new_dp0 = (dp1 * 10 + dp2 * 10 + dp3 * 10) % MOD
        new_dp1 = (dp0 * 20) % MOD
        new_dp2 = (dp0 * 1) % MOD
        new_dp3 = (dp1 * 2) % MOD
        
        dp0, dp1, dp2, dp3 = new_dp0, new_dp1, new_dp2, new_dp3
        
    total = (dp0 + dp1 + dp2 + dp3) % MOD
    return total

if __name__ == '__main__':
    answer = solution()
    print(answer)