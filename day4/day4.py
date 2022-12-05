
# rethink this whole thing
def prob_1_method(f):
    data = f.read().strip().split("\n")
    count = 0
    for pair in data:
        p = pair.split(",")
        start = p[0][:p[0].index("-")]
        start2 = p[1][:p[1].index("-")]
        end = p[0][p[0].index("-"):]
        end2 = p[1][p[1].index("-"):]
        
        range1 = range(int(p[0][:p[0].index("-")]), int(p[0][p[0].index("-") + 1:]))
        range2 = range(int(p[1][:p[1].index("-")]), int(p[1][p[1].index("-") + 1:]))
        len1 = len(range1)
        len2 = len(range2)

        if len1 < len2 and start in range2 and end in range2:
            count += 1
        elif len1 > len2 and start2 in range1 and end2 in range1:
            count += 1
        elif len1 == len2 and start == start2:
            count += 1
    
    print(count)
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
    
if __name__ == "__main__":
    prob_1_test()
