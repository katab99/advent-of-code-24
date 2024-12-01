'''
    Day 1 : Historian Hysteria
'''

def main():
    left_arr : list = []
    right_arr : list = []

    # Read file line by line
    with open('input.txt', 'r') as file:    
        for line in file:
            data1, data2 = line.split()
            left_arr.append(int(data1))
            right_arr.append(int(data2))


    # Part 1
    left_arr.sort()
    right_arr.sort()

    result1 : int = 0

    for d1, d2 in zip(left_arr, right_arr):
        result1 += abs(d1 - d2)

    print(f'Part 1 solution : {result1}')


    # Part 2
    right_hash : dict = {}

    # create hash map for frequency of elements in right_arr
    for data in right_arr:
        right_hash[data] = right_hash.get(data, 0) + 1

    # calculate the result
    result2 = 0
    for data in left_arr:
        result2 += data * right_hash.get(data, 0)

    print(f'Part 2 solution : {result2}')
    
    pass

if __name__ == "__main__":
    main()