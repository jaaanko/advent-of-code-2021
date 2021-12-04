from copy import deepcopy

def mark_boards(num, boards):
    R = len(boards[0])
    C = len(boards[0][0])
    
    for board in boards:
        for r in range(R):
            for c in range(C):
                if board[r][c] == num:
                    board[r][c] = -1

def find_winner(boards, winners):
    R = len(boards[0])
    C = len(boards[0][0])
    winner = None

    for i, board in enumerate(boards):
        if i in winners:
            continue

        for r in range(R):
            curr = 0
            for c in range(C):
                if board[r][c] == -1:
                    curr += 1
            
            if curr == C:
                winners.add(i)
                winner = board
        
        for c in range(C):
            curr = 0
            for r in range(R):
                if board[r][c] == -1:
                    curr += 1
            
            if curr == R:
                winners.add(i)
                winner = board

    return winner

def get_unmarked_nums(board):
    unmarked_nums = []
    R = len(board)
    C = len(board[0])
   
    for r in range(R):
        for c in range(C):
            if board[r][c] != -1:
                unmarked_nums.append(board[r][c])

    return unmarked_nums

def solve_part_1(nums, boards):
    winners = set()

    for num in nums:
        mark_boards(num, boards)
        winner = find_winner(boards, winners)

        if winner:
            return sum(get_unmarked_nums(winner)) * num

    return -1

def solve_part_2(nums, boards):
    winner = None
    lastest_num = -1
    winners = set()

    for num in nums:
        mark_boards(num, boards)
        winner = find_winner(boards, winners)
        
        if len(winners) == len(boards):
            lastest_num = num
            break

    return -1 if not winner else sum(get_unmarked_nums(winner)) * lastest_num

if __name__ == '__main__':
    with open('input_01.txt') as f:
        nums = [int(x) for x in f.readline().strip().split(',')]
        boards = []

        f.readline()

        for board in f.read().split('\n\n'):
            tmp = []
            
            for row in board.split('\n'):
                tmp.append([int(num) for num in row.split()])

            boards.append(tmp)

        print(solve_part_1(nums, deepcopy(boards)))
        print(solve_part_2(nums, deepcopy(boards)))