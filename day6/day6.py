def prob_1_method(f):
    p = 0
    r = 4
    for i in f:
        block = sorted(f[p:p+4])
        p += 1
        if block.count(block[1]) > 1 or block.count(block[2]) > 1:
            r += 1
        else:
            break
    return r

def prob_1_test():  
    with open("test.txt", "r") as f:
        data = f.read()

    assert prob_1_method(data) == 11

def prob_1():
    with open("prod.txt", "r") as f:
        data = f.read()
    print(prob_1_method(data))


# prob 2 method can work for prob 1 if you change r value and size of sorted block
# it's a much better way of doing it
def prob_2_method(f):
    p = 0
    r = 14
    for i in f:
        block = sorted(f[p:p+14])
        p += 1
        if len(block) != len(set(block)):
            r += 1
        else:
            break  
    
    print(r)
    return r

def prob_2_test():  
    with open("test.txt", "r") as f:
        data = f.read()

    assert prob_2_method(data) == 26 

def prob_2():
    with open("prod.txt", "r") as f:
        data = f.read()
    print(prob_2_method(data))


if __name__ == "__main__":
    prob_1_test()
    print("problem 1 tests passed")
    prob_1()
    prob_2_test()
    print("problem 2 tests passed")
    prob_2() 
