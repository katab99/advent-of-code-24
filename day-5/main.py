'''
    Day 5 : Print Queue
'''
import math

def part_one(updates, ordering_rules):
    result1 = 0

    for update in updates:
        is_correct : bool = True      
        for elem in update:
            for i in range(update.index(elem) + 1, len(update)):
                # the current element should be later than the next element, the rule is incorrect
                if((update[i], elem) in ordering_rules):
                    is_correct = False
                    break

        if is_correct:

            result1 += update[math.floor(len(update) / 2) ]

    print(f'Part 1: {result1}')

    return None

def part_two(updates, ordering_rules):
    result2 = 0
    for update in updates:
        is_correct : bool = True
        
        for j in range(len(update)):
            for i in range(j + 1, len(update)):
                # the current element should be later than the next element, the rule is incorrect
                if((update[i], update[j]) in ordering_rules):
                    is_correct = False
                    update[i], update[j] = update[j], update[i]

            
        if is_correct == False:
            result2 += update[math.floor(len(update) / 2) ]

    print(f'Part 2: {result2}')

    return None


def main():
    FILE : str = 'input.txt'

    ordering_rules : list = []
    updates : list = []
    is_empty_line : bool = False

    with open(FILE, 'r') as file:    
        for line in file:
            if line in ['\n', '\r\n']:
                is_empty_line = True
                continue # do nothing else in this iteration

            if is_empty_line:
                data : list = line.split(',')
                data[-1] = data[-1].strip()
                updates.append([int(x) for x in data])
            else:
                data : list = line.split('|')
                data[1] = data[1].strip() # remove the newline character
                ordering_rules.append(( int(data[0]), int(data[1])))        

    # Part 1
    part_one(updates, ordering_rules)

    # Part 2
    part_two(updates, ordering_rules)
    
    pass

if __name__ == '__main__':
    main()