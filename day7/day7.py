def prob_1_method(f):
    dir = {}
    print(f)
    for i in f[:-1]:
        if i.startswith("dir"):
            print(i)

def prob_1_test():  
    with open("test.txt", "r") as f:
        data = f.read().split("\n")

    assert prob_1_method(data) == 95437 

def prob_1():
    with open("prod.txt", "r") as f:
        data = f.read()
    print(prob_1_method(data))


# prob 2 method can work for prob 1 if you change r value and size of sorted block
# it's a much better way of doing it
def prob_2_method(f):
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
