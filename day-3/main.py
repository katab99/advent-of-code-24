'''
    Day 3 : Mull It Over
'''
import re


def main():
    with open('input.txt', 'r') as file:    
        content = file.read()
    
    # -- Part 1 
    # Regex pattern to match mul() with two numbers
    pattern :str = r'mul\((-?\d+\.?\d*),(-?\d+\.?\d*)\)' 
    result1 : int = 0
    
    for match in re.finditer(pattern, content):
        result1 += int(match.group(1)) * int(match.group(2))

    print(f" Part 1 -- Result: {result1}")

    # -- Part 2
    pattern_do : str = r'do\(\)'
    pattern_dont : str = r'don\'t\(\)'
    
    result2 : int = 0

    # to find all the do() and don't() 
    # first split the content by do() and then split by don't() - the first elem will be the do() match
    for s in re.split(pattern_do, content):
        do_match = re.split(pattern_dont, s)[0]
        
        for match in re.finditer(pattern, do_match):
            result2 += int(match.group(1)) * int(match.group(2))

    print(f" Part 2 -- Result: {result2}")

    pass

if __name__ == '__main__':
    main()