def test(func):
    A = [1, 2, 3, 4]
    print(f'input={A}, answer={func(A)}')
    B = [1, 1, 3, 4, 7]
    print(f'input={B}, answer={func(B)}')
    C = [2, 3, 4, 6]
    print(f'input={C}, answer={func(C)}')
    

def existsPartition(nums: 'List[int]') -> bool:
    totalSum = sum(nums)
    if totalSum%2 == 1: return False
    target = totalSum//2
    
    dp = [[False for x in range(target+1)] for y in range(len(nums))]
    
    for i in range(len(nums)):
        dp[i][0] = True
        
    for j in range(1, len(nums)):
        dp[0][j] = nums[j] == j
        
    for i in range(1, len(nums)):
        for j in range(1, target+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    
    return dp[-1][-1]
    
test(existsPartition)
