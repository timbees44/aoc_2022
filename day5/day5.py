def prob_1_method(f):
    data = f.read().strip().split("\n")
    print(data)

    for i in data:
        if not i or i[1] == "1":
            break
        print(i)


def prob_1_test():
    with open("test_input.txt", "r") as f:
        assert prob_1_method(f) == "CMZ"

def prob_1():
    pass

if __name__ == "__main__":
    prob_1_test()
    print("test for prob 1 passed")
