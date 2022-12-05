

def prob_1_method(f):
    data = f.read().strip().replace("-", ",").split("\n")
    count = 0
    for d in data:
        pairs = d.split(",")
        
        range1 = list(range(int(pairs[0]), int(pairs[1])))
        range2 = list(range(int(pairs[2]), int(pairs[3])))
        
        if all(x in range1 for x in range2):
            count += 1
        elif all(x in range2 for x in range1):
            count += 1
        
    return count

def prob_1_test():
    """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """
    with open("test_input_1.txt", "r") as f:
        assert prob_1_method(f) == 2
        
def prob_1():
    with open("prod_input.txt", "r") as f:
        print(prob_1_method(f))
    
if __name__ == "__main__":
    prob_1_test()
    print("test 1 passed")
    prob_1()
