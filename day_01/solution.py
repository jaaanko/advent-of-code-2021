def solve_part_1(nums):
    res = 0
    
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            res += 1
    
    return res

def solve_part_2(nums):
    res = 0
    prev = float('inf')
    curr = nums[0] + nums[1]
    
    for i in range(2, len(nums)):
        curr += nums[i]
        
        if curr > prev:
            res += 1
        
        prev = curr
        curr -= nums[i - 2]

    return res

if __name__ == '__main__':
    with open('input_01.txt') as f:
        nums = [int(line) for line in f.readlines()]

        print(solve_part_1(nums))
        print(solve_part_2(nums))