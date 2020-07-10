def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_table = {}

    for idx, weight in enumerate(weights):
        hash_table[weight] = idx
        entry = limit - weight
        if entry in hash_table:
            idx_2 = hash_table[entry]
            if idx > idx_2:
                return idx, idx_2
            elif idx < idx_2:
                return idx_2, idx
            elif idx == idx_2:
                return idx + 1, idx_2
    
    return

weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))
