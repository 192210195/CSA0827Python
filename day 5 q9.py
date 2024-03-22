from itertools import zip_longest

def shuffle(l1, l2):
    shuffled = []
    for item1, item2 in zip_longest(l1, l2):
        
        if item1 is not None:
            shuffled.append(item1)
        if item2 is not None:
            shuffled.append(item2)
    
    return shuffled


l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']
print(shuffle(l1, l2)) 
