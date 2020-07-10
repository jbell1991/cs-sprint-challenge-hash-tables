def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    matches = []

    for num in a:
        hash_table[num] = num

    for key in hash_table.keys():
        if key and -key in hash_table.keys():
            if key > 0:
                matches.append(key)
    return matches
    
    # speed test without using a hashtable
    # matches = []
    # for num in a:
    #     if num and -num in a:
    #         if num > 0:
    #             matches.append(num)
    # return matches 

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
