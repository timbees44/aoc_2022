def prob_1_method(f):
    lines = f.readlines()

    stacks = []
    end = False
    for line in lines:
        if not line or line[0] == "m":
            
def prob_1_test():
    with open("test_input.txt", "r") as f:
        assert prob_1_method(f) == "CMZ"

def prob_1():
    pass

if __name__ == "__main__":
    prob_1_test()
    print("test for prob 1 passed")
