import string

def prob_1_method(inpt):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    count = 0
    for line in inpt.readlines():
        half = int((len(line)-1)/2)
        match = [x for x in line[:half] if x in line[half:]]
        count += alphabet.index(match[0]) + 1
    return count

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
    f = open("test_input.txt", "r")
    assert prob_1_method(f) == 157, "should be 157"   

def prob_1():
    f = open("prod_input.txt", "r")
    print(prob_1_method(f))

def prob_2_method(inpt):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    count = 0
    line_count = 0
    for line in inpt.readlines():
        while line_count < 3:



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
    assert prob_2_method(f) = 70

if __name__ == "__main__":
    test_prob_1()
    print("tests passed")
    prob_1()
    

