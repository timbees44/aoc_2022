import string

def prob_1_method(inpt):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priority = 0
    for line in inpt.readlines():
        half = int((len(line)-1)/2)
        match = [x for x in line[:half] if x in line[half:]]
        priority += alphabet.index(match[0]) + 1
    return priority 

def test_prob_1():
    #test case
    """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
    f = open("test_input_1.txt", "r")
    assert prob_1_method(f) == 157, "should be 157"   

def prob_1():
    f = open("prod_input.txt", "r")
    print("round 1 answer = {}".format(prob_1_method(f)))

def prob_2_method(inpt):
    n = 3 
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    data = inpt.read().strip()
    bag = data.split("\n")

    c = 0
    priority = 0
    while c < len(bag):
        b1 = bag[c]
        b2 = bag[c + 1]
        b3 = bag[c + 2]
        for i in b1:
            if i in b2 and i in b3:
                priority += alphabet.index(i) + 1
                break
        c += 3

    return priority

def test_prob_2():
    #test cases (two groups)
    """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
    f = open("test_input_2.txt", "r")
    assert prob_2_method(f) == 70

def prob_2():
    f = open("prod_input.txt", "r")
    print("round 2 answer = {}".format(prob_2_method(f)))

if __name__ == "__main__":
    test_prob_1()
    print("tests passed for prob 1")
    prob_1()
    print("Round 2")
    test_prob_2()
    print("tests passed for prob 2")
    prob_2()
