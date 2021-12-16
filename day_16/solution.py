from math import prod

def get_version(packet, offset = 0):
    return int(packet[offset:offset + 3], 2)

def get_type_id(packet, offset = 0):
    return int(packet[offset + 3:offset + 6], 2)

def get_len_type_id(packet, offset = 0):
    return int(packet[offset + 6])

def get_literal_value(packet, offset = 0):
    n = len(packet)

    curr = []
    for i in range(offset + 6, n, 5):
        curr.append(packet[i + 1:i + 5])
        if packet[i] == '0':
            break

    return int(''.join(curr), 2) 

def is_literal(packet, offset = 0):
    return get_type_id(packet, offset) == 4   

def get_end_of_literal(packet, offset = 0):
    for i in range(offset + 6, len(packet), 5):
        if packet[i] == '0':
            return i + 5
    
    return -1

def apply_operation(type_id, nums):
    if type_id == 0:
        return sum(nums)

    if type_id == 1:
        return prod(nums)
    
    if type_id == 2:
        return min(nums)

    if type_id == 3:
        return max(nums)
    
    if type_id == 5:
        return 1 if nums[0] > nums[1] else 0
    
    if type_id == 6:
        return 1 if nums[0] < nums[1] else 0

    if type_id == 7:
        return 1 if nums[0] == nums[1] else 0
    
    return 0

def helper(packet, offset = 0):
    version_total = get_version(packet, offset)

    if is_literal(packet, offset):
        end = get_end_of_literal(packet, offset)
        return end, version_total, get_literal_value(packet, offset)

    results = []
    initial_offset = offset
    end = -1

    if get_len_type_id(packet, offset) == 0:
        total_len = int(packet[offset + 7:offset + 22], 2)
        offset += 22

        while total_len > 0:
            end, version, expr_res = helper(packet, offset)
            results.append(expr_res)
            version_total += version
            total_len -= end - offset
            offset = end 
    else:
        total_count = int(packet[offset + 7:offset + 18], 2)
        offset += 18

        for _ in range(total_count):
            end, version, expr_res = helper(packet, offset)
            results.append(expr_res)
            version_total += version
            offset = end     

    return end, version_total, apply_operation(get_type_id(packet[initial_offset:]), results) 

def hex_to_binary(hex):
    binary = bin(int(hex, 16))[2:]

    while (len(binary) < len(hex) * 4):
        binary = '0' + binary

    return binary

def solve_part_1(packet):
    return helper(packet)[1]

def solve_part_2(packet):
    return helper(packet)[2]

if __name__ == '__main__':
    with open('input_01.txt') as f:
        packet = hex_to_binary(f.readline().strip())

        print(solve_part_1(packet))
        print(solve_part_2(packet))    