def solve_part_1(binary_nums):
    gamma = []
    epsilon = []

    m = len(binary_nums)
    n = len(binary_nums[0])

    for pos in range(n):
        ones = zeroes = 0

        for i in range(m):
            if binary_nums[i][pos] == '1':
                ones += 1
            else:
                zeroes += 1
            
        if ones > zeroes:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

def solve_part_2(binary_nums):
    m = len(binary_nums)
    n = len(binary_nums[0])

    banned_o2 = set()
    banned_co2 = set()

    for pos in range(n):
        if len(banned_o2) == m-1:
            break

        ones = zeroes = 0

        for i in range(m):
            if i in banned_o2:
                continue
            
            if binary_nums[i][pos] == '1':
                ones += 1
            else:
                zeroes += 1    

        if ones >= zeroes:
            for i in range(m):
                if binary_nums[i][pos] == '0':
                    banned_o2.add(i)
        else:
            for i in range(m):                
                if binary_nums[i][pos] == '1':
                    banned_o2.add(i)

    for pos in range(n):
        ones = zeroes = 0

        if len(banned_co2) == m-1:
            break

        for i in range(m):
            if i in banned_co2:
                continue
            
            if binary_nums[i][pos] == '1':
                ones += 1
            else:
                zeroes += 1    

        if ones >= zeroes:
            for i in range(m):
                if binary_nums[i][pos] == '1':
                    banned_co2.add(i)
        else:
            for i in range(m):                
                if binary_nums[i][pos] == '0':
                    banned_co2.add(i)

    o2 = None
    co2 = None
    
    for i in range(m):
        if i not in banned_o2:
            o2 = binary_nums[i]
        
        if i not in banned_co2:
            co2 = binary_nums[i]
    
    return int(o2, 2) * int(co2, 2)

if __name__ == '__main__':
    with open('input_01.txt') as f:
        binary_nums = []

        for line in f.readlines():
            binary_nums.append(line.strip())

        print(solve_part_1(binary_nums))
        print(solve_part_2(binary_nums))