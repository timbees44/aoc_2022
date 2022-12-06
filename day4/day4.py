def prob_1_method(f):
    data = f.read().strip().replace("-", ",").split("\n")
    count = 0
    for d in data:
        pairs = d.split(",")
        
        range1 = list(range(int(pairs[0]), int(pairs[1])+1))
        range2 = list(range(int(pairs[2]), int(pairs[3])+1))
        
        if len(range1) < 1 or len(range2) < 1:
            count += 0
        elif all(x in range1 for x in range2):
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
        print(f"Problem 1 solution: {prob_1_method(f)}")

def prob_2_method(f):
    data = f.read().strip().replace("-", ",").split("\n")
    count = 0
    for d in data:
        pairs = d.split(",")
        
        range1 = list(range(int(pairs[0]), int(pairs[1])+1))
        range2 = list(range(int(pairs[2]), int(pairs[3])+1))
        
        if len(range1) < 1 or len(range2) < 1:
            count += 0
        elif any(x in range1 for x in range2):
            count += 1
        elif any(x in range2 for x in range1):
            count += 1
    
    return count

def prob_2_test():
    """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """
    with open("test_input_1.txt", "r") as f:
        assert prob_2_method(f) == 4

def prob_2():
    with open("prod_input.txt", "r") as f:
        print(f"Problem 2 solution: {prob_2_method(f)}")


     
if __name__ == "__main__":
    prob_1_test()
    print("test 1 passed")
    prob_1()
    prob_2_test()
    print("test 2 passed")
    prob_2()
