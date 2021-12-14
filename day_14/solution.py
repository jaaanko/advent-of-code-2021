from collections import Counter, defaultdict

def solve_part_1(template, between, steps):
    n = len(template)
    pair_counts = defaultdict(int)
    single_counts = Counter(template)

    for i in range(1, n):
        pair_counts[template[i - 1] + template[i]] += 1
    
    for _ in range(steps):
        new_pair_counts = defaultdict(int)

        for pair in list(pair_counts):
            if pair_counts[pair] == 0:
                continue
            
            if pair in between:
                single_counts[between[pair]] += pair_counts[pair]
                new_pair_counts[pair[0] + between[pair]] += pair_counts[pair]
                new_pair_counts[between[pair] + pair[1]] += pair_counts[pair]
        
        pair_counts = new_pair_counts                

    return max(single_counts.values()) - min(single_counts.values())

def solve_part_2(template, between, steps):
    return solve_part_1(template, between, steps)

if __name__ == '__main__':
    with open('input_01.txt') as f:
        template, rules = f.read().split('\n\n')
        template = template.strip()
        between = {}

        for rule in rules.split('\n'):
            pair, char = rule.split(' -> ')
            between[pair] = char

        print(solve_part_1(template, between, 10))
        print(solve_part_2(template, between, 40))